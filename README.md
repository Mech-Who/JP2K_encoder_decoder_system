# 模仿 JPEG2000 编写编解码器

> 参考资料:
>
> - [github: zhangyilang/jpeg2000](https://github.com/zhangyilang/jpeg2000/blob/master/code/compress.py)
> - [github: mengrang/jp2-python](https://github.com/mengrang/jp2-python/tree/master/tests)
> - [github: pydicom/pylibjpeg-openjpeg](https://github.com/pydicom/pylibjpeg-openjpeg)
> - [JPEG 与 JPEG2000](https://www.cnblogs.com/huty/p/8519045.html)
>
> 数据集：
>
> - kodak24：[kodak24 数据集下载地址](https://r0k.us/graphics/kodak/)

## 安装与使用

0. 数据集准备

    请在项目根目录下创建`img`目录，并在其中创建`src_img`、`test_img`、`encoded_img`、`decoded_img`四个目录，将kodok数据集放在`src_img`目录下，最终结构如下所示：

      ```python
      img
      ├─decoded_img
      ├─encoded_img
      ├─src_img
      │  │
      │  └─kodok
      │          kodim01.png
      │          kodim02.png
      │          kodim03.png
      │          ...
      │
      └─test_img
      ```

1. 安装

   - 本项目使用 Python 3.9，推荐使用 Miniconda 或 Anaconda 创建一个虚拟环境：`conda create -n ic python=3.9 -y`
   - 激活虚拟环境：`conda activate ic`
   - 安装本项目所需的依赖包： `pip install -r requirements.txt`

2. 使用

   - 如果需要运行 GUI 软件，请使用：`python main.py`
   - 如果需要查看代码运行案例，请查看 `explain.ipynb` notebook 文件

## 一、开发环境

运行 ipynb 文件所需的依赖包：

- ipykernel：实现 notebook 方式
- pandas：便于查看数据对象

核心功能所需安装的依赖包：

- numpy
- PyWavelets
- pillow
- opencv-python
- bitarray

构建 GUI 所需的依赖包：

- pyside6

评估编解码器性能所需的安装包：

- scikit-image

## 二、主要内容

- 编码过程
  - 色彩空间变换
  - 图像分块
  - 离散小波变换
  - 量化
  - 熵编码
  - 数据组织为二进制码流
  - 码流保存
- 解码过程
  - 码流读取
  - 二进制码流解析
  - 逆熵编码
  - 逆量化
  - 逆离散小波变换
  - 图块合并
  - 色彩空间变换

## 三、GUI 设计

> 参考：[PySide6 基础教程](https://blog.csdn.net/qq_45062768/article/details/132357617)

使用 PySide6 来构建可视化界面。

由于需要可视化界面，因此后续开发将在 Windows 系统上进行。

工具程序所在目录：`<anaconda环境根目录>\Lib\site-packages\PySide6`

UI 内容：

- 设置
  - 文件设置
    - 原图文件
    - 压缩文件
    - 解压文件
  - 压缩设置
    - 量化系数
    - 分块大小
- 可视化展示
  - 图像展示
    - 原图
    - 压缩图像
    - 解压图像
    - 小波图像
  - 图表展示
    - 压缩率比较

常用工具：

- designer.exe：UI 设计，用法 `designer <*.ui>`
- uic.exe：根据 ui 文件生成 py 文件，用法 `uic -g <python|cpp> <*.ui> -o <*.py>`
- rcc.exe：根据资源文件生成 py 文件，用法 `rcc -g <cpp|python|python2> <*.qrc> -o <*.py>`

## 四、工作进度

- [x] 编解码流程实现
- [x] 函数封装
- [x] 类封装
- [x] 用户界面封装
  - [x] 原图像展示
  - [x] 解码图像展示
  - [x] 小波图像展示
  - [x] 小波图像优化
  - [x] 图片文件大小显示
  - [x] 压缩率图表展示
- [x] 编解码器评估代码实现
- [ ]: 编解码过程细化
  - [ ]: 直流平移
  - [ ]: 色彩分量变换
  - [ ]: 使用不同的小波变换
  - [ ]: 使用均匀标量量化
  - [ ]: EBCOT编码
    - [ ]: Tier1 层编码
    - [ ]: Tier2 层编码
