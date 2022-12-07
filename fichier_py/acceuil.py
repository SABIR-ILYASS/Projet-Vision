from PySide2.QtGui import *
from PySide2.QtWidgets import  *
from PySide2.QtCore import  *
from pageVideo import PageVideo
class Acceuil():
    def __init__(self,parent):
        parent.wind.deleteLater()
        parent.wind = QWidget(parent)
        parent.wind.setFixedSize(parent.size())
        parent.wind.setStyleSheet("background-color:white")
        self.w = parent.width()
        self.h = parent.height()
        self.labelLogo = QLabel(parent.wind)
        logo = QPixmap("../Maquette/logoAceuil.png")
        self.labelLogo.setPixmap(logo)
        self.label = QLabel("Please download your video here, so we can analyze it for you and give you the key informations",parent.wind)
        self.btn = QPushButton("Import Video",parent.wind)
        def goPageVideo(event):
            self.videoPath = QFileDialog.getOpenFileName(parent.wind,"Select Video File")[0]
            print(self.videoPath)
            PageVideo(parent,self.videoPath)
        self.btn.mousePressEvent = goPageVideo
        self.DefinirStyle()
        self.DefinirSize()
        self.DefinirPlacement()
        parent.wind.show()
    def DefinirStyle(self):
        self.btn.setStyleSheet("background-color:rgb(215,150,190)")
    def DefinirSize(self):
        self.labelLogo.setFixedSize(self.w/2,self.h/6)
        self.label.setFixedSize(self.w/2,self.h/10)
        self.btn.setFixedSize(self.w/8,self.h/8)
    def DefinirPlacement(self):
        self.labelLogo.move(self.w/3,self.h/6)
        self.label.move(self.w/3.5,self.h/6+self.labelLogo.height() +self.h/15)
        self.btn.move(self.w/2.2,self.h/6+self.labelLogo.height() +self.h/15 +self.label.height() + self.h / 8)