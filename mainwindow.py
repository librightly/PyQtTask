# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1016, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Option = QtWidgets.QMenu(self.menubar)
        self.menu_Option.setObjectName("menu_Option")
        self.menu_Show = QtWidgets.QMenu(self.menubar)
        self.menu_Show.setObjectName("menu_Show")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewTask = QtWidgets.QAction(MainWindow)
        self.actionNewTask.setObjectName("actionNewTask")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSetupDefaultFile = QtWidgets.QAction(MainWindow)
        self.actionSetupDefaultFile.setObjectName("actionSetupDefaultFile")
        self.actionShowTask = QtWidgets.QAction(MainWindow)
        self.actionShowTask.setObjectName("actionShowTask")
        self.actionShowAllWorkFlow = QtWidgets.QAction(MainWindow)
        self.actionShowAllWorkFlow.setObjectName("actionShowAllWorkFlow")
        self.actionShowAllMainstone = QtWidgets.QAction(MainWindow)
        self.actionShowAllMainstone.setObjectName("actionShowAllMainstone")
        self.actionShowAllDataReleasePlan = QtWidgets.QAction(MainWindow)
        self.actionShowAllDataReleasePlan.setObjectName("actionShowAllDataReleasePlan")
        self.actionShowAllWorkFlowOpened = QtWidgets.QAction(MainWindow)
        self.actionShowAllWorkFlowOpened.setObjectName("actionShowAllWorkFlowOpened")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionShowAllSEProblem = QtWidgets.QAction(MainWindow)
        self.actionShowAllSEProblem.setObjectName("actionShowAllSEProblem")
        self.actionShowAllSEProblemOpened = QtWidgets.QAction(MainWindow)
        self.actionShowAllSEProblemOpened.setObjectName("actionShowAllSEProblemOpened")
        self.actionImportSEPPTs = QtWidgets.QAction(MainWindow)
        self.actionImportSEPPTs.setObjectName("actionImportSEPPTs")
        self.actionExportSEtoExcel = QtWidgets.QAction(MainWindow)
        self.actionExportSEtoExcel.setObjectName("actionExportSEtoExcel")
        self.menu_File.addAction(self.actionNewTask)
        self.menu_File.addAction(self.actionImportSEPPTs)
        self.menu_File.addAction(self.actionExportSEtoExcel)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menu_Option.addAction(self.actionSetupDefaultFile)
        self.menu_Show.addAction(self.actionRefresh)
        self.menu_Show.addSeparator()
        self.menu_Show.addAction(self.actionShowTask)
        self.menu_Show.addSeparator()
        self.menu_Show.addAction(self.actionShowAllWorkFlow)
        self.menu_Show.addAction(self.actionShowAllWorkFlowOpened)
        self.menu_Show.addSeparator()
        self.menu_Show.addAction(self.actionShowAllMainstone)
        self.menu_Show.addSeparator()
        self.menu_Show.addAction(self.actionShowAllDataReleasePlan)
        self.menu_Show.addSeparator()
        self.menu_Show.addAction(self.actionShowAllSEProblem)
        self.menu_Show.addAction(self.actionShowAllSEProblemOpened)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Show.menuAction())
        self.menubar.addAction(self.menu_Option.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQtTask"))
        self.tableWidget.setSortingEnabled(True)
        self.menu_File.setTitle(_translate("MainWindow", "文件"))
        self.menu_Option.setTitle(_translate("MainWindow", "选项"))
        self.menu_Show.setTitle(_translate("MainWindow", "显示"))
        self.actionNewTask.setText(_translate("MainWindow", "NewTask"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSetupDefaultFile.setText(_translate("MainWindow", "SetupDefaultFile"))
        self.actionShowTask.setText(_translate("MainWindow", "ShowTask"))
        self.actionShowAllWorkFlow.setText(_translate("MainWindow", "ShowAllWorkFlow"))
        self.actionShowAllMainstone.setText(_translate("MainWindow", "ShowAllMainstone"))
        self.actionShowAllDataReleasePlan.setText(_translate("MainWindow", "ShowAllDataReleasePlan"))
        self.actionShowAllWorkFlowOpened.setText(_translate("MainWindow", "ShowAllWorkFlowOpened"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionShowAllSEProblem.setText(_translate("MainWindow", "ShowAllSEProblem"))
        self.actionShowAllSEProblemOpened.setText(_translate("MainWindow", "ShowAllSEProblemOpened"))
        self.actionImportSEPPTs.setText(_translate("MainWindow", "ImportSEPPTs"))
        self.actionExportSEtoExcel.setText(_translate("MainWindow", "ExportSEtoExcel"))
