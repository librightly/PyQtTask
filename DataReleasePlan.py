# This Python file uses the following encoding: utf-8
from DataReleasePlanItem import DataReleasePlanItem

class DataReleasePlan:
    def __init__(self):

        self.datareleaseplan = list()

    def read_datereleaseplan_from_worksheet(self,ws,pj):
        theRow = 2
        while (ws.cell(row = theRow,column = 1).value != None):
            aDataReleasePlanItem = DataReleasePlanItem()
            aDataReleasePlanItem.name = ws.cell(row = theRow,column = 1).value
            aDataReleasePlanItem.date_planed = ws.cell(row = theRow,column = 2).value
            aDataReleasePlanItem.date_real = ws.cell(row = theRow,column = 3).value
            aDataReleasePlanItem.status = ws.cell(row = theRow,column = 4).value
            aDataReleasePlanItem.note = ws.cell(row = theRow,column = 5).value
            aDataReleasePlanItem.project = pj
            self.datareleaseplan.append(aDataReleasePlanItem)
            theRow += 1
