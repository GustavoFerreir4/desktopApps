import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont

app = QtWidgets.QApplication([])

class MainWindow(QtWidgets.QMainWindow):
    username = "undefined"
    userlastname = "undefined"
    usermsg = "undefined"
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message submit")
        self.setFixedSize(600, 300)

        namelabel = QtWidgets.QLabel(self)
        namelabel.setText("Digite seu nome:")
        namelabel.setGeometry(100, 50, 200, 50)
        namelabel.setObjectName("name")

        nameinput = QtWidgets.QLineEdit(self)
        nameinput.setGeometry(250, 65, 210, 20)
        nameinput.setObjectName("nameinput")

        lastnamelabel = QtWidgets.QLabel(self)
        lastnamelabel.setText("Digite seu sobrenome:")
        lastnamelabel.setGeometry(100, 70, 200, 50)
        lastnamelabel.setObjectName("lastname")

        lastnameinput = QtWidgets.QLineEdit(self)
        lastnameinput.setGeometry(250, 85, 210, 20)
        lastnameinput.setObjectName("lastnameinput")


        messagelabel = QtWidgets.QLabel(self)
        messagelabel.setText("Digite uma Mensagem:")
        messagelabel.setGeometry(100, 120, 200, 50)
        messagelabel.setObjectName("message")

        messageInput = QtWidgets.QTextEdit(self)
        messageInput.setGeometry(250, 120, 210, 100)
        messageInput.setObjectName("messageinput")


        button = QtWidgets.QPushButton(self)
        button.setGeometry( 400, 230, 60, 30)
        button.setText("confirmar")
        button.setToolTipDuration(2000)
        button.setToolTip("Click this button and see what it happens")


window = MainWindow()




window.show()

app.exec()


"""
.setToolTipDuration(msec) -> duration of tip msg.
.setToolTip(" ... ") -> text that appears when hovering mouse cursor on the object. 

.setHidden( True or False ) -> hides the object completely.]
 
 

"""