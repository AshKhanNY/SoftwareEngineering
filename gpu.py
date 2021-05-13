# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Store


class Ui_gpuMenu(object):
    def setupUi(self, gpuMenu):
        #gpuMenu.setObjectName("gpuMenu")
        self.PageName = "gpuMenu"
        gpuMenu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(gpuMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.c = QtWidgets.QVBoxLayout(self.centralwidget)
        self.c.setContentsMargins(0, 0, 0, 0)
        self.c.setSpacing(0)
        self.c.setObjectName("c")
        self.topWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topWidget.sizePolicy().hasHeightForWidth())
        self.topWidget.setSizePolicy(sizePolicy)
        self.topWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.topWidget.setMaximumSize(QtCore.QSize(1677215, 125))
        self.topWidget.setObjectName("topWidget")
        self.topLayout = QtWidgets.QVBoxLayout(self.topWidget)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setSpacing(0)
        self.topLayout.setObjectName("topLayout")
        self.bannerFrame = QtWidgets.QFrame(self.topWidget)
        self.bannerFrame.setStyleSheet("")
        self.bannerFrame.setObjectName("bannerFrame")
        self.BannerLayout = QtWidgets.QHBoxLayout(self.bannerFrame)
        self.BannerLayout.setContentsMargins(0, 0, 0, 0)
        self.BannerLayout.setSpacing(0)
        self.BannerLayout.setObjectName("BannerLayout")
        self.banner = QtWidgets.QLabel(self.bannerFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.banner.sizePolicy().hasHeightForWidth())
        self.banner.setSizePolicy(sizePolicy)
        self.banner.setMaximumSize(QtCore.QSize(16777215, 100))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("banner.jpg"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.BannerLayout.addWidget(self.banner)
        self.topLayout.addWidget(self.bannerFrame)
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
        self.homeBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.homeBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.homeBtn.setIconSize(QtCore.QSize(32, 32))
        self.homeBtn.setFlat(True)
        self.homeBtn.setObjectName("homeBtn")
        self.buttonLayout.addWidget(self.homeBtn)
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
        self.cpuBtn = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpuBtn.sizePolicy().hasHeightForWidth())
        self.cpuBtn.setSizePolicy(sizePolicy)
        self.cpuBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.cpuBtn.setStyleSheet("background-color:#00283a;\n"
"border: 1px solid black;\n"
"color: orange;\n"
"")
        self.cpuBtn.setObjectName("cpuBtn")
        self.buttonLayout.addWidget(self.cpuBtn)
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
        self.caseBtn.setFlat(False)
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
        self.topLayout.addWidget(self.horizontalFrame)
        self.c.addWidget(self.topWidget)
        self.contentGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.contentGroupBox.setStyleSheet("background-color: white;")
        self.contentGroupBox.setObjectName("contentGroupBox")
        self.contentLayout = QtWidgets.QHBoxLayout(self.contentGroupBox)
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout.setSpacing(0)
        self.contentLayout.setObjectName("contentLayout")
        self.leftWidget = QtWidgets.QWidget(self.contentGroupBox)
        self.leftWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.leftWidget.setStyleSheet("")
        self.leftWidget.setObjectName("leftWidget")
        self.leftLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(0)
        self.leftLayout.setObjectName("leftLayout")
        self.contentLayout.addWidget(self.leftWidget)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.contentGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy)
        self.verticalGroupBox.setStyleSheet("")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalGroupLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalGroupLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalGroupLayout.setSpacing(0)
        self.verticalGroupLayout.setObjectName("verticalGroupLayout")
        #Store Edit
        self.Store = Store.Store("GPU")
        self.verticalGroupLayout.addWidget(self.Store)
        
        self.contentLayout.addWidget(self.verticalGroupBox)
        self.rightWidget = QtWidgets.QWidget(self.contentGroupBox)
        self.rightWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.rightWidget.setStyleSheet("")
        self.rightWidget.setObjectName("rightWidget")
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setSpacing(6)
        self.rightLayout.setObjectName("rightLayout")
        self.contentLayout.addWidget(self.rightWidget)
        self.c.addWidget(self.contentGroupBox)
        gpuMenu.setCentralWidget(self.centralwidget)

        #self.retranslateUi(gpuMenu)
        QtCore.QMetaObject.connectSlotsByName(gpuMenu)

    def retranslateUi(self, gpuMenu):
        _translate = QtCore.QCoreApplication.translate
        gpuMenu.setWindowTitle(_translate("gpuMenu", "Parts Authority - GPU"))
        self.homeBtn.setText(_translate("gpuMenu", "Home"))
        self.preBtn.setText(_translate("gpuMenu", "Account"))
        self.cpuBtn.setText(_translate("gpuMenu", "CPU"))
        self.memBtn.setText(_translate("gpuMenu", "Memory"))
        self.moboBtn.setText(_translate("gpuMenu", "Motherboards"))
        self.caseBtn.setText(_translate("gpuMenu", "Cases"))
        self.miscBtn.setText(_translate("gpuMenu", "Miscellaneous"))
        self.forumsBtn.setText(_translate("gpuMenu", "Forums"))

    def setStack(self, stack):
        self.stack = stack
        self.Store.setStack(self.stack)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gpuMenu = QtWidgets.QMainWindow()
    ui = Ui_gpuMenu()
    ui.setupUi(gpuMenu)
    gpuMenu.show()
    sys.exit(app.exec_())
