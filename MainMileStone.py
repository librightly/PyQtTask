# This Python file uses the following encoding: utf-8
#from PyQt5 import QtWidgets

from MainMileStoneItem import MainMileStoneItem
from LDatetime import *

from PyQt5.QtWidgets import QMessageBox

class MainMileStone:
    def __init__(self):
        self.G9 = MainMileStoneItem()
        self.G8 = MainMileStoneItem()
        self.G7 = MainMileStoneItem()
        self.G6 = MainMileStoneItem()
        self.G5 = MainMileStoneItem()
        self.G4 = MainMileStoneItem()
        self.G3 = MainMileStoneItem()
        self.G2 = MainMileStoneItem()
        self.G1 = MainMileStoneItem()
        self.G0 = MainMileStoneItem()
        self.project = ""  #所属项目

    def read_mainstone_from_worksheet(self,ws,pj):
        #QMessageBox.information(None,'消息',ws.title,QMessageBox.Yes | QMessageBox.No)
        self.project = pj
        for theRow in range(2,12):
            if(ws.cell(row = theRow,column = 1).value == "G9"):
                self.G9.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G8"):
                self.G8.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G7"):
                self.G7.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G6"):
                self.G6.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G5"):
                self.G5.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G4"):
                self.G4.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G3"):
                self.G3.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G2"):
                self.G2.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G1"):
                self.G1.date = ws.cell(row = theRow,column = 2).value
            elif(ws.cell(row = theRow,column = 1).value == "G0"):
                self.G0.date = ws.cell(row = theRow,column = 2).value
            else:
                QMessageBox.information(None,'消息','读取主进度报错！',QMessageBox.Yes | QMessageBox.No)
            #QMessageBox.information(None,'消息',ws.cell(row = theRow,column = 1).value,QMessageBox.Yes | QMessageBox.No)
        #QMessageBox.information(None,'消息',str(self.G5),QMessageBox.Yes | QMessageBox.No)
