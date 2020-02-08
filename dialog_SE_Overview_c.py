# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QDialog
from dialog_seoverview import Ui_Dialog_SEOverview

from SEProblemSet import SEProblemSet
from SESheetPPT import SESheetPPT
from OverviewSheetEXCEL import OverveiwSheetEXCEL

class dialog_SE_Overview_c(QDialog,Ui_Dialog_SEOverview):
    def __init__(self):
        QMainWindow.__init__(self)

        #QMessageBox.information(None,'消息','提示1',QMessageBox.Yes | QMessageBox.No)

        self.setupUi(self)
        #QMessageBox.information(None,'消息','提示2',QMessageBox.Yes | QMessageBox.No)

        self.pushButton_ImportSEProblemSheet.clicked.connect(self.import_problem_sheet)
        #self.pushButton_ExportOverviewSheet.clicked.connect(self.save_problem_overview)
        #self.pushButton_SelectSEProblemSheet.clicked.connect(self.select_problem_sheet)

        self.style = False  #标记导出EXCEL格式，ture为项目；false为工程师
        self.radioButton_Project.toggled.connect(lambda :self.btnstate(self.radioButton_Project))
        self.radioButton_Engineer.toggled.connect(lambda :self.btnstate(self.radioButton_Engineer))
        self.problem_set = SEProblemSet()  #专业类对象

        self.SEPPTList = list()   #SE问题单list
        self.SEOverview = OverveiwSheetEXCEL()

        #版本信息
        #self.version = 0.2
        #self.initial_information()

        self.progressBar_SE.setValue(0)

        def initial_information(self):  #初始化窗口信息
            #显示版本号
            str_version = "版本号为：V" + str(self.version) + "."
            self.label_Version.setText(str_version)
            #显示log
            self.listWidget_verLog.clear()
            self.listWidget_verLog.addItem("V0.2.2:新增SE问题单工程师模式；可接受2000-2-2、2000/1/1和2000.1.1格式日期；更换为Qt Creator环境。")
            self.listWidget_verLog.addItem("V0.2.1:修复读取空格时间错误的BUG。")
            self.listWidget_verLog.addItem("V0.2:新增进度条功能、状态列和TOP列底纹显示，TOP问题汇总功能。")
            self.listWidget_verLog.addItem("V0.1:实现基本读取PPT信息功能。")
            #初始化进度条
            self.progressBar_SE.setValue(0)

        def import_problem_sheet(self):  #Button《导入问题单》响应函数
            #循环遍历SE PPT列表，读取PPT内容
            current_index = 0
            while current_index < len(self.SEPPTList):
                if not self.SEPPTList[current_index].isread:
                    self.SEPPTList[current_index].read_problem_sheet(self.progressBar_SE)
                current_index += 1

        def save_problem_overview(self):  #Button《保存问题Overview》响应函数
            self.SEOverview.write_information(self.SEPPTList,self.progressBar_SE,self.style)  #写入相关信息
            self.SEOverview.save_EXCEL_file()  #保存EXCEL文件

        def select_problem_sheet(self):  #Button《选择SE问题单》响应函数
            #清空列表框
            self.listWidget_listSEPPT.clear()
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
                    #在SE PPT列表中添加一个对象
                    aProblemSheetPPT = SESheetPPT()
                    aProblemSheetPPT.filename = strListSEPPT[current_index]
                    self.SEPPTList.append(aProblemSheetPPT)
                    #在列表框中显示SE PPT路径
                    self.listWidget_listSEPPT.addItem(strListSEPPT[current_index])
                    current_index += 2

        def btnstate(self,btn):  #输出按钮1与按钮2的状态，选中还是没选中
            if btn.text()=='Project':
                if btn.isChecked()==True:
                    self.style = True
            if btn.text()=="Engineer":
                if btn.isChecked() == True:
                    self.style = False
