# This Python file uses the following encoding: utf-8
#from PyQt5 import QtCore
#from PyQt5 import QtWidgets

from Topic import Topic
from LDatetime import LDateTime

from enum import Enum

class TaskStatus(Enum):
    notstart = 1  #未开始
    nomal = 2  #正常进行中
    delay_of_risk = 3  #拖期有风险
    delay_of_nonrisk =4  #拖期有风险
    close = 5  #完成

class Task(Topic):
    def __init__(self):
        super().__init__()        
        self.date_created =LDateTime()  #创建时间
        self.date_planed = LDateTime()  #计划完成时间
        #self.date_followed = LDateTime()  #跟踪时间
        self.date_closed = LDateTime()  #关闭时间
        self.status = 0  #状态
        self.note = ""  #备注
