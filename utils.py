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
