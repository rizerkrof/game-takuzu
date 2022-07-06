#!/usr/bin/env python3
import sys

from PyQt5.QtWidgets    import QApplication
from PyQt5.QtCore       import QCoreApplication
from src.GUI.window     import Window

class Application():
    def __init__(self):
        self.appCore = QCoreApplication.instance()
        if self.appCore is None:
            self.appCore = QApplication(sys.argv)

        self.mainWindow = Window()

    def runApp(self):
        self.mainWindow.show()
        self.appCore.exec_()
