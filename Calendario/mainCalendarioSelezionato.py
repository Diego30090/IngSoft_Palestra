# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\utente\PycharmProjects\pythonProject\mainCalendarioSelezionato.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 497)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-60, 120, 861, 381))
        self.label_2.setStyleSheet("background: rgb(240,240,240);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-60, 0, 861, 131))
        self.label.setStyleSheet("background: rgb(240,240,240);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tasksListWidget = QtWidgets.QListWidget(Form)
        self.tasksListWidget.setGeometry(QtCore.QRect(510, 130, 211, 211))
        self.tasksListWidget.setStyleSheet("font:16pt")
        self.tasksListWidget.setObjectName("tasksListWidget")
        self.modifyButton = QtWidgets.QPushButton(Form)
        self.modifyButton.setGeometry(QtCore.QRect(510, 360, 101, 41))
        self.modifyButton.setStyleSheet("background-color: rgb(255,255,87)")
        self.modifyButton.setObjectName("modifyButton")
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setGeometry(QtCore.QRect(620, 360, 101, 41))
        self.deleteButton.setStyleSheet("background-color: rgb(255,77,77)")
        self.deleteButton.setObjectName("deleteButton")
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(510, 412, 211, 41))
        self.backButton.setStyleSheet("background-color: rgb(177,177,177)")
        self.backButton.setObjectName("backButton")
        self.labelReceiver = QtWidgets.QLabel(Form)
        self.labelReceiver.setGeometry(QtCore.QRect(70, 130, 401, 321))
        self.labelReceiver.setStyleSheet("background: white")
        self.labelReceiver.setText("")
        self.labelReceiver.setObjectName("labelReceiver")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Calendario Eventi</span></p></body></html>"))
        self.modifyButton.setText(_translate("Form", "MODIFICA"))
        self.deleteButton.setText(_translate("Form", "ELIMINA"))
        self.backButton.setText(_translate("Form", "INDIETRO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
