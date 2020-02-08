# This Python file uses the following encoding: utf-8

from PyQt5 import QDialog

class DlgEditStatus_C(QDialog,Ui_DlgEditStatus):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
