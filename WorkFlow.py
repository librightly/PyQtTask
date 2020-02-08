# This Python file uses the following encoding: utf-8
#from PyQt5 import QtCore
#from PyQt5 import QtWidgets

from WorkFlowItem import WorkFlowItem

class WorkFlow:
    def __init__(self):

        self.workflowlist = list()  #任务流列表

    #从EXCEL文件中读取项目《业务流》信息
    def read_workflow_from_worksheet(self,ws,pj):
        theRow = 2
        while (ws.cell(row = theRow,column = 3).value != None):
            aWorkFlowItem = WorkFlowItem()
            aWorkFlowItem.phase = ws.cell(row = theRow,column = 1).value
            aWorkFlowItem.index = ws.cell(row = theRow,column = 2).value
            aWorkFlowItem.name = ws.cell(row = theRow,column = 3).value
            aWorkFlowItem.imput = ws.cell(row = theRow,column = 4).value
            aWorkFlowItem.output = ws.cell(row = theRow,column = 5).value
            aWorkFlowItem.responsible = ws.cell(row = theRow,column = 6).value
            aWorkFlowItem.milestone = ws.cell(row = theRow,column = 7).value
            aWorkFlowItem.date_planed = ws.cell(row = theRow,column = 8).value
            aWorkFlowItem.date_closed = ws.cell(row = theRow,column = 9).value
            aWorkFlowItem.status = ws.cell(row = theRow,column = 10).value
            aWorkFlowItem.note = ws.cell(row = theRow,column = 11).value
            aWorkFlowItem.project = pj
            self.workflowlist.append(aWorkFlowItem)
            theRow += 1
