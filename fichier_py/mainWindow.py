from PySide2.QtGui import *
from PySide2.QtWidgets import  *
from acceuil import Acceuil



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("H-Detector")
        self.setWindowIcon(QIcon(QPixmap("../Maquette/logo.png")))



        self.barre = QWidget(self)

        self.cadreDynamique = QWidget(self)
        self.cadreDynamique.wind = QWidget(self.cadreDynamique)

        self.DefinirStyle()
        self.DefinirSize()
        self.DefinirPlacement()
        self.goAcceuil()


    def DefinirStyle(self):
        self.setStyleSheet("background-color:transparent")
        self.barre.setStyleSheet("background-color:rgb(215,150,190)")
        self.cadreDynamique.wind.setStyleSheet("background-color:white")
    def DefinirSize(self):
        self.setFixedSize(1200, 550)
        self.barre.setFixedSize(self.width(),self.height()/10)
        self.cadreDynamique.setFixedSize(self.width(), self.height() * 9 / 10)
        self.cadreDynamique.wind.setFixedSize(self.cadreDynamique.size())

    def DefinirPlacement(self):
        self.barre.move(0,0)
        self.cadreDynamique.move(0,self.height()/10)
    def goAcceuil(self):
        Acceuil(self.cadreDynamique)

