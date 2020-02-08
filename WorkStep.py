# This Python file uses the following encoding: utf-8
from LDatetime import LDateTime

class WorkStep:
    def __init__(self):

        self.detail = ""  #工作内容
        self.date = LDateTime()  #日期
        self.task = ""  #任务
        self.project = ""  #项目
