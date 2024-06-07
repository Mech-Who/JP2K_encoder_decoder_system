import unittest

import numpy as np

from src.core import JP2KEncoder, JP2KDecoder
from src.config_ import SRC_IMG_ROOT, ENCODED_IMG_ROOT, DECODED_IMG_ROOT

class TestEncoder(unittest.TestCase):
    def setUp(self):
        print("="*10, " TestEncoderDecoder Start! ", "="*10)
    
    def tearDown(self):
        print("="*10, " TestEncoderDecoder End! ", "="*10)
    
    def testEncode(self):
        encoder = JP2KEncoder(q_factor=5, tile_size=128)
        img_path = SRC_IMG_ROOT / "kodim01.png"
        img = encoder.read(str(img_path))
        self.assertTrue(isinstance(img, np.ndarray))
        print(f"成功读取图片，图片形状为: {img.shape}!")

        bitstream = encoder.encode(img)
        self.assertTrue(isinstance(bitstream, bytearray))
        print(f"码流类型为bytearray, 长度为 {len(bitstream)}!")

        save_path = ENCODED_IMG_ROOT / "encoded_kodim01.jp2"
        encoder.save(str(save_path), bitstream)
        self.assertTrue(save_path.exists())
        print(f"{save_path} 文件存在!")
        print("编码过程测试成功！")

    def testDecode(self):
        decoder = JP2KDecoder(tile_size=128, q_factor=5, image_shape=(768, 512))
        img_path = ENCODED_IMG_ROOT / "encoded_kodim01.jp2"
        bitstream = decoder.read(str(img_path))
        self.assertNotEqual(bitstream, None)
        print(f"码流非空, 长度为 {len(bitstream)}!")

        img = decoder.decode(bitstream)
        self.assertEqual(img.shape[2], 3)
        print(f"img的形状为 {img.shape}!")

        save_path = DECODED_IMG_ROOT / "decoded_kodim01.png"
        decoder.save(str(save_path), img)
        self.assertTrue(save_path.exists())
        print(f"{save_path} 文件存在!")
        print("解码过程测试成功！")

