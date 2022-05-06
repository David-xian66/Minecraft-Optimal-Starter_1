from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.r = 20

    def paintEvent(self, event):
        p = QPainter(self)
        p.drawPixmap(QPoint(), self.get_round_pixmap())
        p.drawPixmap(QPoint(self.width() - self.r, 0), self.get_round_pixmap(True, False))
        p.drawPixmap(QPoint(0, self.height() - self.r), self.get_round_pixmap(False, True))
        p.drawPixmap(QPoint(self.width() - self.r, self.height() - self.r), self.get_round_pixmap(True, True))

    def get_round_pixmap(self, hmirror = False, vmirror = False):
        r = self.r
        pix = QPixmap(r, r)
        pix.fill(Qt.transparent)
        path = QPainterPath()
        path.moveTo(r, 0)
        path.arcTo(0, 0, r * 2, r * 2, 90, 90)
        path.lineTo(0, 0)
        path.lineTo(r, 0)
        p = QPainter()
        p.begin(pix)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.fillPath(path, Qt.red)
        p.end()
        img = pix.toImage()
        img = img.mirrored(hmirror, vmirror)
        return QPixmap.fromImage(img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())