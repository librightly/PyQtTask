# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_seoverview.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_SEOverview(object):
    def setupUi(self, Dialog_SEOverview):
        Dialog_SEOverview.setObjectName("Dialog_SEOverview")
        Dialog_SEOverview.setWindowModality(QtCore.Qt.WindowModal)
        Dialog_SEOverview.resize(635, 471)
        self.listWidget = QtWidgets.QListWidget(Dialog_SEOverview)
        self.listWidget.setGeometry(QtCore.QRect(30, 130, 451, 231))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_ImportSEProblemSheet = QtWidgets.QPushButton(Dialog_SEOverview)
        self.pushButton_ImportSEProblemSheet.setGeometry(QtCore.QRect(520, 180, 81, 23))
        self.pushButton_ImportSEProblemSheet.setObjectName("pushButton_ImportSEProblemSheet")
        self.pushButton_SelectSEProblemSheet = QtWidgets.QPushButton(Dialog_SEOverview)
        self.pushButton_SelectSEProblemSheet.setGeometry(QtCore.QRect(520, 140, 81, 23))
        self.pushButton_SelectSEProblemSheet.setObjectName("pushButton_SelectSEProblemSheet")
        self.pushButton_ExportOverviewSheet = QtWidgets.QPushButton(Dialog_SEOverview)
        self.pushButton_ExportOverviewSheet.setGeometry(QtCore.QRect(520, 220, 81, 23))
        self.pushButton_ExportOverviewSheet.setObjectName("pushButton_ExportOverviewSheet")
        self.groupBox = QtWidgets.QGroupBox(Dialog_SEOverview)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 571, 80))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_Project = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Project.setGeometry(QtCore.QRect(40, 40, 89, 16))
        self.radioButton_Project.setObjectName("radioButton_Project")
        self.radioButton_Engineer = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_Engineer.setGeometry(QtCore.QRect(320, 40, 89, 16))
        self.radioButton_Engineer.setObjectName("radioButton_Engineer")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_SEOverview)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 481, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog_SEOverview)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 380, 591, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.progressBar_SE = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_SE.setGeometry(QtCore.QRect(0, 30, 591, 23))
        self.progressBar_SE.setProperty("value", 24)
        self.progressBar_SE.setObjectName("progressBar_SE")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_SEOverview)
        self.buttonBox.setGeometry(QtCore.QRect(520, 300, 75, 52))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog_SEOverview)
        self.buttonBox.accepted.connect(Dialog_SEOverview.accept)
        self.buttonBox.rejected.connect(Dialog_SEOverview.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_SEOverview)

    def retranslateUi(self, Dialog_SEOverview):
        _translate = QtCore.QCoreApplication.translate
        Dialog_SEOverview.setWindowTitle(_translate("Dialog_SEOverview", "Dialog"))
        self.pushButton_ImportSEProblemSheet.setText(_translate("Dialog_SEOverview", "导入问题单"))
        self.pushButton_SelectSEProblemSheet.setText(_translate("Dialog_SEOverview", "选择问题单"))
        self.pushButton_ExportOverviewSheet.setText(_translate("Dialog_SEOverview", "导出汇总表"))
        self.groupBox.setTitle(_translate("Dialog_SEOverview", "汇总表类型"))
        self.radioButton_Project.setText(_translate("Dialog_SEOverview", "Project"))
        self.radioButton_Engineer.setText(_translate("Dialog_SEOverview", "Engineer"))
        self.groupBox_2.setTitle(_translate("Dialog_SEOverview", "SE问题单清单"))
        self.groupBox_3.setTitle(_translate("Dialog_SEOverview", "进度"))

