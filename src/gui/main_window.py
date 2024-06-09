from pathlib import Path

import cv2
from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.gen.ui_mainwindow import Ui_MainWindow
from src.core import JP2KDecoder, JP2KEncoder
from src.config_ import SRC_IMG_ROOT, ENCODED_IMG_ROOT, DECODED_IMG_ROOT


class MainWindow(QtWidgets.QMainWindow):
    """主窗口类"""
    # 自定义信号
    origin_file_selected = QtCore.Signal()  # 选择源图结束
    encode_finished = QtCore.Signal()  # 编码结束
    decode_finished = QtCore.Signal()  # 解码结束

    tile_size_changed = QtCore.Signal(int)  # tile_size 被修改
    q_factor_changed = QtCore.Signal(float)  # q_factor 被修改
    image_shape_changed = QtCore.Signal(int, int)   # image_shape 被修改

    def __init__(self):
        super().__init__()
        # 设置UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化
        self.class_init()
        self.ui_init()
        self.signal_slot_init()

    """初始化"""

    def class_init(self):
        """类初始化"""
        # parameter
        self.q_factor = 5.0
        self.q_factor_range = [0, 1000]
        self.tile_size = 128
        self.tile_size_range = [8, 256]
        self.image_shape = [768, 512]
        # file
        self.origin_img_path = None
        self.origin_img = None
        self.encoded_img_path = None
        self.encoded_img = None
        self.decoded_img_path = None
        self.decoded_img = None
        # encoder & decoder
        self.encoder = JP2KEncoder(self.q_factor, self.tile_size)
        self.decoder = JP2KDecoder(self.q_factor, self.tile_size)

    def ui_init(self):
        """UI初始化"""
        # tile_size
        # LineEdit
        int_validator = QtGui.QRegularExpressionValidator(self)
        int_validator.setRegularExpression(
            QtCore.QRegularExpression('[0-9]+$'))
        self.ui.tileSizeLineEdit.setValidator(int_validator)
        self.ui.tileSizeLineEdit.setText(str(self.tile_size))
        # Slider
        self.ui.tileSizeHorizontalSlider.setRange(
            self.tile_size_range[0], self.tile_size_range[1])
        self.ui.tileSizeHorizontalSlider.setValue(int(self.tile_size))
        # MaxLineEdit
        self.ui.tileSizeMaxLineEdit.setValidator(int_validator)
        self.ui.tileSizeMaxLineEdit.setText(str(self.tile_size_range[1]))
        # MinLineEdit
        self.ui.tileSizeMinLineEdit.setValidator(int_validator)
        self.ui.tileSizeMinLineEdit.setText(str(self.tile_size_range[0]))
        # q_factor
        # LineEdit
        float_validator = QtGui.QRegularExpressionValidator(self)
        float_validator.setRegularExpression(
            QtCore.QRegularExpression('[0-9\.]+$'))
        self.ui.qFactorLineEdit.setValidator(float_validator)
        self.ui.qFactorLineEdit.setText(str(self.q_factor))
        # Slider
        self.ui.qFactorHorizontalSlider.setRange(
            self.q_factor_range[0], self.q_factor_range[1])
        self.ui.qFactorHorizontalSlider.setValue(int(self.q_factor))
        # MaxLineEdit
        self.ui.qFactorMaxLineEdit.setValidator(float_validator)
        self.ui.qFactorMaxLineEdit.setText(str(self.q_factor_range[1]))
        # MinLineEdit
        self.ui.qFactorMinLineEdit.setValidator(float_validator)
        self.ui.qFactorMinLineEdit.setText(str(self.q_factor_range[0]))
        # image_shape
        # width
        self.ui.widthLineEdit.setDisabled(True)
        # height
        self.ui.heightLineEdit.setDisabled(True)

    def signal_slot_init(self):
        """信号与槽初始化"""
        self.origin_file_selected.connect(self.origin_file_selected_triggered)
        self.encode_finished.connect(self.encode_finished_triggered)
        self.decode_finished.connect(self.decode_finished_triggered)

        self.tile_size_changed.connect(self.modify_tile_size)
        self.q_factor_changed.connect(self.modify_q_factor)
        self.image_shape_changed.connect(self.modify_image_shape)

    """槽函数部分"""
    # 文件设置
    # # 选择文件
    @QtCore.Slot()
    def on_selectOriginFileButton_clicked(self):
        """选择要打开的源文件"""
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                            caption="选择源文件",
                                                            dir=str(
                                                                SRC_IMG_ROOT),
                                                            filter="图片文件(*.jpg *.gif *.png)",
                                                            options=QtWidgets.QFileDialog.ReadOnly)
        origin_path = Path(filename).absolute()
        self.origin_img_path = origin_path
        self.ui.originFileLineEdit.setText(self.origin_img_path.name)

        self.encoded_img_path = ENCODED_IMG_ROOT / \
            f"encoded_{origin_path.stem}.jp2"
        self.ui.encodedLineEdit.setText(self.encoded_img_path.name)

        self.decoded_img_path = DECODED_IMG_ROOT / \
            f"decoded_{origin_path.stem}.png"
        self.ui.decodedLineEdit.setText(self.decoded_img_path.name)

        self.origin_file_selected.emit()  # 发送信号，显示源图像

    # # 设置编码文件名
    @QtCore.Slot()
    def on_decodedLineEdit_textEdited(self):
        decoded_filename = self.ui.decodedLineEdit.text()
        self.decoded_img_path = Path(decoded_filename)
        # DEBUG_PRINT: 打印调试
        print(f"{self.decoded_img_path=}")

    # # 设置解码文件名
    def on_encodedLineEdit_textEdited(self):
        encoded_filename = self.ui.encodedLineEdit.text()
        self.encoded_img_path = Path(encoded_filename)
        # DEBUG_PRINT: 打印调试
        print(f"{self.encoded_img_path=}")

    # # 开始编码按钮
    @QtCore.Slot()
    def on_encodeButton_clicked(self):
        """解码"""
        self.origin_img = self.encoder.read(self.origin_img_path)
        bitstream = self.encoder.encode(self.origin_img)
        self.encoder.save(self.encoded_img_path, bitstream)
        self.encode_finished.emit()  # 发送信号，显示小波图像

    # # 开始解码按钮
    @QtCore.Slot()
    def on_decodeButton_clicked(self):
        """解码"""
        bitstream = self.decoder.read(self.encoded_img_path)
        self.encoded_img = self.decoder.decode(bitstream)
        self.decoder.save(str(self.decoded_img_path), self.encoded_img)
        self.decode_finished.emit()  # 发送信号，显示解码图像

    # 压缩设置
    # # 分块大小
    @QtCore.Slot()
    def on_tileSizeLineEdit_textEdited(self):
        text = self.ui.tileSizeLineEdit.text()
        if text == '':
            text = self.ui.tileSizeHorizontalSlider.minimum()
        tile_size = int(text)
        self.tile_size_changed.emit(tile_size)  # 发送信号，修改tile_size
        self.ui.tileSizeHorizontalSlider.setValue(tile_size)  # 同步设置 Slider

    @QtCore.Slot()
    def on_tileSizeHorizontalSlider_valueChanged(self):
        value = self.ui.tileSizeHorizontalSlider.value()
        self.tile_size_changed.emit(value)   # 发送信号，修改tile_size
        self.ui.tileSizeLineEdit.setText(str(value))  # 同步设置 LineEdit

    @QtCore.Slot()
    def on_tileSizeMaxLineEdit_editingFinished(self):
        current_value = self.ui.tileSizeHorizontalSlider.value()
        text = self.ui.tileSizeMaxLineEdit.text()
        if text == '':
            text = self.tile_size_range[1]
        self.ui.tileSizeHorizontalSlider.setMaximum(int(text))
        self.ui.tileSizeHorizontalSlider.setValue(current_value)

    @QtCore.Slot()
    def on_tileSizeMinLineEdit_editingFinished(self):
        current_value = self.ui.tileSizeHorizontalSlider.value()
        text = self.ui.tileSizeMinLineEdit.text()
        if text == '':
            text = self.tile_size_range[0]
        self.ui.tileSizeHorizontalSlider.setMinimum(int(text))
        self.ui.tileSizeHorizontalSlider.setValue(current_value)

    # # 量化系数
    @QtCore.Slot()
    def on_qFactorLineEdit_textEdited(self):
        text = self.ui.qFactorLineEdit.text()
        if text == '':
            text = self.ui.qFactorHorizontalSlider.minimum()
        q_factor = float(text)
        self.q_factor_changed.emit(q_factor)    # 发送信号，修改q_factor
        self.ui.qFactorHorizontalSlider.setValue(q_factor)  # 同步设置 Slide

    @QtCore.Slot()
    def on_qFactorHorizontalSlider_valueChanged(self):
        value = self.ui.qFactorHorizontalSlider.value()
        self.q_factor_changed.emit(float(value))    # 发送信号，修改q_factor
        self.ui.qFactorLineEdit.setText(str(value))  # 同步设置 LineEdit

    @QtCore.Slot()
    def on_qFactorMaxLineEdit_editingFinished(self):
        current_value = self.ui.qFactorHorizontalSlider.value()
        text = self.ui.qFactorMaxLineEdit.text()
        if text == '':
            text = self.q_factor_range[1]
        self.ui.qFactorHorizontalSlider.setMaximum(int(text))
        self.ui.qFactorHorizontalSlider.setValue(current_value)

    @QtCore.Slot()
    def on_qFactorMinLineEdit_editingFinished(self):
        current_value = self.ui.qFactorHorizontalSlider.value()
        text = self.ui.qFactorMinLineEdit.text()
        if text == '':
            text = self.q_factor_range[0]
        self.ui.qFactorHorizontalSlider.setMinimum(int(text))
        self.ui.qFactorHorizontalSlider.setValue(current_value)

    # # 图片尺寸
    # HINT: 似乎不需要以下两个槽函数，因为不允许用户编辑以下两个LineEdit
    @QtCore.Slot()
    def on_widthLineEdit_textEdited(self):
        text = self.ui.widthLineEdit.text()
        if text == '':
            text = 0
        width = int(text)
        height = self.image_shape[1]
        self.image_shape_changed.emit(width, height)

    @QtCore.Slot()
    def on_heightLineEdit_textEdited(self):
        text = self.ui.heightLineEdit.text()
        if text == '':
            text = 0
        width = self.image_shape[0]
        height = int(text)
        self.image_shape_changed.emit(width, height)

    # 图像展示
    # # 原始图像
    @QtCore.Slot()
    def origin_file_selected_triggered(self):
        """显示原始图像"""
        # TODO：
        # [ ]: 图像缩放显示
        # Pixmap 打开图像
        q_img = QtGui.QPixmap(str(self.origin_img_path))
        q_rect = self.ui.originGraphicsView.geometry()
        q_img.scaled(q_rect.size())
        if q_img is None:
            QtWidgets.QMessageBox.warning(self, "警告", "图片读取失败，请检查图片路径！")
            return
        width = q_img.width()
        height = q_img.height()
        # 修改显示信息
        self.ui.widthLineEdit.setText(str(width))
        self.ui.heightLineEdit.setText(str(height))
        self.image_shape_changed.emit(width, height)  # 发送信号，修改 image_shape
        # scene 装载图像
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(q_img)
        # view 显示 scene
        self.ui.originGraphicsView.setScene(scene)
        self.ui.originGraphicsView.show()

    # # 解压图像
    @QtCore.Slot()
    def decode_finished_triggered(self):
        # TODO: 
        # [ ]: Check一下tile_size能不能整除，不行的话要报错
        # [ ]: 解压结束之后需要通知栏
        # Pixmap 打开图像
        q_img = QtGui.QPixmap(str(self.decoded_img_path))
        q_rect = self.ui.decodedGraphicsView.geometry()
        q_img.scaled(q_rect.size())
        if q_img is None:
            QtWidgets.QMessageBox.warning(self, "警告", "图片读取失败，请检查图片路径！")
            return
        # scene 装载图像
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(q_img)
        # view 显示 scene
        self.ui.decodedGraphicsView.setScene(scene)
        self.ui.decodedGraphicsView.show()

    # # 小波图像
    @QtCore.Slot()
    def encode_finished_triggered(self):
        # TODO: 
        # [ ]: 编码结束之后需要通知栏
        pass

    # # 图表表示

    # 其他槽函数
    # # 修改 tile_size
    @QtCore.Slot(int)
    def modify_tile_size(self, tile_size):
        self.tile_size = tile_size
        self.encoder.tile_size = tile_size
        self.decoder.tile_size = tile_size

    # # 修改 q_factor
    @QtCore.Slot(float)
    def modify_q_factor(self, q_factor):
        self.q_factor = q_factor
        self.encoder.q_factor = q_factor
        self.decoder.q_factor = q_factor

    # # 修改 image_shape
    @QtCore.Slot(int, int)
    def modify_image_shape(self, width, height):
        self.iamge_shape = [width, height]
        # self.encoder.image_shape = [height, width]
        # self.decoder.image_shape = [height, width]
        self.encoder.image_shape = [width, height]
        self.decoder.image_shape = [width, height]
