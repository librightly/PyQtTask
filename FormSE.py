# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormSE.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SAIC_MED(object):
    def setupUi(self, SAIC_MED):
        SAIC_MED.setObjectName("SAIC_MED")
        SAIC_MED.resize(728, 467)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SAIC_MED.sizePolicy().hasHeightForWidth())
        SAIC_MED.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(SAIC_MED)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 9, 721, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_SE = QtWidgets.QWidget()
        self.tab_SE.setObjectName("tab_SE")
        self.pushButton_ImportSEProblemSheet = QtWidgets.QPushButton(self.tab_SE)
        self.pushButton_ImportSEProblemSheet.setGeometry(QtCore.QRect(190, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ImportSEProblemSheet.setFont(font)
        self.pushButton_ImportSEProblemSheet.setObjectName("pushButton_ImportSEProblemSheet")
        self.pushButton_ExportOverviewSheet = QtWidgets.QPushButton(self.tab_SE)
        self.pushButton_ExportOverviewSheet.setGeometry(QtCore.QRect(550, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ExportOverviewSheet.setFont(font)
        self.pushButton_ExportOverviewSheet.setObjectName("pushButton_ExportOverviewSheet")
        self.listWidget_listSEPPT = QtWidgets.QListWidget(self.tab_SE)
        self.listWidget_listSEPPT.setGeometry(QtCore.QRect(20, 20, 681, 231))
        self.listWidget_listSEPPT.setObjectName("listWidget_listSEPPT")
        self.pushButton_SelectSEProblemSheet = QtWidgets.QPushButton(self.tab_SE)
        self.pushButton_SelectSEProblemSheet.setGeometry(QtCore.QRect(50, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SelectSEProblemSheet.setFont(font)
        self.pushButton_SelectSEProblemSheet.setObjectName("pushButton_SelectSEProblemSheet")
        self.progressBar_SE = QtWidgets.QProgressBar(self.tab_SE)
        self.progressBar_SE.setGeometry(QtCore.QRect(20, 360, 671, 23))
        self.progressBar_SE.setProperty("value", 24)
        self.progressBar_SE.setTextVisible(False)
        self.progressBar_SE.setObjectName("progressBar_SE")
        self.radioButton_Project = QtWidgets.QRadioButton(self.tab_SE)
        self.radioButton_Project.setGeometry(QtCore.QRect(320, 320, 89, 16))
        self.radioButton_Project.setObjectName("radioButton_Project")
        self.radioButton_Engineer = QtWidgets.QRadioButton(self.tab_SE)
        self.radioButton_Engineer.setGeometry(QtCore.QRect(430, 320, 89, 16))
        self.radioButton_Engineer.setObjectName("radioButton_Engineer")
        self.label = QtWidgets.QLabel(self.tab_SE)
        self.label.setGeometry(QtCore.QRect(80, 280, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_SE)
        self.label_2.setGeometry(QtCore.QRect(220, 280, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_SE)
        self.label_3.setGeometry(QtCore.QRect(380, 280, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_SE)
        self.label_4.setGeometry(QtCore.QRect(570, 280, 54, 12))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_SE, "")
        self.tab_Version = QtWidgets.QWidget()
        self.tab_Version.setObjectName("tab_Version")
        self.label_Version = QtWidgets.QLabel(self.tab_Version)
        self.label_Version.setGeometry(QtCore.QRect(30, 20, 671, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Version.setFont(font)
        self.label_Version.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_Version.setObjectName("label_Version")
        self.listWidget_verLog = QtWidgets.QListWidget(self.tab_Version)
        self.listWidget_verLog.setGeometry(QtCore.QRect(15, 61, 691, 281))
        self.listWidget_verLog.setObjectName("listWidget_verLog")
        self.tabWidget.addTab(self.tab_Version, "")
        SAIC_MED.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SAIC_MED)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 23))
        self.menubar.setObjectName("menubar")
        SAIC_MED.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SAIC_MED)
        self.statusbar.setObjectName("statusbar")
        SAIC_MED.setStatusBar(self.statusbar)

        self.retranslateUi(SAIC_MED)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SAIC_MED)

    def retranslateUi(self, SAIC_MED):
        _translate = QtCore.QCoreApplication.translate
        SAIC_MED.setWindowTitle(_translate("SAIC_MED", "PyQtSE"))
        self.pushButton_ImportSEProblemSheet.setText(_translate("SAIC_MED", "导入问题单"))
        self.pushButton_ExportOverviewSheet.setText(_translate("SAIC_MED", "导出汇总表"))
        self.pushButton_SelectSEProblemSheet.setText(_translate("SAIC_MED", "选择问题单"))
        self.radioButton_Project.setText(_translate("SAIC_MED", "Project"))
        self.radioButton_Engineer.setText(_translate("SAIC_MED", "Engineer"))
        self.label.setText(_translate("SAIC_MED", "第一步"))
        self.label_2.setText(_translate("SAIC_MED", "第二步"))
        self.label_3.setText(_translate("SAIC_MED", "第三步"))
        self.label_4.setText(_translate("SAIC_MED", "第四步"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SE), _translate("SAIC_MED", "SE问题单"))
        self.label_Version.setText(_translate("SAIC_MED", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Version), _translate("SAIC_MED", "版本信息"))

