from PyQt5.QtWidgets import QLCDNumber, QApplication
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QIcon
import sys


class Clock(QLCDNumber):
    def __init__(self):
        super().__init__()

        title = "Digital Clock"
        top = 500
        left = 500
        width = 600
        height = 500

        icon = "clock.png"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.setSegmentStyle(QLCDNumber.Filled)
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)

        self.showtime()

    def showtime(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm")
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


app = QApplication(sys.argv)
clock = Clock()
clock.show()
app.exec()
