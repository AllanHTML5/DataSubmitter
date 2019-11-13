#Import Section

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
import sys
import mysql.connector

#Windows Zone
class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-weight:bold;")
        self.setStyleSheet("color:white;")
        self.title = "Data Gather"
        self.top = 0
        self.left = 0
        self.width = 400
        self.height = 200

        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background:black")
    
        vbox = QVBoxLayout()

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Ingrese su nombre")

        self.name.setStyleSheet("background:white")
        self.name.setFont(QtGui.QFont("Sanserif", 15))

        vbox.addWidget(self.name)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Ingrese su Email")

        self.email.setStyleSheet("background:white")
        self.email.setFont(QtGui.QFont("Sanserif", 15))

        vbox.addWidget(self.email)

        self.id = QLineEdit(self)
        self.id.setPlaceholderText("Ingrese su ID")

        self.id.setStyleSheet("background:white")
        self.id.setFont(QtGui.QFont("Sanserif", 15))

        vbox.addWidget(self.id)

        self.edad = QLineEdit(self)
        self.edad.setPlaceholderText("Ingrese su edad")
        self.edad.setStyleSheet("background:white")

        self.edad.setFont(QtGui.QFont("Sanserif", 15))

        vbox.addWidget(self.edad)

        self.button = QPushButton("Submit", self)
        self.button.setStyleSheet("background:green")
        self.button.setFont(QtGui.QFont("Sanserif", 15))

        vbox.addWidget(self.button)

        self.button.clicked.connect(self.InsertData)

        self.setLayout(vbox)

        self.show()

#SQL DATA LOADER SECTION

    def InsertData(self):
        cnx = mysql.connector.connect(user = "SQL", password = "KWUg3ouF4*45", host = "172.245.87.19", database = "usuarios")
        cursor = cnx.cursor()
        #vsql = "INSERT INTO usuarios(nombre, email, id, edad) VALUES(' " +self.name.text()+"','" + self.email.text() + self.id.text() + self.edad.text() + "')"
        vsql = "INSERT INTO usuarios(nombre, edad, email, id) VALUES(' " +self.name.text() + "','" + self.email.text() + "','" + self.edad.text() + "','" + self.id.text() + "')"
        cursor.execute(vsql)
        self.InitWindow()
        self.setStyleSheet("background-color: white;")
        QMessageBox.about(self, "Alert!", "Thanks for your info!")
        self.setStyleSheet("background-color: black;")
        cnx.commit()
        cursor.close()
        cnx.close()

#Start Arguements

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_()) 