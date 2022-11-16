from PySide2.QtGui import *
from PySide2.QtWidgets import  *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("H-Detector")



        self.barre = QWidget(self)
        self.cadreDynamique = QWidget(parent)
        self.DefinirStyle()
        self.DefinirSize()
    def DefinirStyle(self):
        self.setStyleSheet("background-color:transparent")
        self.barre.setStyleSheet("background-color:rgb(215,150,190)")
        self.cadreDynamique.setStyleSheet("backhground-color:transparent")
    def DefinirSize(self):
        self.setFixedSize(1200, 800)
        self.barre.setFixedSize(self.width(),self.height()/5)
        self.cadreDynamique.setFixedSize(self.width(), self.height()*4/ 5)


