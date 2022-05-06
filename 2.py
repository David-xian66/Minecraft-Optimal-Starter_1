import sys
from PyQt5 import QtWidgets,QtGui,uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Fillrect(QWidget):
    def __init__(self):
        super(Fillrect,self).__init__()
        self.setWindowTitle("用画刷填充区域")
        self.resize(900,600)



    def paintEvent(self,event):
        painter=QPainter(self)   #先定义画布
        painter.begin(self)      #初始化画布
        brush=QBrush(Qt.SolidPattern)  #定义实心画刷样式
        painter.setBrush(brush)
        painter.drawRect(10,15,90,60)

        brush = QBrush(Qt.Dense1Pattern)  # 定义实心画刷样式1
        painter.setBrush(brush)
        painter.drawRect(120, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)  # 定义实心画刷样式2
        painter.setBrush(brush)
        painter.drawRect(230, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)  # 定义实心画刷样式3
        painter.setBrush(brush)
        painter.drawRect(340, 15, 90, 60)
        brush = QBrush(Qt.Dense4Pattern)  # 定义实心画刷样式4
        painter.setBrush(brush)
        painter.drawRect(450, 15, 90, 60)
        brush = QBrush(Qt.Dense5Pattern)  # 定义实心画刷样式5
        painter.setBrush(brush)
        painter.drawRect(560, 15, 90, 60)
        brush = QBrush(Qt.Dense6Pattern)  # 定义实心画刷样式6
        painter.setBrush(brush)
        painter.drawRect(670, 15, 90, 60)
        brush = QBrush(Qt.Dense7Pattern)  # 定义实心画刷样式7
        painter.setBrush(brush)
        painter.drawRect(780, 15, 90, 60)
        painter.end()


if __name__=="__main__":
    app=QApplication(sys.argv)
    p=Fillrect()
    p.show()
    sys.exit(app.exec_())