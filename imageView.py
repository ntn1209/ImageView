import sys
import os
import matplotlib.pyplot as plt
import pandas
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QVBoxLayout,
                             QGridLayout)
from PyQt6.QtCore import Qt



class Window(QWidget):
     def __init__(self):
         super().__init__()






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


