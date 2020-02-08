# This Python file uses the following encoding: utf-8
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QDirModel,QMenu
from PyQt5.QtWidgets import QDialog,QMessageBox,QFileDialog,QInputDialog,QLineEdit
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QHeaderView,QAbstractItemView,QTableView,QTreeWidgetItem
from PyQt5.QtGui import QStandardItemModel

from mainwindow import Ui_MainWindow
#from DlgEditText_C import DlgEditText_C

from TaskEXECL import TaskEXECL
from Project import Project
from Task import Task

from SEProblemSet import SEProblemSet
from SESheetPPT import SESheetPPT
from OverviewSheetEXCEL import OverveiwSheetEXCEL
#from SEProblem import SEProblem
#from WorkFlowItem import WorkFlowItem
#from MainMileStone import MainMileStone

#from LDatetime import LDateTime

class PyQtTask(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)        

        #数据成员
        self.boolStyle = True  #程序类型，True为调试版本，False为发布版本
        self.table_style = 0  #表格视图关联数据类型标识
        self.DefaultDirectory = ""  #默认项目文件路径
        self.TaskList = list()  #普通任务列表
        self.ProjectList = list()  #项目列表
        self.listTable = list()  #表格视图关联列表
        self.listSEPPT = list()  #SE问题PPT列表
        self.listSE = list()  #SE问题列表

        if not self.boolStyle:
            #self.actionImportSEPPTs.setVisible(False)
            #self.actionExportSEtoExcel.setVisible(False)

            self.actionShowTask.setVisible(False)
            self.actionShowAllWorkFlow.setVisible(False)
            self.actionShowAllMainstone.setVisible(False)
            self.actionShowAllDataReleasePlan.setVisible(False)
            self.actionShowAllWorkFlowOpened.setVisible(False)
            self.actionShowAllSEProblem.setVisible(False)
            self.actionShowAllSEProblemOpened.setVisible(False)
            self.actionRefresh.setVisible(False)

        #self.actionNewTask.triggered.connect(self.active_TASK_Dialog)
        self.actionImportSEPPTs.triggered.connect(self.import_problem_sheet)
        self.actionExportSEtoExcel.triggered.connect(self.export_SE_to_excel)

        #self.actionSetupDefaultFile.triggered.connect(self.setup_default_directory)
        self.actionRefresh.triggered.connect(self.initial)
        self.actionShowTask.triggered.connect(self.show_task)
        self.actionShowAllWorkFlow.triggered.connect(self.show_allpj_workflow)
        self.actionShowAllWorkFlowOpened.triggered.connect(self.show_workflow_opened)
        self.actionShowAllMainstone.triggered.connect(self.show_allpj_mainstone)
        self.actionShowAllDataReleasePlan.triggered.connect(self.show_allpj_datareleaseplan)
        self.actionShowAllSEProblem.triggered.connect(self.show_all_SE)
        self.actionShowAllSEProblemOpened.triggered.connect(self.show_all_SE_opened)

        self.actionExit.triggered.connect(self.close)

        self.treeWidget.customContextMenuRequested.connect(self.custom_right_menu_tree)
        self.tableWidget.customContextMenuRequested.connect(self.custom_right_menu_table)

        #初始化数据
        self.initial()

    #初始化
    def initial(self):
        self.TaskList.clear()  #普通任务列表
        self.DefaultDirectory = ""  #默认文件路径
        self.table_style = 0  #表格视图关联数据类型标识
        self.ProjectList.clear()  #项目列表
        self.listTable.clear()  #表格视图关联列表
        self.progressBar.setValue(0)

        if self.boolStyle :
            self.DefaultDirectory = "E:\MY DOCUMENTS\PyQtTask Files"
        else:
            self.DefaultDirectory = QFileDialog.getExistingDirectory (self,'设置默认文件夹',"/home",)
        taskFilePath = self.DefaultDirectory + "\\OptionFiles\\TaskData.xlsx"
        tasklist_wb = TaskEXECL()
        tasklist_wb.read_task_list(taskFilePath,self.TaskList)  #导入Task信息
        pjDirectory = self.DefaultDirectory + "\\ProjectFiles"
        pjFileList = os.listdir(pjDirectory)
        for pjFileName in pjFileList:
            pj = Project()
            #pj.filepath = pjDirectory + "/" + pjFileName
            pj.projectfile.initial(pjDirectory,pjFileName)
            pjFileNameList = pjFileName.split(".")
            pj.name = pjFileNameList[0]
            pj.read_project_EXCEL()
            pj.caculate_percentage()
            self.ProjectList.append(pj)
        self.initial_TreeWidget()  #初始化树控件

    #设置默认文件夹
    #def setup_default_directory(self):
        #self.DefaultDirectory = QFileDialog.getExistingDirectory (self,'设置默认文件夹',"/home",)

    #在表格视图中显示任务
    def show_task(self):
        self.table_style = 1
        self.initial_TableWidget(self.TaskList,self.table_style)    

    #在表格视图中显示所有项目NA和关闭外的业务流
    def show_workflow_opened(self):
        self.table_style = 2
        self.listTable.clear()
        for pj in self.ProjectList:
            for wfi in pj.workflow.workflowlist:
                if ((wfi.status != str("NA")) & (wfi.status != str("已完成"))):
                    self.listTable.append(wfi)
        self.initial_TableWidget(self.listTable,self.table_style)

    #在表格视图中显示所有项目业务流
    def show_allpj_workflow(self):
        self.table_style = 2
        self.listTable.clear()
        for pj in self.ProjectList:
            self.listTable += pj.workflow.workflowlist
        self.initial_TableWidget(self.listTable,self.table_style)

    #在表格视图中显示所有项目主进度
    def show_allpj_mainstone(self):
        self.table_style = 3
        self.listTable.clear()
        for pj in self.ProjectList:
            self.listTable.append(pj.mainmilestone)
        self.initial_TableWidget(self.listTable,self.table_style)

    #在表格视图中显示所有项目数据发布节点
    def show_allpj_datareleaseplan(self):
        self.table_style = 4
        self.listTable.clear()
        for pj in self.ProjectList:
            self.listTable += pj.datareleaseplan.datareleaseplan
        self.initial_TableWidget(self.listTable,self.table_style)

    #在表格视图中显示所有SE问题
    def show_all_SE(self):
        self.table_style = 5
        self.listTable.clear()
        for ppt in self.listSEPPT:
            self.listTable += ppt.problem_set.problem_list
        self.initial_TableWidget(self.listTable,self.table_style)

    #在表格视图中显示所有未关闭SE问题
    def show_all_SE_opened(self):
        self.table_style = 5
        self.listTable.clear()
        for ppt in self.listSEPPT:
            for sep in ppt.problem_set.problem_list:
                if sep.status != 4:
                    self.listTable.append(sep)
        self.initial_TableWidget(self.listTable,self.table_style)

    #树视图右键菜单设置函数
    def custom_right_menu_tree(self, pos):
        menu = QMenu()
        item = self.treeWidget.currentItem()
        if item.childCount() == 0:
            project = Project()
            item_Parent = item.parent()
            for pj in self.ProjectList:
                if item_Parent.text(0) == pj.name:
                    project = pj
                    break
            if item.text(0) == "主进度":
                opt1 = menu.addAction("显示")
                action = menu.exec_(self.treeWidget.mapToGlobal(pos))
                if action == opt1:
                    self.table_style = 3
                    self.listTable.clear()
                    self.listTable.append(project.mainmilestone)
                    self.initial_TableWidget(self.listTable,self.table_style)
                    return
                else:
                    return
            elif item.text(0) == "数据发布节点":
                opt1 = menu.addAction("显示")
                action = menu.exec_(self.treeWidget.mapToGlobal(pos))
                if action == opt1:
                    self.table_style = 4
                    self.listTable.clear()
                    self.listTable += project.datareleaseplan.datareleaseplan
                    self.initial_TableWidget(self.listTable,self.table_style)
                    return
                else:
                    return
            elif item.text(0) == "业务流":
                opt1 = menu.addAction("显示所有")
                opt2 = menu.addAction("显示未完成")
                action = menu.exec_(self.treeWidget.mapToGlobal(pos))
                if action == opt1:
                    self.table_style = 2
                    self.listTable.clear()
                    self.listTable += project.workflow.workflowlist
                    self.initial_TableWidget(self.listTable,self.table_style)
                    return
                elif action == opt2:
                    self.table_style = 2
                    self.listTable.clear()
                    for wfi in project.workflow.workflowlist:
                        if ((wfi.status != str("NA")) & (wfi.status != str("已完成"))):
                            self.listTable.append(wfi)
                    self.initial_TableWidget(self.listTable,self.table_style)
                    return
                else:
                    return

    #表格视图右键菜单设置函数
    def custom_right_menu_table(self, pos):
        menu = QMenu()
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        item = self.tableWidget.currentItem()

        if self.table_style == 1:
            opt1 = menu.addAction("编辑")
            opt2 = menu.addAction("新增工作内容")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            QMessageBox.information(None,'消息','任务',QMessageBox.Yes | QMessageBox.No)
        elif self.table_style == 2:
            opt1 = menu.addAction("编辑")
            opt2 = menu.addAction("新增工作步骤")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == opt1:
                text, ok = QInputDialog().getText(self, "编辑信息","更新为")
                if ok:
                    item.setText(text)
                    self.update_database(row,col,text)
                return
            elif action == opt2:
                return
            else:
                return
        elif self.table_style == 3:
            opt1 = menu.addAction("编辑")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            QMessageBox.information(None,'消息','主进度',QMessageBox.Yes | QMessageBox.No)
        elif self.table_style == 4:
            opt1 = menu.addAction("编辑")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            QMessageBox.information(None,'消息','数据发布节点',QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(None,'消息','非法的table类型！',QMessageBox.Yes | QMessageBox.No)
            return

    #根据tableWidget中最新状态更新database
    def update_database(self,row,col,str_new_info):
        item_row_head = self.tableWidget.item(row,0)
        if self.table_style == 1:
            QMessageBox.information(None,'消息','任务',QMessageBox.Yes | QMessageBox.No)
        elif self.table_style == 2:
            pj_name = item_row_head.text()
            project = Project()
            for pj in self.ProjectList:
                if pj_name == pj.name:
                    project = pj
                    break
            index_wfi = self.tableWidget.item(row,2).text()
            #QMessageBox.information(None,'消息',str(index_wfi),QMessageBox.Yes | QMessageBox.No)
            #QMessageBox.information(None,'消息',str(len(project.workflow.workflowlist)),QMessageBox.Yes | QMessageBox.No)
            for wfi in project.workflow.workflowlist:
                #wfi.show_info()
                if index_wfi == wfi.index:
                    if 6 == col:
                        wfi.responsible = str_new_info
                    elif 8 == col:
                        wfi.date_planed = str_new_info
                    elif 9 == col:
                        wfi.date_closed = str_new_info
                    elif 10 == col:
                        wfi.status = str_new_info
                    elif 11 == col:
                        wfi.note = str_new_info
                    else:
                        QMessageBox.information(None,'消息',"不可编辑！",QMessageBox.Yes | QMessageBox.No)
                        break
                #wfi.show_info()
                wfi.write_a_wfi_to_EXCEL(project.projectfile.filepath)
        elif self.table_style == 3:
            QMessageBox.information(None,'消息','主进度',QMessageBox.Yes | QMessageBox.No)
        elif self.table_style == 4:
            QMessageBox.information(None,'消息','数据发布节点',QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(None,'消息','非法的table类型！',QMessageBox.Yes | QMessageBox.No)
        #self.


    #初始化树视图
    def initial_TreeWidget(self):
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['名称','值'])
        root=QTreeWidgetItem(self.treeWidget)
        root.setText(0,'Root')
        for pj in self.ProjectList:
            child = QTreeWidgetItem()
            child.setText(0,pj.name)            
            root.addChild(child)
            child_1 = QTreeWidgetItem()
            child_1.setText(0,'主进度')
            child.addChild(child_1)
            child_2 = QTreeWidgetItem()
            child_2.setText(0,'数据发布节点')
            child.addChild(child_2)
            child_3 = QTreeWidgetItem()
            child_3.setText(0,'业务流')
            child_3.setText(1,str(pj.percentage))
            child.addChild(child_3)
            child_4 = QTreeWidgetItem()
            child_4.setText(0,'问题')
            child.addChild(child_4)
        self.treeWidget.expandAll()

    #初始化表视图
    def initial_TableWidget(self,list,style):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(list))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)#所有列自动拉伸，充满界面
        self.tableWidget.resizeColumnsToContents()#设置列宽高按照内容自适应
        self.tableWidget.resizeRowsToContents()#设置行宽和高按照内容自适应
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows);  # 设置只有行选中, 整行选中

        if(style == 1):
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['任务简述','创建时间','计划完成时间','实际完成时间','状态','备注'])
            #index = 0
            for index in range(len(list)):
                aTask = list[index]
                col = 0
                newItem = QTableWidgetItem(str(aTask.name))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aTask.date_created.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aTask.date_planed.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aTask.date_closed.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aTask.status))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aTask.note))
                self.tableWidget.setItem(index, col, newItem)
        elif(style == 2):
            self.tableWidget.setColumnCount(12)
            self.tableWidget.setHorizontalHeaderLabels(['项目','阶段','序号','业务流内容简述','输入','输出','负责人','Milestone','计划完成时间','实际完成时间','状态','备注'])
            for index in range(len(list)):
                aWorkFlowItem = list[index]
                col = 0
                newItem = QTableWidgetItem(str(aWorkFlowItem.project))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.phase))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.index))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.name))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.imput))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.output))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.responsible))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.milestone))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.date_planed))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.date_closed))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.status))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aWorkFlowItem.note))
                self.tableWidget.setItem(index, col, newItem)
        elif(style == 3):
            self.tableWidget.setColumnCount(8)
            self.tableWidget.setHorizontalHeaderLabels(['项目','G9','G8','G7','G6','G5','G4','G1'])
            for index in range(len(list)):
                aMainMileStone = list[index]
                col = 0
                newItem = QTableWidgetItem(str(aMainMileStone.project))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G9.date))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G8.date))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G7.date))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G6.date))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G5.date))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G4.date))
                self.tableWidget.setItem(index, col, newItem)
                '''
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G3.date))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G2.date))
                self.tableWidget.setItem(index, col, newItem)'''
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G1.date))
                self.tableWidget.setItem(index, col, newItem)
                '''
                col += 1
                newItem = QTableWidgetItem(str(aMainMileStone.G0.date))
                self.tableWidget.setItem(index, col, newItem)'''
        elif(style == 4):
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['项目','数据&状态','计划发布时间','实际发布时间','状态','备注'])
            for index in range(len(list)):
                aDataReleasePlanItem = list[index]
                col = 0
                newItem = QTableWidgetItem(str(aDataReleasePlanItem.project))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aDataReleasePlanItem.name))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aDataReleasePlanItem.date_planed))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aDataReleasePlanItem.date_real))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aDataReleasePlanItem.status))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aDataReleasePlanItem.note))
                self.tableWidget.setItem(index, col, newItem)
        elif(style == 5):
            self.tableWidget.setColumnCount(13)
            self.tableWidget.setHorizontalHeaderLabels(['项目','问题序号','问题描述','建议措施','问题进展','状态','TOP','干系人','创建时间','计划关闭时间','跟踪时间','实际关闭时间','专业区域'])
            for index in range(len(list)):
                aSEProblem = list[index]
                col = 0
                newItem = QTableWidgetItem(str(aSEProblem.project))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.index))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.brief_and_reason))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.suggestion))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.detail_and_progress))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.status))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.top))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.stakeholder))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.date_created.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.date_planed.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.date_followed.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.date_closed.datetime))
                self.tableWidget.setItem(index, col, newItem)
                col += 1
                newItem = QTableWidgetItem(str(aSEProblem.area_division))
                self.tableWidget.setItem(index, col, newItem)
        else:
            QMessageBox.information(None,'消息','非法的Table类型！',QMessageBox.Yes | QMessageBox.No)

    """菜单《导入问题单》响应函数"""
    def import_problem_sheet(self):
        #清空列表框
        strListSEPPT = []
        #获取PPT文件名
        aQString = QFileDialog.getOpenFileNames(self,'打开SE问题单','','Powerpoint Files(*.ppt *.pptx):All Files(*.*)')
        aString = str(aQString)
        strListSEPPT = aString.split("'",)
        lensth = len(strListSEPPT) - 3
        current_index = 1
        while current_index <= lensth:
            if len(strListSEPPT[current_index]) == 0:
                return
            else:
                """在SE PPT列表中添加一个对象"""
                aProblemSheetPPT = SESheetPPT()
                aProblemSheetPPT.filename = strListSEPPT[current_index]
                self.listSEPPT.append(aProblemSheetPPT)
                current_index += 2

        """循环遍历SE PPT列表，读取PPT内容"""
        current_index = 0
        while current_index < len(self.listSEPPT):
            if not self.listSEPPT[current_index].isread:
                    self.listSEPPT[current_index].read_problem_sheet(self.progressBar)
            current_index += 1

        QMessageBox.information(None,'消息','导入完成！',QMessageBox.Yes | QMessageBox.No)

    """菜单《导出问题单》响应函数"""
    def export_SE_to_excel(self):
        SEOverview = OverveiwSheetEXCEL()
        """写入相关信息"""
        SEOverview.write_information(self.listSEPPT,self.progressBar,2)
        """保存EXCEL文件"""
        SEOverview.save_EXCEL_file()
        QMessageBox.information(None,'消息','导出完成！',QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    app = QApplication([])
    window = PyQtTask()
    window.show()
    sys.exit(app.exec_())
