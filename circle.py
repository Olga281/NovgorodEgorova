import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QPainter, QColor
from random import randint
SCREEN_SIZE = [500, 500]

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(10, 10)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_flag(self, qp):
        x = randint(1, 20)
        y = randint(1, 200)
        a = randint(1, 100)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(self.xs(x), self.ys(y), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())