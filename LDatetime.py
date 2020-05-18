from datetime import datetime,date
from PyQt5.QtWidgets import QMessageBox

class LDateTime:
    def __init__(self):
        self.datetime = datetime.strptime("2000-1-1","%Y-%m-%d")
        self.date_string = None  #日期字符串

    def showDateInTableWidget(self,row,col):
        return self.datetime.date()

    def convertDateToString(self):
        self.date_string = self.datetime.date().isoformat()

    def fromString(self,date_string_in,style = False):
        date_string = date_string_in.strip()
        if (style == True) and (date_string == None):
            QMessageBox.information(None,'消息','日期不能为空!',QMessageBox.Yes | QMessageBox.No)
            return
        elif style == False and (date_string == ""):
            return
        elif date_string.count("-") == 2:
            self.datetime = datetime.strptime(date_string,"%Y-%m-%d")
            self.convertDateToString()
            return
        elif date_string.count("/") == 2:
            self.datetime = datetime.strptime(date_string,"%Y/%m/%d")
            self.convertDateToString()
            return
        elif date_string.count(".") == 2:
            self.datetime = datetime.strptime(date_string,"%Y.%m.%d")
            self.convertDateToString()
            return
        else:
            QMessageBox.about(None,'报错','日期格式不符合要求，请按照“Y-M-D”或“Y/M/D”或“Y.M.D”格式填写!')
            return
