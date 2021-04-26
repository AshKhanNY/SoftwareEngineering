# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.setEnabled(True)
        HomeWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setSpacing(0)
        self.centralLayout.setObjectName("centralLayout")
        self.containerLayout = QtWidgets.QGroupBox(self.centralwidget)
        self.containerLayout.setObjectName("containerLayout")
        self.QSplitterLayout = QtWidgets.QVBoxLayout(self.containerLayout)
        self.QSplitterLayout.setContentsMargins(0, 0, 0, 0)
        self.QSplitterLayout.setSpacing(0)
        self.QSplitterLayout.setObjectName("QSplitterLayout")
        self.topWidget = QtWidgets.QWidget(self.containerLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topWidget.sizePolicy().hasHeightForWidth())
        self.topWidget.setSizePolicy(sizePolicy)
        self.topWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.topWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.topWidget.setObjectName("topWidget")
        self.topView = QtWidgets.QVBoxLayout(self.topWidget)
        self.topView.setContentsMargins(0, 0, 0, 0)
        self.topView.setSpacing(0)
        self.topView.setObjectName("topView")
        self.bannerLayout = QtWidgets.QFrame(self.topWidget)
        self.bannerLayout.setStyleSheet("")
        self.bannerLayout.setObjectName("bannerLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bannerLayout)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.banner = QtWidgets.QLabel(self.bannerLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.banner.sizePolicy().hasHeightForWidth())
        self.banner.setSizePolicy(sizePolicy)
        self.banner.setMaximumSize(QtCore.QSize(16777215, 100))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("banner.jpg"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.horizontalLayout_2.addWidget(self.banner)
        self.topView.addWidget(self.bannerLayout)
        self.horizontalFrame = QtWidgets.QFrame(self.topWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.buttonLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.preBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preBtn.sizePolicy().hasHeightForWidth())
        self.preBtn.setSizePolicy(sizePolicy)
        self.preBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.preBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.preBtn.setIconSize(QtCore.QSize(32, 32))
        self.preBtn.setFlat(True)
        self.preBtn.setObjectName("preBtn")
        self.buttonLayout.addWidget(self.preBtn)
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.buttonLayout.addWidget(self.pushButton)
        self.gpuBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpuBtn.sizePolicy().hasHeightForWidth())
        self.gpuBtn.setSizePolicy(sizePolicy)
        self.gpuBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.gpuBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.gpuBtn.setObjectName("gpuBtn")
        self.buttonLayout.addWidget(self.gpuBtn)
        self.memBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memBtn.sizePolicy().hasHeightForWidth())
        self.memBtn.setSizePolicy(sizePolicy)
        self.memBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.memBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.memBtn.setObjectName("memBtn")
        self.buttonLayout.addWidget(self.memBtn)
        self.moboBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moboBtn.sizePolicy().hasHeightForWidth())
        self.moboBtn.setSizePolicy(sizePolicy)
        self.moboBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.moboBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.moboBtn.setIconSize(QtCore.QSize(32, 32))
        self.moboBtn.setFlat(True)
        self.moboBtn.setObjectName("moboBtn")
        self.buttonLayout.addWidget(self.moboBtn)
        self.caseBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caseBtn.sizePolicy().hasHeightForWidth())
        self.caseBtn.setSizePolicy(sizePolicy)
        self.caseBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.caseBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.caseBtn.setIconSize(QtCore.QSize(32, 32))
        self.caseBtn.setFlat(True)
        self.caseBtn.setObjectName("caseBtn")
        self.buttonLayout.addWidget(self.caseBtn)
        self.miscBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.miscBtn.sizePolicy().hasHeightForWidth())
        self.miscBtn.setSizePolicy(sizePolicy)
        self.miscBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.miscBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.miscBtn.setIconSize(QtCore.QSize(32, 32))
        self.miscBtn.setFlat(True)
        self.miscBtn.setObjectName("miscBtn")
        self.buttonLayout.addWidget(self.miscBtn)
        self.forumsBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forumsBtn.sizePolicy().hasHeightForWidth())
        self.forumsBtn.setSizePolicy(sizePolicy)
        self.forumsBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.forumsBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.forumsBtn.setIconSize(QtCore.QSize(32, 32))
        self.forumsBtn.setFlat(True)
        self.forumsBtn.setObjectName("forumsBtn")
        self.buttonLayout.addWidget(self.forumsBtn)
        self.topView.addWidget(self.horizontalFrame)
        self.QSplitterLayout.addWidget(self.topWidget)
        self.bottomWidget = QtWidgets.QWidget(self.containerLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.bottomWidget.setObjectName("bottomWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottomWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftFrame = QtWidgets.QFrame(self.bottomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftFrame.sizePolicy().hasHeightForWidth())
        self.leftFrame.setSizePolicy(sizePolicy)
        self.leftFrame.setMinimumSize(QtCore.QSize(140, 0))
        self.leftFrame.setStyleSheet("background-color: white;")
        self.leftFrame.setObjectName("leftFrame")
        self.leftLayout = QtWidgets.QHBoxLayout(self.leftFrame)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(0)
        self.leftLayout.setObjectName("leftLayout")
        self.horizontalLayout.addWidget(self.leftFrame)
        self.gridFrame = QtWidgets.QFrame(self.bottomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setStyleSheet("border-image: url(fade.jpg) 0 0 0 0 stretch stretch;")
        self.gridFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(50, 20, 40, 20)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(35)
        self.gridLayout.setObjectName("gridLayout")
        self.frameLayout1 = QtWidgets.QFrame(self.gridFrame)
        self.frameLayout1.setStyleSheet("border-image: url(white.jpg);")
        self.frameLayout1.setObjectName("frameLayout1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameLayout1)
        self.verticalLayout_5.setContentsMargins(10, 0, 10, 25)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sgtTitle1 = QtWidgets.QLabel(self.frameLayout1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtTitle1.sizePolicy().hasHeightForWidth())
        self.sgtTitle1.setSizePolicy(sizePolicy)
        self.sgtTitle1.setStyleSheet("color: orange;\n"
"qproperty-alignment: AlignCenter;\n"
"font: bold;")
        self.sgtTitle1.setObjectName("sgtTitle1")
        self.verticalLayout_5.addWidget(self.sgtTitle1)
        self.sgtImg1 = QtWidgets.QLabel(self.frameLayout1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtImg1.sizePolicy().hasHeightForWidth())
        self.sgtImg1.setSizePolicy(sizePolicy)
        self.sgtImg1.setMinimumSize(QtCore.QSize(0, 0))
        self.sgtImg1.setMaximumSize(QtCore.QSize(100, 100))
        self.sgtImg1.setStyleSheet("")
        self.sgtImg1.setText("")
        self.sgtImg1.setPixmap(QtGui.QPixmap("sgtpc1.jpg"))
        self.sgtImg1.setScaledContents(True)
        self.sgtImg1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sgtImg1.setObjectName("sgtImg1")
        self.verticalLayout_5.addWidget(self.sgtImg1, 0, QtCore.Qt.AlignHCenter)
        self.sgtPurchase1 = QtWidgets.QPushButton(self.frameLayout1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtPurchase1.sizePolicy().hasHeightForWidth())
        self.sgtPurchase1.setSizePolicy(sizePolicy)
        self.sgtPurchase1.setMinimumSize(QtCore.QSize(125, 25))
        self.sgtPurchase1.setStyleSheet("border-image: url(:/purchase/purchase.jpg);")
        self.sgtPurchase1.setObjectName("sgtPurchase1")
        self.verticalLayout_5.addWidget(self.sgtPurchase1, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frameLayout1, 1, 2, 1, 1)
        self.frameLayout2 = QtWidgets.QFrame(self.gridFrame)
        self.frameLayout2.setStyleSheet("border-image: url(white.jpg);")
        self.frameLayout2.setObjectName("frameLayout2")
        self.sgtFrame2 = QtWidgets.QVBoxLayout(self.frameLayout2)
        self.sgtFrame2.setContentsMargins(10, 0, 10, 25)
        self.sgtFrame2.setSpacing(0)
        self.sgtFrame2.setObjectName("sgtFrame2")
        self.sgtTitle2 = QtWidgets.QLabel(self.frameLayout2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtTitle2.sizePolicy().hasHeightForWidth())
        self.sgtTitle2.setSizePolicy(sizePolicy)
        self.sgtTitle2.setStyleSheet("color: orange;\n"
"qproperty-alignment: AlignCenter;\n"
"font: bold;")
        self.sgtTitle2.setObjectName("sgtTitle2")
        self.sgtFrame2.addWidget(self.sgtTitle2)
        self.sgtImg2 = QtWidgets.QLabel(self.frameLayout2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtImg2.sizePolicy().hasHeightForWidth())
        self.sgtImg2.setSizePolicy(sizePolicy)
        self.sgtImg2.setMinimumSize(QtCore.QSize(0, 0))
        self.sgtImg2.setMaximumSize(QtCore.QSize(100, 100))
        self.sgtImg2.setStyleSheet("")
        self.sgtImg2.setText("")
        self.sgtImg2.setPixmap(QtGui.QPixmap("sgtpc2.jpg"))
        self.sgtImg2.setScaledContents(True)
        self.sgtImg2.setObjectName("sgtImg2")
        self.sgtFrame2.addWidget(self.sgtImg2, 0, QtCore.Qt.AlignHCenter)
        self.sgtPurchase2 = QtWidgets.QPushButton(self.frameLayout2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtPurchase2.sizePolicy().hasHeightForWidth())
        self.sgtPurchase2.setSizePolicy(sizePolicy)
        self.sgtPurchase2.setMinimumSize(QtCore.QSize(125, 25))
        self.sgtPurchase2.setStyleSheet("border-image: url(:/purchase/purchase.jpg);")
        self.sgtPurchase2.setObjectName("sgtPurchase2")
        self.sgtFrame2.addWidget(self.sgtPurchase2, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frameLayout2, 1, 3, 1, 1)
        self.frameLayout3 = QtWidgets.QFrame(self.gridFrame)
        self.frameLayout3.setStyleSheet("border-image: url(white.jpg);")
        self.frameLayout3.setObjectName("frameLayout3")
        self.sgtFrame_3 = QtWidgets.QVBoxLayout(self.frameLayout3)
        self.sgtFrame_3.setContentsMargins(10, 0, 10, 25)
        self.sgtFrame_3.setSpacing(0)
        self.sgtFrame_3.setObjectName("sgtFrame_3")
        self.sgtTitle3 = QtWidgets.QLabel(self.frameLayout3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtTitle3.sizePolicy().hasHeightForWidth())
        self.sgtTitle3.setSizePolicy(sizePolicy)
        self.sgtTitle3.setStyleSheet("color: orange;\n"
"qproperty-alignment: AlignCenter;\n"
"font: bold;")
        self.sgtTitle3.setObjectName("sgtTitle3")
        self.sgtFrame_3.addWidget(self.sgtTitle3)
        self.sgtImg3 = QtWidgets.QLabel(self.frameLayout3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sgtImg3.sizePolicy().hasHeightForWidth())
        self.sgtImg3.setSizePolicy(sizePolicy)
        self.sgtImg3.setMinimumSize(QtCore.QSize(0, 0))
        self.sgtImg3.setMaximumSize(QtCore.QSize(100, 100))
        self.sgtImg3.setStyleSheet("")
        self.sgtImg3.setText("")
        self.sgtImg3.setPixmap(QtGui.QPixmap("sgtpc3.jpg"))
        self.sgtImg3.setScaledContents(True)
        self.sgtImg3.setObjectName("sgtImg3")
        self.sgtFrame_3.addWidget(self.sgtImg3, 0, QtCore.Qt.AlignHCenter)
        self.sgtPurchase3 = QtWidgets.QPushButton(self.frameLayout3)
        self.sgtPurchase3.setMinimumSize(QtCore.QSize(125, 25))
        self.sgtPurchase3.setStyleSheet("border-image: url(:/purchase/purchase.jpg);")
        self.sgtPurchase3.setObjectName("sgtPurchase3")
        self.sgtFrame_3.addWidget(self.sgtPurchase3, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frameLayout3, 1, 4, 1, 1)
        self.mstPopular1 = QtWidgets.QFrame(self.gridFrame)
        self.mstPopular1.setStyleSheet("border-image: url(white.jpg);")
        self.mstPopular1.setObjectName("mstPopular1")
        self.mstPopular1_1 = QtWidgets.QVBoxLayout(self.mstPopular1)
        self.mstPopular1_1.setContentsMargins(10, 0, 10, 25)
        self.mstPopular1_1.setSpacing(0)
        self.mstPopular1_1.setObjectName("mstPopular1_1")
        self.popularTitle1 = QtWidgets.QLabel(self.mstPopular1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularTitle1.sizePolicy().hasHeightForWidth())
        self.popularTitle1.setSizePolicy(sizePolicy)
        self.popularTitle1.setStyleSheet("color: orange;\n"
"qproperty-alignment: AlignCenter;\n"
"font: bold;")
        self.popularTitle1.setScaledContents(False)
        self.popularTitle1.setObjectName("popularTitle1")
        self.mstPopular1_1.addWidget(self.popularTitle1)
        self.popularImg1 = QtWidgets.QLabel(self.mstPopular1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularImg1.sizePolicy().hasHeightForWidth())
        self.popularImg1.setSizePolicy(sizePolicy)
        self.popularImg1.setMinimumSize(QtCore.QSize(0, 0))
        self.popularImg1.setMaximumSize(QtCore.QSize(100, 100))
        self.popularImg1.setText("")
        self.popularImg1.setPixmap(QtGui.QPixmap("sgtpc1.jpg"))
        self.popularImg1.setScaledContents(True)
        self.popularImg1.setObjectName("popularImg1")
        self.mstPopular1_1.addWidget(self.popularImg1, 0, QtCore.Qt.AlignHCenter)
        self.popularPurchase1 = QtWidgets.QPushButton(self.mstPopular1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularPurchase1.sizePolicy().hasHeightForWidth())
        self.popularPurchase1.setSizePolicy(sizePolicy)
        self.popularPurchase1.setMinimumSize(QtCore.QSize(125, 25))
        self.popularPurchase1.setStyleSheet("border-image: url(:/purchase/purchase.jpg);")
        self.popularPurchase1.setObjectName("popularPurchase1")
        self.mstPopular1_1.addWidget(self.popularPurchase1, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.mstPopular1, 2, 2, 1, 1)
        self.mstPopular2 = QtWidgets.QFrame(self.gridFrame)
        self.mstPopular2.setStyleSheet("border-image: url(white.jpg);")
        self.mstPopular2.setObjectName("mstPopular2")
        self.mstPopular2_2 = QtWidgets.QVBoxLayout(self.mstPopular2)
        self.mstPopular2_2.setContentsMargins(10, 0, 10, 25)
        self.mstPopular2_2.setSpacing(0)
        self.mstPopular2_2.setObjectName("mstPopular2_2")
        self.popularTitle2 = QtWidgets.QLabel(self.mstPopular2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularTitle2.sizePolicy().hasHeightForWidth())
        self.popularTitle2.setSizePolicy(sizePolicy)
        self.popularTitle2.setStyleSheet("border-image: url(white.jpg.JPG);\n"
"color: orange;\n"
"qproperty-alignment: AlignCenter;\n"
"font: bold;")
        self.popularTitle2.setObjectName("popularTitle2")
        self.mstPopular2_2.addWidget(self.popularTitle2)
        self.popularImg2 = QtWidgets.QLabel(self.mstPopular2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularImg2.sizePolicy().hasHeightForWidth())
        self.popularImg2.setSizePolicy(sizePolicy)
        self.popularImg2.setMinimumSize(QtCore.QSize(0, 0))
        self.popularImg2.setMaximumSize(QtCore.QSize(100, 100))
        self.popularImg2.setText("")
        self.popularImg2.setPixmap(QtGui.QPixmap("sgtpc2.jpg"))
        self.popularImg2.setScaledContents(True)
        self.popularImg2.setObjectName("popularImg2")
        self.mstPopular2_2.addWidget(self.popularImg2, 0, QtCore.Qt.AlignHCenter)
        self.popularPurchase2 = QtWidgets.QPushButton(self.mstPopular2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularPurchase2.sizePolicy().hasHeightForWidth())
        self.popularPurchase2.setSizePolicy(sizePolicy)
        self.popularPurchase2.setMinimumSize(QtCore.QSize(125, 25))
        self.popularPurchase2.setStyleSheet("border-image: url(:/purchase/purchase.jpg);")
        self.popularPurchase2.setObjectName("popularPurchase2")
        self.mstPopular2_2.addWidget(self.popularPurchase2, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.mstPopular2, 2, 3, 1, 1)
        self.mstPopular3 = QtWidgets.QFrame(self.gridFrame)
        self.mstPopular3.setStyleSheet("border-image: url(white.jpg);")
        self.mstPopular3.setObjectName("mstPopular3")
        self.mstPopular3_3 = QtWidgets.QVBoxLayout(self.mstPopular3)
        self.mstPopular3_3.setContentsMargins(10, 0, 10, 25)
        self.mstPopular3_3.setSpacing(0)
        self.mstPopular3_3.setObjectName("mstPopular3_3")
        self.popularTitle3 = QtWidgets.QLabel(self.mstPopular3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularTitle3.sizePolicy().hasHeightForWidth())
        self.popularTitle3.setSizePolicy(sizePolicy)
        self.popularTitle3.setStyleSheet("color: orange;\n"
"qproperty-alignment: AlignCenter;\n"
"font: bold;")
        self.popularTitle3.setObjectName("popularTitle3")
        self.mstPopular3_3.addWidget(self.popularTitle3)
        self.popularImg3 = QtWidgets.QLabel(self.mstPopular3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularImg3.sizePolicy().hasHeightForWidth())
        self.popularImg3.setSizePolicy(sizePolicy)
        self.popularImg3.setMinimumSize(QtCore.QSize(0, 0))
        self.popularImg3.setMaximumSize(QtCore.QSize(100, 100))
        self.popularImg3.setText("")
        self.popularImg3.setPixmap(QtGui.QPixmap("sgtpc3.jpg"))
        self.popularImg3.setScaledContents(True)
        self.popularImg3.setObjectName("popularImg3")
        self.mstPopular3_3.addWidget(self.popularImg3, 0, QtCore.Qt.AlignHCenter)
        self.popularPurchase3 = QtWidgets.QPushButton(self.mstPopular3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popularPurchase3.sizePolicy().hasHeightForWidth())
        self.popularPurchase3.setSizePolicy(sizePolicy)
        self.popularPurchase3.setMinimumSize(QtCore.QSize(125, 25))
        self.popularPurchase3.setStyleSheet("border-image: url(:/purchase/purchase.jpg);")
        self.popularPurchase3.setObjectName("popularPurchase3")
        self.mstPopular3_3.addWidget(self.popularPurchase3, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.mstPopular3, 2, 4, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame)
        self.rightFrame = QtWidgets.QFrame(self.bottomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightFrame.sizePolicy().hasHeightForWidth())
        self.rightFrame.setSizePolicy(sizePolicy)
        self.rightFrame.setMinimumSize(QtCore.QSize(140, 0))
        self.rightFrame.setStyleSheet("background-color: white;")
        self.rightFrame.setObjectName("rightFrame")
        self.rightLayout = QtWidgets.QHBoxLayout(self.rightFrame)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setSpacing(0)
        self.rightLayout.setObjectName("rightLayout")
        self.horizontalLayout.addWidget(self.rightFrame)
        self.QSplitterLayout.addWidget(self.bottomWidget)
        self.centralLayout.addWidget(self.containerLayout)
        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Parts Authority"))
        self.preBtn.setText(_translate("HomeWindow", "Pre-Built PCs"))
        self.pushButton.setText(_translate("HomeWindow", "CPU"))
        self.gpuBtn.setText(_translate("HomeWindow", "GPU"))
        self.memBtn.setText(_translate("HomeWindow", "Memory"))
        self.moboBtn.setText(_translate("HomeWindow", "Motherboards"))
        self.caseBtn.setText(_translate("HomeWindow", "Cases"))
        self.miscBtn.setText(_translate("HomeWindow", "Miscellaneous"))
        self.forumsBtn.setText(_translate("HomeWindow", "Forums"))
        self.sgtTitle1.setText(_translate("HomeWindow", " Suggested Computer #1"))
        self.sgtPurchase1.setText(_translate("HomeWindow", "Purchase"))
        self.sgtTitle2.setText(_translate("HomeWindow", "Suggested Computer #2"))
        self.sgtPurchase2.setText(_translate("HomeWindow", "Purchase"))
        self.sgtTitle3.setText(_translate("HomeWindow", "Suggested Computer #3"))
        self.sgtPurchase3.setText(_translate("HomeWindow", "Purchase"))
        self.popularTitle1.setText(_translate("HomeWindow", "Most Popular #1"))
        self.popularPurchase1.setText(_translate("HomeWindow", "Purchase"))
        self.popularTitle2.setText(_translate("HomeWindow", "Most Popular #2"))
        self.popularPurchase2.setText(_translate("HomeWindow", "Purchase"))
        self.popularTitle3.setText(_translate("HomeWindow", "Most Popular #3"))
        self.popularPurchase3.setText(_translate("HomeWindow", "Purchase"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())
