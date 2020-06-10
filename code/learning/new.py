from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


# def window():
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QHBoxLayout()
#     l1 = QtWidgets.QLabel(w)

#     # l1.setAlignment(QtCore.Qt.AlignCenter)
#     l1.setText('Hello')
#     l1.setPixmap("clock.png")
#     l1.setWindowTitle('hey')
#     w.show()
#     l1.show()
#     sys.exit(app.exec())


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("First Program")

        wid = QWidget()
        self.setCentralWidget(wid)
        l1 = QLabel()
        l2 = QLabel()
        l3 = QLabel()
        l4 = QLabel()

        l1.setText("Hello World")
        l4.setText("TutorialsPoint")
        l2.setText("welcome to Python GUI Programming")

        l1.setAlignment(Qt.AlignCenter)
        l3.setAlignment(Qt.AlignCenter)
        l4.setAlignment(Qt.AlignRight)
        l3.setPixmap(QPixmap("clock.png"))

        vbox = QVBoxLayout()
        vbox.addWidget(l1)
        vbox.addStretch()
        vbox.addWidget(l2)
        vbox.addStretch()
        vbox.addWidget(l3)
        vbox.addStretch()
        vbox.addWidget(l4)

        wid.setLayout(vbox)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
