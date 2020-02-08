# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgEditStatus.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgEditStatus(object):
    def setupUi(self, DlgEditStatus):
        DlgEditStatus.setObjectName("DlgEditStatus")
        DlgEditStatus.setWindowModality(QtCore.Qt.WindowModal)
        DlgEditStatus.resize(606, 265)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgEditStatus)
        self.buttonBox.setGeometry(QtCore.QRect(390, 110, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(DlgEditStatus)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 351, 151))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(DlgEditStatus)
        self.buttonBox.accepted.connect(DlgEditStatus.accept)
        self.buttonBox.rejected.connect(DlgEditStatus.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgEditStatus)

    def retranslateUi(self, DlgEditStatus):
        _translate = QtCore.QCoreApplication.translate
        DlgEditStatus.setWindowTitle(_translate("DlgEditStatus", "Dialog"))

