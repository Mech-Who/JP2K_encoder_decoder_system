import math
import numpy as np

from PIL import Image
import cv2


def pil2np(pil_image: Image.Image) -> np.ndarray:
    """
    param:
        pil_image: PIL读取的图片
    return:
        OpenCV读取图片的类型
    """
    return np.asarray(pil_image)


def np2pil(cv_image: np.ndarray, color_cvt=cv2.COLOR_BGR2RGB, mode='RGB') -> Image.Image:
    """
    param:
        cv_image: OpenCV读取的图片
        color_cvt: 转换颜色空间到RGB的选项
    return:
        PIL.Image读取的图片格式
    """
    if color_cvt is not None:
        return Image.fromarray(cv2.cvtColor(cv_image, color_cvt), mode=mode)
    else:
        return Image.fromarray(cv_image, mode=mode)


def turn2pair(one) -> tuple:
    return (one, one)


def get_correct_size(size):
    """获得简化值和计量单位"""
    unit = "B"
    current_size = size
    if current_size > 1024:
        current_size /= 1024
        unit = "KB"
    if current_size > 1024:
        current_size /= 1024
        unit = "MB"
    if current_size > 1024:
        current_size /= 1024
        unit = "GB"
    if current_size > 1024:
        current_size /= 1024
        unit = "TB"
    return current_size, unit


def psnr(old: str, new: str):
    """
    计算PSNR
    PSNR: 峰值信噪比
    图像与影像压缩中典型的峰值讯噪比值在 30dB 到 50dB 之间, 愈高愈好。

    PSNR接近 50dB, 代表压缩后的图像仅有些许非常小的误差。
    PSNR大于 30dB, 人眼很难察觉压缩后和原始影像的差异。
    PSNR介于 20dB 到 30dB 之间, 人眼就可以察觉出图像的差异。
    PSNR介于 10dB 到 20dB 之间, 人眼还是可以用肉眼看出这个图像原始的结构, 且直观上会判断两张图像不存在很大的差异。
    PSNR低于 10dB, 人类很难用肉眼去判断两个图像是否为相同, 一个图像是否为另一个图像的压缩结果。
    """
    old = np.array(cv2.imread(old, cv2.IMREAD_GRAYSCALE), dtype='int64')
    new = np.array(cv2.imread(new, cv2.IMREAD_GRAYSCALE), dtype='int64')
    s = 0
    for i in range(len(old)):
        for j in range(len(old[i])):
            s += (old[i][j]-new[i][j])**2
    s /= (len(old)*len(old[0]))
    psnr = 10*math.log((255**2)/s)
    return psnr
