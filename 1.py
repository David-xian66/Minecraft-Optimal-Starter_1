#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5 import QtWidgets,QtGui,uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用画刷填充区域") 
        self.resize(900,600)
        self.initUI()

    def initUI(self):
        self.resize(700, 500)
        #窗口，{长，宽}
        self.show()
 
 
    def paintEvent(self, e):
 
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
 
        
    def drawRectangles(self, qp):
      
        col = QColor(255,255,255)
        col.setNamedColor('#d4d4d4')
        #上面这个是边框颜色
        qp.setPen(col)
        
        qp.setBrush(QColor(51, 102, 255))
        qp.drawRect(-3, -3, 900, 60)

        qp.setBrush(QColor(102,140,255))
        qp.drawRect(0, 56, 100, 60)
        #上面的是显示设置，{到左边边框距离，到上边边框距离，长，宽}
              
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

