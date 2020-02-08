# This Python file uses the following encoding: utf-8
#from PyQt5 import QtCore
#from PyQt5 import QtWidgets,QDialog

from PyQt5.QtWidgets import QDialog

from DlgEditText import Ui_DlgEditText

class DlgEditText_C(QDialog,Ui_DlgEditText):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
