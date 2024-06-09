import heapq
import struct
from pathlib import Path
from collections import Counter
from abc import ABC, abstractmethod
from typing import Union, List, Dict, Tuple, ByteString

import cv2
import pywt
import numpy as np
from PIL import Image

import src.core.utils as utils


class Encoder(ABC):
    """
    Encoder 抽象基类
    """
    @abstractmethod
    def encode(self, image_path, save_path):
        raise NotImplementedError("抽象类中不进行实现: Encoder.encode()!")

    def read(self, file_path):
        raise NotImplementedError("抽象类中不进行实现: Encoder.read()!")

    def save(self, file_path, bitstream):
        raise NotImplementedError("抽象类中不进行实现: Encoder.save()!")


class JP2KEncoder(Encoder):
    """
    JPEG2000 编码器
    """

    def __init__(self, q_factor: int = 5, tile_size: int = 128) -> None:
        self.q_factor = q_factor
        # TODO: 后面可以改成自适应图片（求300以内的 w 和 h 的最大公因数）
        self.tile_size = tile_size

    def encode(self, img: np.ndarray) -> ByteString:
        """
        实现编码过程，将图片数据编码为jp2k格式的码流并保存
        """
        img = JP2KEncoder.convert_color2YUV(img)
        tiles = JP2KEncoder.tile_np_image(img, self.tile_size)
        bitstream, _ = JP2KEncoder.organize_bitstream(tiles, self.q_factor)
        return bitstream

    def read(self, img_path: str) -> np.ndarray:
        return cv2.imread(img_path)

    def save(self, save_path: str, bitstream: ByteString) -> None:
        with open(save_path, 'wb') as f:
            f.write(bitstream)

    def get_wavelet_image(self, img: np.ndarray) -> Tuple:
        lt_0, (rt_0, lb_0, rb_0) = JP2KEncoder.discrete_wavelet_transform_2d(
            img[:, :, 0])
        lt_1, (rt_1, lb_1, rb_1) = JP2KEncoder.discrete_wavelet_transform_2d(
            img[:, :, 1])
        lt_2, (rt_2, lb_2, rb_2) = JP2KEncoder.discrete_wavelet_transform_2d(
            img[:, :, 2])
        lt = np.stack([lt_0, lt_1, lt_2], axis=2)
        rt = np.stack([rt_0, rt_1, rt_2], axis=2)
        lb = np.stack([lb_0, lb_1, lb_2], axis=2)
        rb = np.stack([rb_0, rb_1, rb_2], axis=2)
        return lt, rt, lb, rb

    def get_gray_wavelet_image(self, img: np.ndarray) -> Tuple:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lt, (rt, lb, rb) = JP2KEncoder.discrete_wavelet_transform_2d(gray_img)
        return lt, rt, lb, rb

    @staticmethod
    def tile_np_image(image, tile_size) -> List[np.ndarray]:
        """
        将图像分割成指定大小的块
        :param image: 输入图像,NumPy数组
        :param tile_size: 块大小(h, w),整数或元组
        :return: 图像块列表
        """
        h, w = image.shape[:2]
        tiles = []

        if isinstance(tile_size, int):
            tile_size = utils.turn2pair(tile_size)
        tile_h, tile_w = tile_size

        # 遍历图像并提取块
        for x in range(0, w, tile_w):
            for y in range(0, h, tile_h):
                tile = image[y:y+tile_h, x:x+tile_w]
                tiles.append(tile)

        return tiles

    @staticmethod
    def convert_color2YUV(image: Union[np.ndarray, Image.Image]) -> np.ndarray:
        """
        颜色变换: 从RGB转换到YUV
        :param image: 输入图像, PIL.Image.Image 或 np.ndarray
        :return: YUV图像 np.ndarray
        """
        yuv_img = None
        if isinstance(image, Image.Image):
            yuv_img = cv2.cvtColor(utils.pil2np(image), cv2.COLOR_RGB2YUV)
        else:
            yuv_img = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        return yuv_img

    @staticmethod
    def discrete_wavelet_transform_2d(image: np.ndarray):
        """
        对图像块进行离散小波变换
        :param image: 图像块(2D)
        :return: 小波变换系数
        """
        coeffs = pywt.dwt2(image, 'haar')
        return coeffs

    @staticmethod
    def quantize(coeffs: Tuple, q_factor: int):
        """
        对小波系数进行量化
        :param coeffs: 小波系数
        :param q_factor: 量化因子
        :return: 量化后的系数
        """
        cA, (cH, cV, cD) = coeffs
        cA = np.round(cA / q_factor)
        cH = np.round(cH / q_factor)
        cV = np.round(cV / q_factor)
        cD = np.round(cD / q_factor)
        return cA, (cH, cV, cD)

    @staticmethod
    def huffman_encoding(data: np.ndarray):
        """
        霍夫曼编码
        :param data: 输入数据
        :return: 编码后的数据和霍夫曼树
        """
        frequency = Counter(data)
        heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        huffman_tree = sorted(heapq.heappop(
            heap)[1:], key=lambda p: (len(p[-1]), p))
        huffman_dict = {symbol: code for symbol, code in huffman_tree}
        encoded_data = "".join(huffman_dict[symbol] for symbol in data)

        return encoded_data, huffman_tree

    @staticmethod
    def serialize_huffman_tree(huffman_tree: Dict) -> List[Tuple[int, str]]:
        """
        序列化霍夫曼树以便存储
        :param huffman_tree: 霍夫曼树
        :return: 序列化的霍夫曼树
        """
        serialized_tree = []
        for symbol, code in huffman_tree:
            serialized_tree.append((symbol, code))
        return serialized_tree

    @staticmethod
    def process_block(block: np.ndarray, q_factor: int) -> Tuple[str, Dict]:
        """
        对 block 进行离散小波变换、量化和熵编码
        :param block: 要处理的数据块
        :param q_factor: 量化因子
        :return: 处理好的数据
        """
        coeffs = JP2KEncoder.discrete_wavelet_transform_2d(block)
        cA, (cH, cV, cD) = JP2KEncoder.quantize(coeffs, q_factor)
        # 将量化后的系数转成一行数组
        flat_array = np.hstack(
            (cA.flatten(), cH.flatten(), cV.flatten(), cD.flatten())).astype(int)
        encoded_data, huffman_tree = JP2KEncoder.huffman_encoding(flat_array)
        return encoded_data, huffman_tree

    @staticmethod
    def organize_bitstream(blocks: List[np.ndarray], q_factor: int) -> Tuple[ByteString, Dict[int, str]]:
        """
        组织码流
        :param blocks: 图像块列表
        :param q_faactor: 量化因子
        :return: 码流
        """
        bitstream = bytearray()
        huffman_trees = []

        for block in blocks:
            # 对每个通道进行处理
            for channel in range(block.shape[2]):
                # 对数据进行小波变换、量化和熵编码
                encoded_data, huffman_tree = JP2KEncoder.process_block(
                    block[:, :, channel], q_factor)
                huffman_trees.append(huffman_tree)
                # 序列化霍夫曼树
                serialized_tree = JP2KEncoder.serialize_huffman_tree(
                    huffman_tree)

                # 将编码后的数据写入码流
                bitstream += struct.pack('I', len(encoded_data))
                bitstream += encoded_data.encode('utf-8')
                bitstream += struct.pack('I', len(serialized_tree))
                for symbol, code in serialized_tree:
                    bitstream += struct.pack('i', symbol)
                    bitstream += struct.pack('I', len(code))
                    bitstream += code.encode('utf-8')
        return bitstream, huffman_trees
