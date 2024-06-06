import typing
from PyQt5.QtWidgets import QApplication,QListWidgetItem, QMainWindow,QCheckBox,QComboBox,QPlainTextEdit,QRadioButton,QGroupBox, QLabel, QPushButton, QTextEdit, QWidget, QDialog
from PyQt5 import uic, QtCore, QtGui,QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np
import sys
import serial.tools.list_ports
import serial

class Todo(QMainWindow):
    def __init__(self):
        super(Todo, self).__init__()
        uic.loadUi("main.ui", self)
        
        todos= ("test1", "test2", "test3") 
        
        for todo in todos:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)
        self.toggleall_button.clicked.connect(self.toggle_all)
            
    def toggle_all(self):
        for i in range(self.listWidget.count()):  
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
            else:
                item.setCheckState(QtCore.Qt.Checked)
            
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Todo()
    window.show()
    app.exec_()