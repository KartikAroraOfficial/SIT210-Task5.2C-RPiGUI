from gpiozero import LED
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

red = LED(14)
green = LED(15)
blue = LED(18)



#led_controller class starts here
class led_controller(object):
    def red(self):
        self.reset()
        red.on()

    def green(self):
        self.reset()
        green.on()

    def blue(self):
        self.reset()
        blue.on()

    def reset(self):
        red.off()
        green.off()
        blue.off()

# Ui_MainWindow class starts here 
class Ui_MainWindow(object):
    def __init__(self):
        self.controller = led_controller()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red = QtWidgets.QRadioButton(self.centralwidget,
                                          clicked=lambda: self.controller.red()
                                          )
        self.red.setGeometry(QtCore.QRect(200, 110, 113, 28))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        font.setItalic(True)
        self.red.setFont(font)
        self.red.setObjectName("red")
        self.red.setStyleSheet("QRadioButton"
                               "{"
                               "background-color : red"
                               "}"
                               )

        self.green = QtWidgets.QRadioButton(self.centralwidget,
                                            clicked=lambda:
                                                self.controller.green()
                                            )
        self.green.setGeometry(QtCore.QRect(200, 170, 113, 28))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        font.setItalic(True)
        self.green.setFont(font)
        self.green.setObjectName("green")
        self.green.setStyleSheet("QRadioButton"
                                 "{"
                                 "background-color : lightgreen"
                                 "}"
                                 )
        self.blue = QtWidgets.QRadioButton(self.centralwidget,
                                           clicked=lambda:
                                               self.controller.blue()
                                           )
        self.blue.setGeometry(QtCore.QRect(200, 230, 113, 28))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(16)
        font.setItalic(True)
        self.blue.setFont(font)
        self.blue.setObjectName("blue")
        self.blue.setStyleSheet("QRadioButton"
                                "{"
                                "background-color : lightblue"
                                "}"
                                )
        self.exit = QtWidgets.QPushButton(self.centralwidget,
                                          clicked=lambda: self.clean_exit()
                                          )
        self.exit.setGeometry(QtCore.QRect(180, 310, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red.setText(_translate("MainWindow", "Red"))
        self.green.setText(_translate("MainWindow", "Green"))
        self.blue.setText(_translate("MainWindow", "Blue"))
        self.exit.setText(_translate("MainWindow", "Exit"))

    def clean_exit(self):
        self.controller.reset()
        sys.exit()


if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())