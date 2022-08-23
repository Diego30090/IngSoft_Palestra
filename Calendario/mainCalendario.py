# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\utente\PycharmProjects\IngSoft_Palestra-main\Calendario\mainCalendario.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 499)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 132, 411, 321))
        self.calendarWidget.setStyleSheet("    color: black;  \n"
"    background-color: light grey;  \n"
"    selection-background-color: rgb(126,126,126); \n"
"    selection-color black; \n"
"    alternate-background-color: rgb(196,196, 196); \n"
"font: 12pt;\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tasksListWidget = QtWidgets.QListWidget(Form)
        self.tasksListWidget.setGeometry(QtCore.QRect(510, 130, 211, 111))
        self.tasksListWidget.setStyleSheet("font:16pt")
        self.tasksListWidget.setObjectName("tasksListWidget")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(510, 250, 211, 81))
        self.addButton.setStyleSheet("background-color: rgb(173,255,147)")
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-50, 0, 861, 131))
        self.label.setStyleSheet("background: rgb(240,240,240);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-30, 150, 861, 381))
        self.label_2.setStyleSheet("background: rgb(240,240,240);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.taskLineEdit = QtWidgets.QLineEdit(Form)
        self.taskLineEdit.setGeometry(QtCore.QRect(580, 340, 141, 20))
        self.taskLineEdit.setStyleSheet("font: 12;")
        self.taskLineEdit.setObjectName("taskLineEdit")
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(230, 100, 121, 23))
        self.saveButton.setObjectName("saveButton")
        self.infoButton = QtWidgets.QPushButton(Form)
        self.infoButton.setGeometry(QtCore.QRect(150, 70, 51, 51))
        self.infoButton.setObjectName("infoButton")
        self.taskLineEdit1 = QtWidgets.QLineEdit(Form)
        self.taskLineEdit1.setGeometry(QtCore.QRect(580, 370, 141, 20))
        self.taskLineEdit1.setStyleSheet("font: 12;")
        self.taskLineEdit1.setObjectName("taskLineEdit1")
        self.taskLineEdit2 = QtWidgets.QLineEdit(Form)
        self.taskLineEdit2.setGeometry(QtCore.QRect(580, 400, 141, 20))
        self.taskLineEdit2.setStyleSheet("font: 12;")
        self.taskLineEdit2.setObjectName("taskLineEdit2")
        self.taskLineEdit3 = QtWidgets.QLineEdit(Form)
        self.taskLineEdit3.setGeometry(QtCore.QRect(580, 430, 141, 20))
        self.taskLineEdit3.setStyleSheet("font: 12;")
        self.taskLineEdit3.setObjectName("taskLineEdit3")
        self.taskLineEdit4 = QtWidgets.QLineEdit(Form)
        self.taskLineEdit4.setGeometry(QtCore.QRect(580, 460, 141, 20))
        self.taskLineEdit4.setStyleSheet("font: 12;")
        self.taskLineEdit4.setObjectName("taskLineEdit4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 340, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(540, 370, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(540, 400, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(520, 430, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(510, 460, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label.raise_()
        self.label_2.raise_()
        self.calendarWidget.raise_()
        self.tasksListWidget.raise_()
        self.addButton.raise_()
        self.taskLineEdit.raise_()
        self.saveButton.raise_()
        self.infoButton.raise_()
        self.taskLineEdit1.raise_()
        self.taskLineEdit2.raise_()
        self.taskLineEdit3.raise_()
        self.taskLineEdit4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addButton.setText(_translate("Form", "Crea Evento"))
        self.label.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Calendario Eventi</span></p></body></html>"))
        self.label_2.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.saveButton.setText(_translate("Form", "SaveChangesTEMP"))
        self.infoButton.setText(_translate("Form", "INFO"))
        self.label_3.setText(_translate("Form", "Nome Evento"))
        self.label_4.setText(_translate("Form", "Luogo"))
        self.label_5.setText(_translate("Form", "Orario"))
        self.label_6.setText(_translate("Form", "Descrizione"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
