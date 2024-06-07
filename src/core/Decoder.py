import struct
from abc import ABC, abstractmethod
from typing import Union, List, Dict, Tuple, ByteString

import cv2
import pywt
import numpy as np

import src.core.utils as utils

BYTE_LENGTH = 4

class Decoder(ABC):
    """
    Decoder 抽象基类
    """
    @abstractmethod
    def decode(self, image_path, decoded_path):
        raise NotImplementedError("抽象类中不进行实现: Decoder.decode()!")
    
    def read(self, file_path):
        raise NotImplementedError("抽象类中不进行实现: Decoder.read()!")

    def save(self, save_path, bitstream):
        raise NotImplementedError("抽象类中不进行实现: Decoder.save()!")

class JP2KDecoder(Decoder):
    """
    JPEG2000 解码器
    """
    def __init__(self, tile_size: int=128, q_factor: int=5, image_shape: Tuple=(768, 512)) -> None:
        # HACK: 之后改成从码流中获取
        self.tile_size = tile_size
        self.q_factor = q_factor
        self.image_shape = image_shape
    
    def decode(self, bitstream: ByteString) -> np.ndarray:
        """
        针对JP2K格式的文件进行解码，并保存到新文件
        :param image_path: JP2K格式的文件路径
        :param save_path: 新文件路径
        """
        decoded_blocks = JP2KDecoder.decode_bitstream(bitstream)
        decoded_tiles = JP2KDecoder.get_tiles_from_data(decoded_blocks, self.tile_size, self.q_factor)
        decode_img = JP2KDecoder.merge_image(decoded_tiles, self.tile_size, self.image_shape)
        decode_img = JP2KDecoder.convertColor2RGB(decode_img)
        decode_img = cv2.cvtColor(decode_img, cv2.COLOR_RGB2BGR)
        return decode_img

    def read(self, image_path: str) -> ByteString:
        bitstream = None
        with open(image_path, 'rb') as f:
            bitstream = f.read()
        return bitstream
    
    def save(self, save_path: str, img: np.ndarray) -> None:
        cv2.imwrite(save_path, img)

    @staticmethod
    def deserialize_huffman_tree(serialized_tree:List[Tuple[int, str]]) -> Dict[str,int]:
        """反序列化霍夫曼树"""
        return {code: symbol for symbol, code in serialized_tree}

    @staticmethod
    def huffman_decoding(encoded_data: str, huffman_tree: Dict[str, int]) -> List[int]:
        """
        霍夫曼解码
        :param encoded_data: 编码后的数据
        :param huffman_tree: 霍夫曼树
        :return: 解码后的数据
        """
        decoded_data = []
        code = ""
        for bit in encoded_data:
            code += bit
            if code in huffman_tree:
                decoded_data.append(huffman_tree[code])
                code = ""
        return decoded_data
    
    @staticmethod
    def decode_bitstream(bitstream: ByteString) -> List[List[int]]:
        """
        解码码流
        :param bitstream: 文件码流
        :return: 图像数据
        """
        offset = 0
        data_blocks = []
        while offset < len(bitstream):
            # 读取编码数据的长度
            encoded_length = struct.unpack_from('I', bitstream, offset)[0]
            offset += BYTE_LENGTH
            
            # 读取编码数据
            encoded_data = bitstream[offset:offset + encoded_length]
            encoded_data = encoded_data.decode('utf-8')
            offset += encoded_length

            # 读取霍夫曼树的长度
            huffman_tree_length = struct.unpack_from('I', bitstream, offset)[0]
            offset += BYTE_LENGTH
            
            # 读取霍夫曼树
            serialized_tree = []
            for _ in range(huffman_tree_length):
                symbol = struct.unpack_from('i', bitstream, offset)[0]
                offset += BYTE_LENGTH

                code_length = struct.unpack_from('I', bitstream, offset)[0]
                offset += BYTE_LENGTH

                code = bitstream[offset:offset + code_length]
                code = code.decode('utf-8')
                offset += code_length
                
                serialized_tree.append((symbol, code))
            
            huffman_tree = JP2KDecoder.deserialize_huffman_tree(serialized_tree)
            decoded_data = JP2KDecoder.huffman_decoding(encoded_data, huffman_tree)

            # 将解码数据添加到块列表
            data_blocks.append(decoded_data)
        
        return data_blocks
    
    @staticmethod
    def inverse_quantize(quantized_coeffs: Tuple, q_factor: int) -> Tuple:
        """
        反量化小波系数
        :param quantized_coeffs: 量化后的系数
        :param q_factor: 量化因子
        :return: 反量化后的系数
        """
        cA, (cH, cV, cD) = quantized_coeffs
        cA = cA * q_factor
        cH = cH * q_factor
        cV = cV * q_factor
        cD = cD * q_factor
        return cA, (cH, cV, cD)
    
    @staticmethod
    def inverse_quantize_from_block(block: List[int], tile_size: int) -> Tuple:
        """
        将混合的数据拆分开
        :param block: 混合的图块数据
        :param tile_size: 编码时的图块大小
        :return: 
        """
        half_size = int(tile_size / 2)
        fre_size = half_size**2
        cA = np.array(block[:fre_size]).reshape((half_size, half_size))
        cH = np.array(block[fre_size: fre_size*2]).reshape((half_size, half_size))
        cV = np.array(block[fre_size*2: fre_size*3]).reshape((half_size, half_size))
        cD = np.array(block[fre_size*3:]).reshape((half_size, half_size))
        return cA, (cH, cV, cD)
    
    @staticmethod
    def inverse_discrete_wavelet_transform(coeffs: Tuple) -> Tuple:
        """
        逆离散小波变换
        :param coeffs: 小波变换系数
        :return: 重建的图像块
        """
        return pywt.idwt2(coeffs, 'haar')
    
    @staticmethod
    def get_tiles_from_data(data_blocks: List[List[int]], tile_size: int=128, q_factor: int=5) -> List[np.ndarray]:
        """
        从数据块还原图像块
        :param blocks: 解码后的图像块
        :param tile_size: 分块大小
        :return: 原始的图像块列表
        """
        reconstruct_tiles = []
        channels = []
        for block in data_blocks:
            # 数据拆分
            origin_coeffs = JP2KDecoder.inverse_quantize_from_block(block, tile_size)
            # 反量化
            coeffs = JP2KDecoder.inverse_quantize(origin_coeffs, q_factor)
            # 反小波变换
            single_channel = JP2KDecoder.inverse_discrete_wavelet_transform(coeffs)
            # 组合 通道数据块 形成 3通道的图块
            channels.append(single_channel)
            if len(channels) == 3:
                reconstruct_tiles.append(np.stack(channels, axis=2))
                channels.clear()
        return reconstruct_tiles
    
    @staticmethod
    def convertColor2RGB(image: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(image, cv2.COLOR_YUV2RGB)
    
    @staticmethod
    def merge_image(tiles: List[np.ndarray], tile_size: int, image_shape: Union[List,Tuple]):
        """
        将图像块重新组合并显示
        :param tiles: 图像块列表
        :param tile_size: 块大小(w, h)，整数或元组
        :param image_shape: 原始图像的形状(w, h)
        """
        w, h = image_shape

        if isinstance(tile_size, int):
            tile_size = utils.turn2pair(tile_size)

        tile_h, tile_w = tile_size
        # 创建一个空白图像用于展示块
        merged_image = np.zeros((h, w, 3), dtype=np.uint8)
        
        # 重新组合图像块
        idx = 0
        for x in range(0, w, tile_w):
            for y in range(0, h, tile_h):
                merged_image[y:y+tile_h, x:x+tile_w] = tiles[idx]
                idx += 1
        return merged_image
