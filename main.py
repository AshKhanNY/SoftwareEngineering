import sys
from PyQt5.QtWidgets import *
import case, cpu, forums, gpu, home, mem, misc, mobo, pb

class MyStack(QStackedLayout):
    def __init__(self):
        QStackedLayout.__init__(self)
        self.pages = {}
        self.user = []

    def gotoHomePage(self):
        self.setCurrentWidget(self.pages['HomeWindow'].centralwidget)
        self.pages['HomeWindow'].retranslateUi(mw)

    def gotoCaseMenu(self):
        self.setCurrentWidget(self.pages['caseMenu'].centralwidget)
        self.pages['caseMenu'].retranslateUi(mw)

    def gotoCpuMenu(self):
        self.setCurrentWidget(self.pages['cpuMenu'].centralwidget)
        self.pages['cpuMenu'].retranslateUi(mw)

    def gotoForumsMenu(self):
        self.setCurrentWidget(self.pages['forumsMenu'].centralwidget)
        self.pages['forumsMenu'].retranslateUi(mw)

    def gotoGpuMenu(self):
        self.setCurrentWidget(self.pages['gpuMenu'].centralwidget)
        self.pages['gpuMenu'].retranslateUi(mw)

    def gotoMemMenu(self):
        self.setCurrentWidget(self.pages['memMenu'].centralwidget)
        self.pages['memMenu'].retranslateUi(mw)

    def gotoMiscMenu(self):
        self.setCurrentWidget(self.pages['miscMenu'].centralwidget)
        self.pages['miscMenu'].retranslateUi(mw)

    def gotoMoboMenu(self):
        self.setCurrentWidget(self.pages['moboMenu'].centralwidget)
        self.pages['moboMenu'].retranslateUi(mw)

    def gotoPbMenu(self):
        self.setCurrentWidget(self.pages['pbMenu'].centralwidget)
        self.pages['pbMenu'].retranslateUi(mw)

app = QApplication(sys.argv)
mw = QMainWindow()
w = QWidget(mw)
stack = MyStack()

def addPage(ui):
    ui.setupUi(mw)
    stack.addWidget(ui.centralwidget)
    stack.pages.update({ui.PageName : ui})
    ui.setStack(stack)
    if ui.PageName != "HomeWindow":
        ui.homeBtn.clicked.connect(stack.gotoHomePage)
    if ui.PageName != "caseMenu":
        ui.caseBtn.clicked.connect(stack.gotoCaseMenu)
    if ui.PageName != "cpuMenu":
        ui.cpuBtn.clicked.connect(stack.gotoCpuMenu)
    if ui.PageName != "forumsMenu":
        ui.forumsBtn.clicked.connect(stack.gotoForumsMenu)
    if ui.PageName != "gpuMenu":
        ui.gpuBtn.clicked.connect(stack.gotoGpuMenu)
    if ui.PageName != "memMenu":
        ui.memBtn.clicked.connect(stack.gotoMemMenu)
    if ui.PageName != "miscMenu":
        ui.miscBtn.clicked.connect(stack.gotoMiscMenu)
    if ui.PageName != "moboMenu":
        ui.moboBtn.clicked.connect(stack.gotoMoboMenu)
    if ui.PageName != "pbMenu":
        ui.preBtn.clicked.connect(stack.gotoPbMenu)

addPage(home.Ui_HomeWindow())
addPage(case.Ui_caseMenu())
addPage(cpu.Ui_cpuMenu())
addPage(forums.Ui_forumsMenu())
addPage(gpu.Ui_gpuMenu())
addPage(mem.Ui_memMenu())
addPage(misc.Ui_miscMenu())
addPage(mobo.Ui_moboMenu())
addPage(pb.Ui_pbMenu())


w.setLayout(stack)
mw.setCentralWidget(w)
mw.showMaximized()
mw.show()
sys.exit(app.exec_())
