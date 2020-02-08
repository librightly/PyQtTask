# This Python file uses the following encoding: utf-8
#from PyQt5 import QtWidgets

from Topic import Topic
from LDatetime import LDateTime

class MainMileStoneItem(Topic):
    def __init__(self):
        super().__init__()

        self.date = LDateTime()
