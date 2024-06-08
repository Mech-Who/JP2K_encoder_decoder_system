# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 600)
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.settingTab = QTabWidget(self.CentralWidget)
        self.settingTab.setObjectName(u"settingTab")
        self.settingTab.setGeometry(QRect(10, 10, 221, 531))
        self.otherTab = QWidget()
        self.otherTab.setObjectName(u"otherTab")
        self.gridLayoutWidget_4 = QWidget(self.otherTab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 201, 139))
        self.fileLayout = QGridLayout(self.gridLayoutWidget_4)
        self.fileLayout.setObjectName(u"fileLayout")
        self.fileLayout.setContentsMargins(0, 0, 0, 0)
        self.decodedFileLabel = QLabel(self.gridLayoutWidget_4)
        self.decodedFileLabel.setObjectName(u"decodedFileLabel")

        self.fileLayout.addWidget(self.decodedFileLabel, 4, 0, 1, 1)

        self.originFileLabel = QLabel(self.gridLayoutWidget_4)
        self.originFileLabel.setObjectName(u"originFileLabel")

        self.fileLayout.addWidget(self.originFileLabel, 0, 0, 1, 1)

        self.decodedLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.decodedLineEdit.setObjectName(u"decodedLineEdit")

        self.fileLayout.addWidget(self.decodedLineEdit, 5, 0, 1, 2)

        self.encodedLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.encodedLineEdit.setObjectName(u"encodedLineEdit")

        self.fileLayout.addWidget(self.encodedLineEdit, 3, 0, 1, 2)

        self.encodedFileLabel = QLabel(self.gridLayoutWidget_4)
        self.encodedFileLabel.setObjectName(u"encodedFileLabel")

        self.fileLayout.addWidget(self.encodedFileLabel, 2, 0, 1, 1)

        self.selectOriginFileButton = QPushButton(self.gridLayoutWidget_4)
        self.selectOriginFileButton.setObjectName(u"selectOriginFileButton")

        self.fileLayout.addWidget(self.selectOriginFileButton, 0, 1, 1, 1)

        self.originFileLineEdit = QLineEdit(self.gridLayoutWidget_4)
        self.originFileLineEdit.setObjectName(u"originFileLineEdit")

        self.fileLayout.addWidget(self.originFileLineEdit, 1, 0, 1, 2)

        self.horizontalLayoutWidget = QWidget(self.otherTab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 150, 201, 31))
        self.buttonLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.encodeButton = QPushButton(self.horizontalLayoutWidget)
        self.encodeButton.setObjectName(u"encodeButton")

        self.buttonLayout.addWidget(self.encodeButton)

        self.decodeButton = QPushButton(self.horizontalLayoutWidget)
        self.decodeButton.setObjectName(u"decodeButton")

        self.buttonLayout.addWidget(self.decodeButton)

        icon = QIcon()
        iconThemeName = u"tool"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.settingTab.addTab(self.otherTab, icon, "")
        self.baseTab = QWidget()
        self.baseTab.setObjectName(u"baseTab")
        self.gridLayoutWidget = QWidget(self.baseTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 190, 201, 81))
        self.imageSizeLayout = QGridLayout(self.gridLayoutWidget)
        self.imageSizeLayout.setObjectName(u"imageSizeLayout")
        self.imageSizeLayout.setContentsMargins(0, 0, 0, 0)
        self.heightLineEdit = QLineEdit(self.gridLayoutWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")

        self.imageSizeLayout.addWidget(self.heightLineEdit, 2, 1, 1, 1)

        self.widthLabel = QLabel(self.gridLayoutWidget)
        self.widthLabel.setObjectName(u"widthLabel")

        self.imageSizeLayout.addWidget(self.widthLabel, 1, 0, 1, 1)

        self.widthLineEdit = QLineEdit(self.gridLayoutWidget)
        self.widthLineEdit.setObjectName(u"widthLineEdit")

        self.imageSizeLayout.addWidget(self.widthLineEdit, 1, 1, 1, 1)

        self.heightLabel = QLabel(self.gridLayoutWidget)
        self.heightLabel.setObjectName(u"heightLabel")

        self.imageSizeLayout.addWidget(self.heightLabel, 2, 0, 1, 1)

        self.imageSizeLabel = QLabel(self.gridLayoutWidget)
        self.imageSizeLabel.setObjectName(u"imageSizeLabel")

        self.imageSizeLayout.addWidget(self.imageSizeLabel, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.baseTab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 100, 201, 86))
        self.qFactorLayout = QGridLayout(self.gridLayoutWidget_2)
        self.qFactorLayout.setObjectName(u"qFactorLayout")
        self.qFactorLayout.setContentsMargins(0, 0, 0, 0)
        self.qFactorMaxLabel = QLabel(self.gridLayoutWidget_2)
        self.qFactorMaxLabel.setObjectName(u"qFactorMaxLabel")

        self.qFactorLayout.addWidget(self.qFactorMaxLabel, 2, 2, 1, 1)

        self.qFactorMinLabel = QLabel(self.gridLayoutWidget_2)
        self.qFactorMinLabel.setObjectName(u"qFactorMinLabel")

        self.qFactorLayout.addWidget(self.qFactorMinLabel, 2, 0, 1, 1)

        self.qFactorMinLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.qFactorMinLineEdit.setObjectName(u"qFactorMinLineEdit")

        self.qFactorLayout.addWidget(self.qFactorMinLineEdit, 2, 1, 1, 1)

        self.qFactorMaxLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.qFactorMaxLineEdit.setObjectName(u"qFactorMaxLineEdit")

        self.qFactorLayout.addWidget(self.qFactorMaxLineEdit, 2, 3, 1, 1)

        self.qFactorLineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.qFactorLineEdit.setObjectName(u"qFactorLineEdit")

        self.qFactorLayout.addWidget(self.qFactorLineEdit, 0, 2, 1, 2)

        self.qFactorHorizontalSlider = QSlider(self.gridLayoutWidget_2)
        self.qFactorHorizontalSlider.setObjectName(u"qFactorHorizontalSlider")
        self.qFactorHorizontalSlider.setOrientation(Qt.Horizontal)
        self.qFactorHorizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.qFactorHorizontalSlider.setTickInterval(1000)

        self.qFactorLayout.addWidget(self.qFactorHorizontalSlider, 1, 0, 1, 4)

        self.qFactorLabel = QLabel(self.gridLayoutWidget_2)
        self.qFactorLabel.setObjectName(u"qFactorLabel")

        self.qFactorLayout.addWidget(self.qFactorLabel, 0, 0, 1, 2)

        self.gridLayoutWidget_3 = QWidget(self.baseTab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 201, 86))
        self.tileSizeLayout = QGridLayout(self.gridLayoutWidget_3)
        self.tileSizeLayout.setObjectName(u"tileSizeLayout")
        self.tileSizeLayout.setContentsMargins(0, 0, 0, 0)
        self.tileSizeMaxLineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.tileSizeMaxLineEdit.setObjectName(u"tileSizeMaxLineEdit")

        self.tileSizeLayout.addWidget(self.tileSizeMaxLineEdit, 2, 3, 1, 1)

        self.tileSizeMinLineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.tileSizeMinLineEdit.setObjectName(u"tileSizeMinLineEdit")

        self.tileSizeLayout.addWidget(self.tileSizeMinLineEdit, 2, 1, 1, 1)

        self.tileSizeMaxLabel = QLabel(self.gridLayoutWidget_3)
        self.tileSizeMaxLabel.setObjectName(u"tileSizeMaxLabel")

        self.tileSizeLayout.addWidget(self.tileSizeMaxLabel, 2, 2, 1, 1)

        self.tileSizeMinLabel = QLabel(self.gridLayoutWidget_3)
        self.tileSizeMinLabel.setObjectName(u"tileSizeMinLabel")

        self.tileSizeLayout.addWidget(self.tileSizeMinLabel, 2, 0, 1, 1)

        self.tileSizeHorizontalSlider = QSlider(self.gridLayoutWidget_3)
        self.tileSizeHorizontalSlider.setObjectName(u"tileSizeHorizontalSlider")
        self.tileSizeHorizontalSlider.setOrientation(Qt.Horizontal)
        self.tileSizeHorizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.tileSizeHorizontalSlider.setTickInterval(256)

        self.tileSizeLayout.addWidget(self.tileSizeHorizontalSlider, 1, 0, 1, 4)

        self.tileSizeLabel = QLabel(self.gridLayoutWidget_3)
        self.tileSizeLabel.setObjectName(u"tileSizeLabel")

        self.tileSizeLayout.addWidget(self.tileSizeLabel, 0, 0, 1, 2)

        self.tileSizeLineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.tileSizeLineEdit.setObjectName(u"tileSizeLineEdit")

        self.tileSizeLayout.addWidget(self.tileSizeLineEdit, 0, 2, 1, 2)

        self.settingTab.addTab(self.baseTab, "")
        self.imageTab = QTabWidget(self.CentralWidget)
        self.imageTab.setObjectName(u"imageTab")
        self.imageTab.setGeometry(QRect(240, 10, 551, 531))
        self.originTab = QWidget()
        self.originTab.setObjectName(u"originTab")
        self.originGraphicsView = QGraphicsView(self.originTab)
        self.originGraphicsView.setObjectName(u"originGraphicsView")
        self.originGraphicsView.setGeometry(QRect(10, 10, 531, 491))
        self.imageTab.addTab(self.originTab, "")
        self.encodedTab = QWidget()
        self.encodedTab.setObjectName(u"encodedTab")
        self.encodedGraphicsView = QGraphicsView(self.encodedTab)
        self.encodedGraphicsView.setObjectName(u"encodedGraphicsView")
        self.encodedGraphicsView.setGeometry(QRect(10, 10, 531, 491))
        self.imageTab.addTab(self.encodedTab, "")
        self.decodedTab = QWidget()
        self.decodedTab.setObjectName(u"decodedTab")
        self.decodedGraphicsView = QGraphicsView(self.decodedTab)
        self.decodedGraphicsView.setObjectName(u"decodedGraphicsView")
        self.decodedGraphicsView.setGeometry(QRect(10, 10, 531, 491))
        self.imageTab.addTab(self.decodedTab, "")
        self.waveletTab = QWidget()
        self.waveletTab.setObjectName(u"waveletTab")
        self.ltGraphicsView = QGraphicsView(self.waveletTab)
        self.ltGraphicsView.setObjectName(u"ltGraphicsView")
        self.ltGraphicsView.setGeometry(QRect(10, 10, 261, 241))
        self.rtGraphicsView = QGraphicsView(self.waveletTab)
        self.rtGraphicsView.setObjectName(u"rtGraphicsView")
        self.rtGraphicsView.setGeometry(QRect(280, 10, 261, 241))
        self.lbGraphicsView = QGraphicsView(self.waveletTab)
        self.lbGraphicsView.setObjectName(u"lbGraphicsView")
        self.lbGraphicsView.setGeometry(QRect(10, 261, 261, 241))
        self.rbGraphicsView = QGraphicsView(self.waveletTab)
        self.rbGraphicsView.setObjectName(u"rbGraphicsView")
        self.rbGraphicsView.setGeometry(QRect(280, 261, 261, 241))
        self.imageTab.addTab(self.waveletTab, "")
        self.graphTab = QWidget()
        self.graphTab.setObjectName(u"graphTab")
        self.graphWebEngineView = QWebEngineView(self.graphTab)
        self.graphWebEngineView.setObjectName(u"graphWebEngineView")
        self.graphWebEngineView.setGeometry(QRect(10, 10, 531, 491))
        self.graphWebEngineView.setUrl(QUrl(u"about:blank"))
        self.imageTab.addTab(self.graphTab, "")
        MainWindow.setCentralWidget(self.CentralWidget)
        self.imageTab.raise_()
        self.settingTab.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.settingTab.setCurrentIndex(1)
        self.imageTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.decodedFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u538b\u6587\u4ef6\u540d\uff1a", None))
        self.originFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u6587\u4ef6\uff1a", None))
        self.encodedFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u538b\u7f29\u6587\u4ef6\u540d\uff1a", None))
        self.selectOriginFileButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6e90\u56fe\u7247", None))
        self.encodeButton.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.decodeButton.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7801", None))
        self.settingTab.setTabText(self.settingTab.indexOf(self.otherTab), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bbe\u7f6e", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\uff08Width\uff09\uff1a", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\uff08Height\uff09\uff1a", None))
        self.imageSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5c3a\u5bf8\uff1a", None))
        self.qFactorMaxLabel.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.qFactorMinLabel.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.qFactorLabel.setText(QCoreApplication.translate("MainWindow", u"\u91cf\u5316\u7cfb\u6570\uff1a", None))
        self.tileSizeMaxLabel.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.tileSizeMinLabel.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.tileSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5757\u5927\u5c0f\uff1a", None))
        self.settingTab.setTabText(self.settingTab.indexOf(self.baseTab), QCoreApplication.translate("MainWindow", u"\u538b\u7f29\u8bbe\u7f6e", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.originTab), QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.encodedTab), QCoreApplication.translate("MainWindow", u"\u538b\u7f29\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.decodedTab), QCoreApplication.translate("MainWindow", u"\u89e3\u538b\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.waveletTab), QCoreApplication.translate("MainWindow", u"\u5c0f\u6ce2\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.graphTab), QCoreApplication.translate("MainWindow", u"\u56fe\u8868\u5c55\u793a", None))
    # retranslateUi

