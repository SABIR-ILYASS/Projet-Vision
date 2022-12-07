from PySide2.QtGui import *
from PySide2.QtWidgets import  *


class PageVideo():
    def __init__(self,parent,path):
        parent.wind.deleteLater()
        parent.wind = QWidget(parent)
        parent.wind.setFixedSize(parent.size())
        parent.wind.setStyleSheet("background-color:white")
        self.w = parent.width()
        self.h = parent.height()
        self.videoLabel = QLabel(parent.wind)
        self.barreInf = QWidget(parent.wind)
        self.hide = QPushButton("Hide",self.barreInf)
        self.process = QPushButton("Process",self.barreInf)
        # temps ecoulé en video jusqu au frame actuel
        self.time = QLabel("<h1>10 : 08</h1>",self.barreInf)
        self.DefinirStyle()
        self.DefinirSize()
        self.DefinirPlacement()
        parent.wind.show()
    def DefinirSize(self):
        self.videoLabel.setFixedSize(self.w *3/4,self.h *6/8)
        self.barreInf.setFixedSize(self.w *3/4,self.h /8)
        self.hide.setFixedSize(self.barreInf.width()/ 8,self.barreInf.height()*3/4)
        self.process.setFixedSize(self.barreInf.width() / 8, self.barreInf.height() * 3 / 4)
        self.time.setFixedSize(self.barreInf.width() / 8, self.barreInf.height() * 3 / 4)
    def DefinirStyle(self):
        self.videoLabel.setStyleSheet("background-color:rgb(215,0,200)")
        self.barreInf.setStyleSheet("background-color:rgb(215,150,190)")
        self.hide.setStyleSheet("background-color:rgb(215,150,190)")
        self.process.setStyleSheet("background-color:rgb(215,150,190)")
        self.time.setStyleSheet("background-color:transparent;color:white;")
    def DefinirPlacement(self):
        self.videoLabel.move(self.w /8,self.h /16)
        self.barreInf.move(self.w /8,self.h*13.5/16)
        self.hide.move(self.barreInf.width() /16, self.barreInf.height() / 8)
        self.process.move(self.barreInf.width() - self.barreInf.width() *3/16, self.barreInf.height() / 8)
        self.time.move(self.barreInf.width() / 2 - self.barreInf.width() /16, self.barreInf.height() / 8)