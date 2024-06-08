# 模仿 JPEG2000 编写编解码器

> 参考资料:
>
> - https://github.com/zhangyilang/jpeg2000/blob/master/code/compress.py
> - https://github.com/mengrang/jp2-python/tree/master/tests
> - https://github.com/pydicom/pylibjpeg-openjpeg
> - https://www.cnblogs.com/huty/p/8519045.html
>
> 数据集：
>
> - kodak24：https://r0k.us/graphics/kodak/

### 一、开发环境

运行 ipynb 文件所需的依赖包：

- ipykernel：实现 notebook 方式
- pandas：查看数据对象

核心功能所需安装的依赖包：

- pillow
- numpy
- PyWavelets
- opencv-python

构建 GUI 所需的依赖包：

- pyside6

### 二、主要内容

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

> 参考：https://blog.csdn.net/qq_45062768/article/details/132357617

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

- [x] 流程实现
- [x] 函数封装
- [x] 类封装
- [ ] 用户界面封装
