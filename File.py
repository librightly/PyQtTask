# This Python file uses the following encoding: utf-8
#from PyQt5 import QtCore
#from PyQt5 import QtWidgets

class File:
    def __init__(self):

        self.filepath = ""  #文件路径
        self.filename = ""  #文件名

    #初始化文件名和路径
    def initial(self,dic,name):
        self.filename = name
        self.filepath = dic + "\\" + name
