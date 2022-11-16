import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import  *

from mainWindow import MainWindow

if __name__ =="__main__":
    app = QApplication(sys.argv)
    mwind = MainWindow()
    mwind.show()
    sys.exit(app.exec_())