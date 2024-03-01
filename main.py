import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Fon():
    def __init__(self, file):
        uic.loadUi(file, self)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        super().__init__()
        Fon("UI.ui")
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.width = self.size().width()
        self.height = self.size().height()
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        for el in range(5):
            self.x = random.randint(40, self.width - 40)
            self.y = random.randint(30, self.height - 30)
            self.r = random.randint(10, 40)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            qp.drawEllipse(self.x, self.y,
                           self.r, self.r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

