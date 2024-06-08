from pathlib import Path

import cv2
from PySide6 import QtCore, QtWidgets, QtGui

from src.gui.gen.ui_mainwindow import Ui_MainWindow
from src.core import JP2KDecoder, JP2KEncoder
from src.config_ import SRC_IMG_ROOT


class MainWindow(QtWidgets.QMainWindow):
    """主窗口类"""
    # 自定义信号
    origin_file_selected = QtCore.Signal()  # 选择源图结束
    encode_finished = QtCore.Signal()  # 编码结束
    decode_finished = QtCore.Signal()  # 解码结束

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
        self.q_factor = 5.0
        self.q_factor_range = [0, 1000]
        self.tile_size = 128
        self.tile_size_range = [8, 256]
        self.image_shape = (768, 512)
        self.origin_img_path = None
        self.origin_img = None
        self.encoded_img_path = None
        self.encoded_img = None
        self.decoded_img_path = None
        self.decoded_img = None
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

    def signal_slot_init(self):
        """信号与槽初始化"""
        # TODO: 绑定选择原文件之后显示原图像
        self.origin_file_selected.connect(self.on_origin_file_selected_clicked)
        # TODO: 绑定编码结束后显示小波图象
        # self.encode_finished.connect()
        # TODO: 绑定解码结束后显示解码图像
        # self.decode_finished.connect()

    """槽函数部分"""
    # 文件设置
    # 选择文件
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

        self.encoded_img_path = origin_path.parent / \
            f"encoded_{origin_path.stem}.jp2"
        self.ui.encodedLineEdit.setText(self.encoded_img_path.name)

        self.decoded_img_path = origin_path.parent / \
            f"decoded_{origin_path.stem}.png"
        self.ui.decodedLineEdit.setText(self.decoded_img_path.name)

        self.origin_file_selected.emit()  # 发送信号，显示源图像

    # 设置编码文件名
    @QtCore.Slot()
    def on_decodedLineEdit_textEdited(self):
        decoded_filename = self.ui.decodedLineEdit.text()
        self.decoded_img_path = Path(decoded_filename)
        # DEBUG_PRINT: 打印调试
        print(f"{self.decoded_img_path=}")

    # 设置解码文件名
    def on_encodedLineEdit_textEdited(self):
        encoded_filename = self.ui.encodedLineEdit.text()
        self.encoded_img_path = Path(encoded_filename)
        # DEBUG_PRINT: 打印调试
        print(f"{self.encoded_img_path=}")

    # 开始编码按钮
    @QtCore.Slot()
    def on_encodeButton_clicked(self):
        """解码"""
        self.origin_img = self.encoder.read(self.origin_img_path)
        bitstream = self.encoder.encode(self.origin_img)
        self.encoder.save(self.encoded_img_path, bitstream)
        self.encode_finished.emit()  # 发送信号，显示小波图像

    @QtCore.Slot()
    def on_decodeButton_clicked(self):
        """解码"""
        bitstream = self.decoder.read(self.encoded_img_path)
        self.encoded_img = self.decoder.decode(bitstream)
        self.decoder.save(self.encoded_img)
        self.decode_finished.emit()  # 发送信号，显示解码图像

    # 开始解码按钮

    # 压缩设置
    # 分块大小
    @QtCore.Slot()
    def on_tileSizeLineEdit_textEdited(self):
        text = self.ui.tileSizeLineEdit.text()
        if text == '':
            text = self.ui.tileSizeHorizontalSlider.minimum()
        tile_size = int(text)
        self.tile_size = tile_size
        self.ui.tileSizeHorizontalSlider.setValue(tile_size)  # 同步设置 Slider

    @QtCore.Slot()
    def on_tileSizeHorizontalSlider_valueChanged(self):
        value = self.ui.tileSizeHorizontalSlider.value()
        self.tile_size = value
        self.ui.tileSizeLineEdit.setText(str(value))  # 同步设置 LineEdit

    @QtCore.Slot()
    def on_tileSizeMaxLineEdit_editingFinished(self):
        text = self.ui.tileSizeMaxLineEdit.text()
        if text == '':
            text = self.tile_size_range[1]
        self.ui.tileSizeHorizontalSlider.setMaximum(int(text))

    @QtCore.Slot()
    def on_tileSizeMinLineEdit_editingFinished(self):
        text = self.ui.tileSizeMinLineEdit.text()
        if text == '':
            text = self.tile_size_range[0]
        self.ui.tileSizeHorizontalSlider.setMinimum(int(text))

    # 量化系数
    @QtCore.Slot()
    def on_qFactorLineEdit_textEdited(self):
        text = self.ui.qFactorLineEdit.text()
        if text == '':
            text = self.ui.qFactorHorizontalSlider.minimum()
        q_factor = float(text)
        self.tile_size = q_factor
        self.ui.qFactorHorizontalSlider.setValue(q_factor)  # 同步设置 Slide

    @QtCore.Slot()
    def on_qFactorHorizontalSlider_valueChanged(self):
        value = self.ui.qFactorHorizontalSlider.value()
        self.tile_size = value
        self.ui.qFactorLineEdit.setText(str(value))  # 同步设置 LineEdit

    @QtCore.Slot()
    def on_qFactorMaxLineEdit_editingFinished(self):
        text = self.ui.qFactorMaxLineEdit.text()
        if text == '':
            text = self.q_factor_range[1]
        self.ui.qFactorHorizontalSlider.setMaximum(int(text))

    @QtCore.Slot()
    def on_qFactorMinLineEdit_editingFinished(self):
        text = self.ui.qFactorMinLineEdit.text()
        if text == '':
            text = self.q_factor_range[0]
        self.ui.qFactorHorizontalSlider.setMinimum(int(text))

    # 图片尺寸 
    # TODO: 展示原图片后设置

    # 图像展示

    # 原始图像
    @QtCore.Slot()
    def on_origin_file_selected_triggered(self):
        src_img = cv2.imread("2.jpg")
        if src_img is None:
            QtWidgets.QMessageBox.information(self, "警告", "图片读取失败，请检查图片路径！")
            return
        show_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
        q_img = QtGui.QImage(
            show_img.data, show_img.wrap_channels, QtGui.QImage.Format_RGB888)
        scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScenet(scene)
        self.ui.graphicsView.show()
        scene.addPixmap(QtGui.QPixmap.fromImage(q_img))

    # 解压图像
    @QtCore.Slot()
    def on_decode_finished_triggered(self):
        pass

    # 小波图像
    @QtCore.Slot()
    def on_encode_finished_triggered(self):
        pass

    # 图表表示
