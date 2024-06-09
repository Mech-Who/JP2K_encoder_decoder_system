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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 600)
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.gridLayout = QGridLayout(self.CentralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.settingTab = QTabWidget(self.CentralWidget)
        self.settingTab.setObjectName(u"settingTab")
        self.otherTab = QWidget()
        self.otherTab.setObjectName(u"otherTab")
        self.verticalLayout = QVBoxLayout(self.otherTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileLayout = QGridLayout()
        self.fileLayout.setObjectName(u"fileLayout")
        self.decodedFileLabel = QLabel(self.otherTab)
        self.decodedFileLabel.setObjectName(u"decodedFileLabel")

        self.fileLayout.addWidget(self.decodedFileLabel, 4, 0, 1, 1)

        self.decodedLineEdit = QLineEdit(self.otherTab)
        self.decodedLineEdit.setObjectName(u"decodedLineEdit")

        self.fileLayout.addWidget(self.decodedLineEdit, 5, 0, 1, 2)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.encodeButton = QPushButton(self.otherTab)
        self.encodeButton.setObjectName(u"encodeButton")

        self.buttonLayout.addWidget(self.encodeButton)

        self.decodeButton = QPushButton(self.otherTab)
        self.decodeButton.setObjectName(u"decodeButton")

        self.buttonLayout.addWidget(self.decodeButton)


        self.fileLayout.addLayout(self.buttonLayout, 7, 0, 1, 2)

        self.selectOriginFileButton = QPushButton(self.otherTab)
        self.selectOriginFileButton.setObjectName(u"selectOriginFileButton")

        self.fileLayout.addWidget(self.selectOriginFileButton, 0, 1, 1, 1)

        self.encodedFileLabel = QLabel(self.otherTab)
        self.encodedFileLabel.setObjectName(u"encodedFileLabel")

        self.fileLayout.addWidget(self.encodedFileLabel, 2, 0, 1, 1)

        self.encodedLineEdit = QLineEdit(self.otherTab)
        self.encodedLineEdit.setObjectName(u"encodedLineEdit")

        self.fileLayout.addWidget(self.encodedLineEdit, 3, 0, 1, 2)

        self.originFileLabel = QLabel(self.otherTab)
        self.originFileLabel.setObjectName(u"originFileLabel")

        self.fileLayout.addWidget(self.originFileLabel, 0, 0, 1, 1)

        self.originFileLineEdit = QLineEdit(self.otherTab)
        self.originFileLineEdit.setObjectName(u"originFileLineEdit")

        self.fileLayout.addWidget(self.originFileLineEdit, 1, 0, 1, 2)

        self.grayCheckBox = QCheckBox(self.otherTab)
        self.grayCheckBox.setObjectName(u"grayCheckBox")
        self.grayCheckBox.setEnabled(True)
        self.grayCheckBox.setTabletTracking(False)
        self.grayCheckBox.setChecked(True)

        self.fileLayout.addWidget(self.grayCheckBox, 6, 0, 1, 2)


        self.verticalLayout.addLayout(self.fileLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon = QIcon(QIcon.fromTheme(u"tool"))
        self.settingTab.addTab(self.otherTab, icon, "")
        self.baseTab = QWidget()
        self.baseTab.setObjectName(u"baseTab")
        self.verticalLayout_2 = QVBoxLayout(self.baseTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tileSizeLayout = QGridLayout()
        self.tileSizeLayout.setObjectName(u"tileSizeLayout")
        self.tileSizeMaxLineEdit = QLineEdit(self.baseTab)
        self.tileSizeMaxLineEdit.setObjectName(u"tileSizeMaxLineEdit")

        self.tileSizeLayout.addWidget(self.tileSizeMaxLineEdit, 2, 3, 1, 1)

        self.tileSizeMinLineEdit = QLineEdit(self.baseTab)
        self.tileSizeMinLineEdit.setObjectName(u"tileSizeMinLineEdit")

        self.tileSizeLayout.addWidget(self.tileSizeMinLineEdit, 2, 1, 1, 1)

        self.tileSizeMaxLabel = QLabel(self.baseTab)
        self.tileSizeMaxLabel.setObjectName(u"tileSizeMaxLabel")

        self.tileSizeLayout.addWidget(self.tileSizeMaxLabel, 2, 2, 1, 1)

        self.tileSizeMinLabel = QLabel(self.baseTab)
        self.tileSizeMinLabel.setObjectName(u"tileSizeMinLabel")

        self.tileSizeLayout.addWidget(self.tileSizeMinLabel, 2, 0, 1, 1)

        self.tileSizeHorizontalSlider = QSlider(self.baseTab)
        self.tileSizeHorizontalSlider.setObjectName(u"tileSizeHorizontalSlider")
        self.tileSizeHorizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.tileSizeHorizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.tileSizeHorizontalSlider.setTickInterval(256)

        self.tileSizeLayout.addWidget(self.tileSizeHorizontalSlider, 1, 0, 1, 4)

        self.tileSizeLabel = QLabel(self.baseTab)
        self.tileSizeLabel.setObjectName(u"tileSizeLabel")

        self.tileSizeLayout.addWidget(self.tileSizeLabel, 0, 0, 1, 2)

        self.tileSizeLineEdit = QLineEdit(self.baseTab)
        self.tileSizeLineEdit.setObjectName(u"tileSizeLineEdit")

        self.tileSizeLayout.addWidget(self.tileSizeLineEdit, 0, 2, 1, 2)


        self.verticalLayout_2.addLayout(self.tileSizeLayout)

        self.qFactorLayout = QGridLayout()
        self.qFactorLayout.setObjectName(u"qFactorLayout")
        self.qFactorMaxLabel = QLabel(self.baseTab)
        self.qFactorMaxLabel.setObjectName(u"qFactorMaxLabel")

        self.qFactorLayout.addWidget(self.qFactorMaxLabel, 2, 2, 1, 1)

        self.qFactorMinLabel = QLabel(self.baseTab)
        self.qFactorMinLabel.setObjectName(u"qFactorMinLabel")

        self.qFactorLayout.addWidget(self.qFactorMinLabel, 2, 0, 1, 1)

        self.qFactorMinLineEdit = QLineEdit(self.baseTab)
        self.qFactorMinLineEdit.setObjectName(u"qFactorMinLineEdit")

        self.qFactorLayout.addWidget(self.qFactorMinLineEdit, 2, 1, 1, 1)

        self.qFactorMaxLineEdit = QLineEdit(self.baseTab)
        self.qFactorMaxLineEdit.setObjectName(u"qFactorMaxLineEdit")

        self.qFactorLayout.addWidget(self.qFactorMaxLineEdit, 2, 3, 1, 1)

        self.qFactorLineEdit = QLineEdit(self.baseTab)
        self.qFactorLineEdit.setObjectName(u"qFactorLineEdit")

        self.qFactorLayout.addWidget(self.qFactorLineEdit, 0, 2, 1, 2)

        self.qFactorHorizontalSlider = QSlider(self.baseTab)
        self.qFactorHorizontalSlider.setObjectName(u"qFactorHorizontalSlider")
        self.qFactorHorizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.qFactorHorizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.qFactorHorizontalSlider.setTickInterval(1000)

        self.qFactorLayout.addWidget(self.qFactorHorizontalSlider, 1, 0, 1, 4)

        self.qFactorLabel = QLabel(self.baseTab)
        self.qFactorLabel.setObjectName(u"qFactorLabel")

        self.qFactorLayout.addWidget(self.qFactorLabel, 0, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.qFactorLayout)

        self.imageSizeLayout = QGridLayout()
        self.imageSizeLayout.setObjectName(u"imageSizeLayout")
        self.heightLineEdit = QLineEdit(self.baseTab)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        self.heightLineEdit.setReadOnly(True)

        self.imageSizeLayout.addWidget(self.heightLineEdit, 2, 1, 1, 1)

        self.widthLabel = QLabel(self.baseTab)
        self.widthLabel.setObjectName(u"widthLabel")

        self.imageSizeLayout.addWidget(self.widthLabel, 1, 0, 1, 1)

        self.widthLineEdit = QLineEdit(self.baseTab)
        self.widthLineEdit.setObjectName(u"widthLineEdit")
        self.widthLineEdit.setReadOnly(True)

        self.imageSizeLayout.addWidget(self.widthLineEdit, 1, 1, 1, 1)

        self.heightLabel = QLabel(self.baseTab)
        self.heightLabel.setObjectName(u"heightLabel")

        self.imageSizeLayout.addWidget(self.heightLabel, 2, 0, 1, 1)

        self.imageSizeLabel = QLabel(self.baseTab)
        self.imageSizeLabel.setObjectName(u"imageSizeLabel")

        self.imageSizeLayout.addWidget(self.imageSizeLabel, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.imageSizeLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.settingTab.addTab(self.baseTab, "")

        self.gridLayout.addWidget(self.settingTab, 0, 0, 1, 1)

        self.imageTab = QTabWidget(self.CentralWidget)
        self.imageTab.setObjectName(u"imageTab")
        self.originTab = QWidget()
        self.originTab.setObjectName(u"originTab")
        self.horizontalLayout = QHBoxLayout(self.originTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.originGraphicsView = QGraphicsView(self.originTab)
        self.originGraphicsView.setObjectName(u"originGraphicsView")

        self.horizontalLayout.addWidget(self.originGraphicsView)

        self.imageTab.addTab(self.originTab, "")
        self.waveletTab = QWidget()
        self.waveletTab.setObjectName(u"waveletTab")
        self.gridLayout_2 = QGridLayout(self.waveletTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ltGraphicsView = QGraphicsView(self.waveletTab)
        self.ltGraphicsView.setObjectName(u"ltGraphicsView")

        self.gridLayout_2.addWidget(self.ltGraphicsView, 0, 0, 1, 1)

        self.rtGraphicsView = QGraphicsView(self.waveletTab)
        self.rtGraphicsView.setObjectName(u"rtGraphicsView")

        self.gridLayout_2.addWidget(self.rtGraphicsView, 0, 1, 1, 1)

        self.lbGraphicsView = QGraphicsView(self.waveletTab)
        self.lbGraphicsView.setObjectName(u"lbGraphicsView")

        self.gridLayout_2.addWidget(self.lbGraphicsView, 1, 0, 1, 1)

        self.rbGraphicsView = QGraphicsView(self.waveletTab)
        self.rbGraphicsView.setObjectName(u"rbGraphicsView")

        self.gridLayout_2.addWidget(self.rbGraphicsView, 1, 1, 1, 1)

        self.imageTab.addTab(self.waveletTab, "")
        self.decodedTab = QWidget()
        self.decodedTab.setObjectName(u"decodedTab")
        self.horizontalLayout_3 = QHBoxLayout(self.decodedTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.decodedGraphicsView = QGraphicsView(self.decodedTab)
        self.decodedGraphicsView.setObjectName(u"decodedGraphicsView")

        self.horizontalLayout_3.addWidget(self.decodedGraphicsView)

        self.imageTab.addTab(self.decodedTab, "")
        self.graphTab = QWidget()
        self.graphTab.setObjectName(u"graphTab")
        self.horizontalLayout_4 = QHBoxLayout(self.graphTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.graphWebEngineView = QWebEngineView(self.graphTab)
        self.graphWebEngineView.setObjectName(u"graphWebEngineView")
        self.graphWebEngineView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_4.addWidget(self.graphWebEngineView)

        self.imageTab.addTab(self.graphTab, "")

        self.gridLayout.addWidget(self.imageTab, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.CentralWidget)
        self.imageTab.raise_()
        self.settingTab.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.settingTab.setCurrentIndex(0)
        self.imageTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.decodedFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u538b\u6587\u4ef6\u540d\uff1a", None))
        self.encodeButton.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.decodeButton.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7801", None))
        self.selectOriginFileButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6e90\u56fe\u7247", None))
        self.encodedFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u538b\u7f29\u6587\u4ef6\u540d\uff1a", None))
        self.originFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u6587\u4ef6\uff1a", None))
        self.grayCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u6ce2\u53d8\u6362\u5c55\u793a\u7070\u5ea6\u56fe", None))
        self.settingTab.setTabText(self.settingTab.indexOf(self.otherTab), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bbe\u7f6e", None))
        self.tileSizeMaxLabel.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.tileSizeMinLabel.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.tileSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5757\u5927\u5c0f\uff1a", None))
        self.qFactorMaxLabel.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.qFactorMinLabel.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.qFactorLabel.setText(QCoreApplication.translate("MainWindow", u"\u91cf\u5316\u7cfb\u6570\uff1a", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\uff08Width\uff09\uff1a", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\uff08Height\uff09\uff1a", None))
        self.imageSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5c3a\u5bf8\uff1a", None))
        self.settingTab.setTabText(self.settingTab.indexOf(self.baseTab), QCoreApplication.translate("MainWindow", u"\u538b\u7f29\u8bbe\u7f6e", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.originTab), QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.waveletTab), QCoreApplication.translate("MainWindow", u"\u5c0f\u6ce2\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.decodedTab), QCoreApplication.translate("MainWindow", u"\u89e3\u7801\u56fe\u50cf", None))
        self.imageTab.setTabText(self.imageTab.indexOf(self.graphTab), QCoreApplication.translate("MainWindow", u"\u56fe\u8868\u5c55\u793a", None))
    # retranslateUi

