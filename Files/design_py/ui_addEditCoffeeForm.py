# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 280)
        Dialog.setWindowTitle("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 250, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.sort = QtWidgets.QLineEdit(Dialog)
        self.sort.setGeometry(QtCore.QRect(140, 10, 201, 31))
        self.sort.setObjectName("sort")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 161, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 121, 31))
        self.label_6.setObjectName("label_6")
        self.price = QtWidgets.QDoubleSpinBox(Dialog)
        self.price.setGeometry(QtCore.QRect(140, 170, 201, 31))
        self.price.setMinimum(1.0)
        self.price.setMaximum(10000.0)
        self.price.setObjectName("price")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.label_7.setObjectName("label_7")
        self.smel = QtWidgets.QLineEdit(Dialog)
        self.smel.setGeometry(QtCore.QRect(140, 130, 201, 31))
        self.smel.setObjectName("smel")
        self.stepen = QtWidgets.QLineEdit(Dialog)
        self.stepen.setGeometry(QtCore.QRect(140, 50, 201, 31))
        self.stepen.setObjectName("stepen")
        self.type = QtWidgets.QLineEdit(Dialog)
        self.type.setGeometry(QtCore.QRect(140, 90, 201, 31))
        self.type.setObjectName("type")
        self.massa = QtWidgets.QDoubleSpinBox(Dialog)
        self.massa.setGeometry(QtCore.QRect(140, 210, 201, 31))
        self.massa.setMinimum(1.0)
        self.massa.setMaximum(10000.0)
        self.massa.setObjectName("massa")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.label.setText(_translate("Dialog", "Название сорта"))
        self.label_2.setText(_translate("Dialog", "Степень обжарки"))
        self.label_3.setText(_translate("Dialog", "Вид зерен"))
        self.label_4.setText(_translate("Dialog", "Описание вкуса"))
        self.label_5.setText(_translate("Dialog", "Неверно заполнена форма"))
        self.label_6.setText(_translate("Dialog", "Цена"))
        self.label_7.setText(_translate("Dialog", "Объем упаковки (кг)"))
