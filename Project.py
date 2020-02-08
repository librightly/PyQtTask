# This Python file uses the following encoding: utf-8
#from PyQt5 import QtCore
#from PyQt5 import QtWidgets

from openpyxl import Workbook
from openpyxl import load_workbook

from Topic import Topic
from File_EXCEL import File_EXCEL
from WorkFlow import WorkFlow
from MainMileStone import MainMileStone
from DataReleasePlan import DataReleasePlan

#from PyQt5.QtWidgets import QMessageBox

class Project(Topic):
    def __init__(self):
        super().__init__()

        #self.workbook = Workbook()  #项目数据EXCEL
        self.projectfile = File_EXCEL()  #项目对应EXCEL表文件
        self.workflow = WorkFlow()  #项目业务流列表
        self.mainmilestone = MainMileStone()  #项目主进度
        self.datareleaseplan =DataReleasePlan()  #项目数据发布计划
        self.percentage = ""  #业务流完成率
        #self.filepath = ""  #项目文件夹路径

    def caculate_percentage(self):
        count = 0
        for wfi in self.workflow.workflowlist:
            if (wfi.status == "NA"):
                count += 1
            elif (wfi.status == "OK"):
                count += 1
        percentage = count / len(self.workflow.workflowlist)
        self.percentage = str(percentage)[0:4]
        #QMessageBox.information(None,'消息',str(self.percentage),QMessageBox.Yes | QMessageBox.No)

    #从EXCEL文件中读取项目信息
    def read_project_EXCEL(self):
        self.projectfile.load_file()

        ws_MainMileStone = self.projectfile.workbook["主进度"]
        self.mainmilestone.read_mainstone_from_worksheet(ws_MainMileStone,self.name)  #从EXCEL中读取项目业务流

        ws_WorkFlow = self.projectfile.workbook["业务流"]
        self.workflow.read_workflow_from_worksheet(ws_WorkFlow,self.name)  #从EXCEL中读取项目业务流

        ws_DataReleasePlan = self.projectfile.workbook["先决条件时间节点"]
        self.datareleaseplan.read_datereleaseplan_from_worksheet(ws_DataReleasePlan,self.name)  #从EXCEL中读取项目业务流
