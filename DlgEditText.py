# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgEditText.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgEditText(object):
    def setupUi(self, DlgEditText):
        DlgEditText.setObjectName("DlgEditText")
        DlgEditText.setWindowModality(QtCore.Qt.WindowModal)
        DlgEditText.resize(641, 129)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgEditText)
        self.buttonBox.setGeometry(QtCore.QRect(20, 40, 591, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(DlgEditText)
        self.textEdit.setGeometry(QtCore.QRect(110, 40, 181, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(DlgEditText)
        self.buttonBox.accepted.connect(DlgEditText.accept)
        self.buttonBox.rejected.connect(DlgEditText.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgEditText)

    def retranslateUi(self, DlgEditText):
        _translate = QtCore.QCoreApplication.translate
        DlgEditText.setWindowTitle(_translate("DlgEditText", "Dialog"))

