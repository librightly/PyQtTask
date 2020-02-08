# This Python file uses the following encoding: utf-8
from Topic import Topic

from LDatetime import LDateTime

class DataReleasePlanItem(Topic):
    def __init__(self):

        self.date_planed = LDateTime()
        self.date_real = LDateTime()
        self.status = ""
        self.note = ""
        self.project = ""
