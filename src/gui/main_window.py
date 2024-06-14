import sys
from pathlib import Path

import cv2
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui, QtCharts

from src.gui.gen.ui_mainwindow import Ui_MainWindow
from src.core import JP2KDecoder, JP2KEncoder
from src.config_ import SRC_IMG_ROOT, TEST_IMG_ROOT, ENCODED_IMG_ROOT, DECODED_IMG_ROOT
import src.core.utils as utils


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
        self.tile_size = 120
        self.tile_size_range = [8, 256]
        self.image_shape = [768, 512]
        # file
        self.origin_img_path = None
        self.origin_img = None
        self.is_gray_wavelets = True
        self.encoded_img_path = None
        self.encoded_img = None
        self.decoded_img_path = None
        self.decoded_img = None
        # encoder & decoder
        self.encoder = JP2KEncoder(self.q_factor, self.tile_size)
        self.decoder = JP2KDecoder(self.q_factor, self.tile_size)
        # other matric
        self.psnr = None

    def ui_init(self):
        """UI初始化"""
        # grayCheckBox
        self.ui.grayCheckBox.setChecked(self.is_gray_wavelets)
        # tile_size
        # # LineEdit
        int_validator = QtGui.QRegularExpressionValidator(self)
        int_validator.setRegularExpression(
            QtCore.QRegularExpression('[0-9]+$'))
        self.ui.tileSizeLineEdit.setValidator(int_validator)
        self.ui.tileSizeLineEdit.setText(str(self.tile_size))
        # # Slider
        self.ui.tileSizeHorizontalSlider.setRange(
            self.tile_size_range[0], self.tile_size_range[1])
        self.ui.tileSizeHorizontalSlider.setValue(int(self.tile_size))
        # # MaxLineEdit
        self.ui.tileSizeMaxLineEdit.setValidator(int_validator)
        self.ui.tileSizeMaxLineEdit.setText(str(self.tile_size_range[1]))
        # # MinLineEdit
        self.ui.tileSizeMinLineEdit.setValidator(int_validator)
        self.ui.tileSizeMinLineEdit.setText(str(self.tile_size_range[0]))
        # q_factor
        # # LineEdit
        float_validator = QtGui.QRegularExpressionValidator(self)
        float_validator.setRegularExpression(
            QtCore.QRegularExpression('[0-9\.]+$'))
        self.ui.qFactorLineEdit.setValidator(float_validator)
        self.ui.qFactorLineEdit.setText(str(self.q_factor))
        # # Slider
        self.ui.qFactorHorizontalSlider.setRange(
            self.q_factor_range[0], self.q_factor_range[1])
        self.ui.qFactorHorizontalSlider.setValue(int(self.q_factor))
        # # MaxLineEdit
        self.ui.qFactorMaxLineEdit.setValidator(float_validator)
        self.ui.qFactorMaxLineEdit.setText(str(self.q_factor_range[1]))
        # # MinLineEdit
        self.ui.qFactorMinLineEdit.setValidator(float_validator)
        self.ui.qFactorMinLineEdit.setText(str(self.q_factor_range[0]))
        # image_shape
        # # width
        self.ui.widthLineEdit.setDisabled(True)
        # # height
        self.ui.heightLineEdit.setDisabled(True)
        # image show
        self.ui.originGraphicsView
        self.ui.waveGraphicsView
        self.ui.decodedGraphicsView

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
        if not origin_path.exists() or origin_path.is_dir():
            return
        self.origin_img_path = origin_path
        self.ui.originFileLineEdit.setText(self.origin_img_path.name)
        self.set_file_size_label(self.origin_img_path,
                                 self.ui.originSizeNumberLabel)
        img = cv2.imread(str(self.origin_img_path))
        self.origin_img = cv2.imread(self.origin_img_path)
        file_size = sys.getsizeof(img)
        value, unit = utils.get_correct_size(file_size)
        self.ui.dataSizeNumberLabel.setText(f"{value:.2f} {unit}")

        self.encoded_img_path = ENCODED_IMG_ROOT / \
            f"encoded_{origin_path.stem}.myjp"
        self.ui.encodedLineEdit.setText(self.encoded_img_path.name)
        # self.set_file_size_label(
        #     self.encoded_img_path, self.ui.encodedSizeNumberLabel)

        self.decoded_img_path = DECODED_IMG_ROOT / \
            f"decoded_{origin_path.stem}.png"
        self.ui.decodedLineEdit.setText(self.decoded_img_path.name)
        # self.set_file_size_label(
        #     self.decoded_img_path, self.ui.decodedSizeNumberLabel)

        self.origin_file_selected.emit()  # 发送信号，显示源图像

    # # 设置解码文件名
    @QtCore.Slot()
    def on_encodedLineEdit_textEdited(self):
        encoded_filename = self.ui.encodedLineEdit.text()
        self.encoded_img_path = Path(encoded_filename)
        self.set_file_size_label(
            self.encoded_img_path, self.ui.encodedSizeNumberLabel)

    # # 设置编码文件名
    @QtCore.Slot()
    def on_decodedLineEdit_textEdited(self):
        decoded_filename = self.ui.decodedLineEdit.text()
        self.decoded_img_path = Path(decoded_filename)
        self.set_file_size_label(
            self.decoded_img_path, self.ui.decodedSizeNumberLabel)

    # # 小波灰度彩色切换
    @QtCore.Slot()
    def on_grayCheckBox_stateChanged(self):
        if self.ui.grayCheckBox.isChecked():
            self.is_gray_wavelets = True
        else:
            self.is_gray_wavelets = False

    # # 开始编码按钮
    @QtCore.Slot()
    def on_encodeButton_clicked(self):
        """编码"""
        # 读取图像文件
        self.origin_img = self.encoder.read(self.origin_img_path)

        # 异常处理
        height, width = self.origin_img.shape[:2]
        if width % self.tile_size != 0 or height % self.tile_size != 0:
            QtWidgets.QMessageBox.critical(
                self, "错误", f"图像大小为({width}，{height})，分块大小为{self.tile_size}，无法整除，请调整分块大小！")
            return

        # 编码
        bitstream = self.encoder.encode(self.origin_img)
        self.encoder.save(self.encoded_img_path, bitstream)

        # 显示解码图片大小
        self.set_file_size_label(
            self.encoded_img_path, self.ui.encodedSizeNumberLabel)

        self.encode_finished.emit()  # 发送信号，显示小波图像

    # # 开始解码按钮
    @QtCore.Slot()
    def on_decodeButton_clicked(self):
        """解码"""
        # 异常处理
        if not self.encoded_img_path.exists():
            QtWidgets.QMessageBox.critical(
                self, "错误", f"文件{self.encoded_img_path}不存在，请先进行图像编码！")
            return

        # 解码
        bitstream = self.decoder.read(self.encoded_img_path)
        self.encoded_img = self.decoder.decode(bitstream)
        self.decoder.save(str(self.decoded_img_path), self.encoded_img)

        # 显示解码图片大小
        self.set_file_size_label(
            self.decoded_img_path, self.ui.decodedSizeNumberLabel)

        # 计算bpp并显示
        img_pixel = self.origin_img.shape[0] * self.origin_img.shape[1]
        file_size = self.decoded_img_path.stat().st_size
        self.bpp = utils.bpp(img_pixel, file_size)
        self.ui.BPPValueLabel.setText(str(self.bpp))

        # 计算psnr并显示
        self.psnr = utils.psnr(self.origin_img_path, self.decoded_img_path)
        self.ui.PSNRValueLabel.setText(str(self.psnr))

        self.decode_finished.emit()  # 发送信号，显示解码图像

    # # 绘制 PSNR-bpp 图表按钮
    @QtCore.Slot()
    def on_chartButton_clicked(self):
        """绘制 PSNR-bpp 图并展示"""
        # 展示图表
        # # 创建绘图组件
        chart = QtCharts.QChart()
        chart.setTitle("PSNR-bpp")
        chart_view = QtCharts.QChartView(chart, self.ui.graphTab)
        chart_view.setGeometry(
            0, 0, self.ui.graphTab.width(), self.ui.graphTab.height())
        # # 设置数据
        bpp_list, psnr_list = self.calculate_data()
        # bpp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # psnr_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        series = QtCharts.QLineSeries()
        for bpp, psnr in zip(bpp_list, psnr_list):
            series.append(bpp, psnr)
        chart.addSeries(series)
        # # 设置坐标轴
        # # # x 轴
        axis_x = QtCharts.QValueAxis()
        axis_x.setTitleText("Bits Per Pixel (bpp)")
        axis_x.setRange(min(bpp_list)-1, max(bpp_list)+1)
        chart.setAxisX(axis_x, series)
        # # # y 轴
        axis_y = QtCharts.QValueAxis()
        axis_y.setTitleText("PSNR (dB)")
        axis_y.setRange(min(psnr_list)-5, max(psnr_list)+5)
        chart.setAxisY(axis_y, series)
        # 将量化系数设置回原来的
        self.encoder.q_factor = self.q_factor
        self.decoder.q_factor = self.q_factor

    def calculate_data(self):
        bpp_list = []
        psnr_list = []
        for q_factor in range(1, 25):
            # 设置量化系数
            self.encoder.q_factor = q_factor
            self.decoder.q_factor = q_factor
            # 编码保存
            bitstream = self.encoder.encode(self.origin_img)
            encode_path = TEST_IMG_ROOT / f"test_{q_factor}.myjp"
            self.encoder.save(encode_path, bitstream)
            # 计算 bpp
            img_pixel = self.origin_img.shape[0] * self.origin_img.shape[1]
            file_size = encode_path.stat().st_size
            bpp = utils.bpp(img_pixel, file_size)
            # 解码保存
            decoded_img = self.decoder.decode(bitstream)
            decode_path = TEST_IMG_ROOT / f"test_{q_factor}.png"
            self.decoder.save(decode_path, decoded_img)
            # 计算 psnr
            psnr = utils.psnr(self.origin_img_path, decode_path)
            print(f"{q_factor=}, {bpp=}, {psnr=}")
            # 记录结果
            bpp_list.append(bpp)
            psnr_list.append(psnr)
        print(f"{bpp_list=}")
        print(f"{psnr_list=}")
        return bpp_list, psnr_list

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
        # Pixmap 打开图像
        q_img = QtGui.QPixmap(str(self.origin_img_path))
        if q_img is None:
            QtWidgets.QMessageBox.warning(self, "警告", "图片读取失败，请检查图片路径！")
            return
        width = q_img.width()
        height = q_img.height()
        # 修改显示信息
        self.ui.widthLineEdit.setText(str(width))
        self.ui.heightLineEdit.setText(str(height))
        # scene 装载图像
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(q_img)
        # view 显示 scene
        self.ui.originGraphicsView.setScene(scene)
        self.ui.originGraphicsView.fitInView(
            scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.ui.originGraphicsView.show()

        self.image_shape_changed.emit(width, height)  # 发送信号，修改 image_shape

    # # 小波图像
    @QtCore.Slot()
    def encode_finished_triggered(self):
        wave_img = self.encoder.get_wavelet_image(
            cv2.imread(str(self.origin_img_path)))
        options = QtGui.QImage.Format_RGB888

        if self.is_gray_wavelets:
            wave_img = cv2.cvtColor(wave_img, cv2.COLOR_RGB2GRAY)
            options = QtGui.QImage.Format_Grayscale8

        # # 方案一：保存小波图像然后读取显示
        # self.wave_img_path = WAVE_IMG_ROOT / \
        #     f"wave_{self.origin_img_path.stem}.png"
        # self.wavelet_img = wave_img
        # cv2.imwrite(self.wave_img_path, self.wavelet_img)
        # wave_pixmap = QtGui.QPixmap(str(self.wave_img_path))

        # 方案二：直接处理显示，不保存
        wave_img = QtGui.QImage(
            wave_img.data, wave_img.shape[1], wave_img.shape[0], options)
        wave_pixmap = QtGui.QPixmap.fromImage(wave_img)

        # scene 装载图像
        wave_scene = QtWidgets.QGraphicsScene()
        wave_scene.addPixmap(wave_pixmap)
        # view 显示 scene
        self.ui.waveGraphicsView.setScene(wave_scene)
        self.ui.waveGraphicsView.fitInView(
            wave_scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.ui.waveGraphicsView.show()

        # 编码完成，发送通知
        QtWidgets.QMessageBox.information(
            self, "通知", f"编码完成！文件保存在{self.encoded_img_path}!")

    # # 解码图像
    @ QtCore.Slot()
    def decode_finished_triggered(self):
        # Pixmap 打开图像
        q_img = QtGui.QPixmap(str(self.decoded_img_path))
        if q_img is None:
            QtWidgets.QMessageBox.warning(self, "警告", "图片读取失败，请检查图片路径！")
            return
        # scene 装载图像
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(q_img)
        # view 显示 scene
        self.ui.decodedGraphicsView.setScene(scene)
        self.ui.decodedGraphicsView.fitInView(
            scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.ui.decodedGraphicsView.show()
        # 解码完成，发送通知
        QtWidgets.QMessageBox.information(
            self, "通知", f"解码完成！文件保存在{self.decoded_img_path}!")

    # # 图表表示

    # 其他槽函数
    # # 修改 tile_size
    @ QtCore.Slot(int)
    def modify_tile_size(self, tile_size):
        self.tile_size = tile_size
        self.encoder.tile_size = tile_size
        self.decoder.tile_size = tile_size

    # # 修改 q_factor
    @ QtCore.Slot(float)
    def modify_q_factor(self, q_factor):
        self.q_factor = q_factor
        self.encoder.q_factor = q_factor
        self.decoder.q_factor = q_factor

    # # 修改 image_shape
    @ QtCore.Slot(int, int)
    def modify_image_shape(self, width, height):
        self.iamge_shape = [width, height]
        # self.encoder.image_shape = [height, width]
        # self.decoder.image_shape = [height, width]
        self.encoder.image_shape = [width, height]
        self.decoder.image_shape = [width, height]

    def set_file_size_label(self, path: Path, label: QtWidgets.QLabel):
        size = path.stat().st_size
        value, unit = utils.get_correct_size(size)
        label.setText(f"{value:.2f} {unit}")
