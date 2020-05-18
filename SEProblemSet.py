# coding: utf-8

from Topic import Topic
from SEProblem import SEProblem
from PyQt5.QtWidgets import QMessageBox

class SEProblemSet(Topic):
    #问题集合类
    def __init__(self):
        #初始化集合类
        super().__init__()
        self.problem_list = list()  #问题列表        
        #问题数汇总字典
        self.num_status = {}
        #状态
        self.num_status['close'] = 0
        self.num_status['check'] = 0
        self.num_status['follow'] = 0
        self.num_status['action'] = 0
        self.num_status['analysis'] = 0
        self.num_status['start'] = 0
        #分类
        self.num_division = {}
        self.num_division['造型'] = 0
        self.num_division['DTS前部'] = 0
        self.num_division['DTS后部'] = 0
        self.num_division['下车体'] = 0
        self.num_division['上车体'] = 0
        self.num_division['门盖'] = 0
        self.num_division['内外饰前部'] = 0
        self.num_division['内外饰后部'] = 0
        self.num_division['工艺'] = 0
        self.num_division['测量方案'] = 0
        #风险
        self.num_risk = {}
        self.num_risk['low'] = 0
        self.num_risk['middle'] = 0
        self.num_risk['high'] = 0
        #汇总
        self.sum = 0

    '''在尾端添加问题'''
    def append(self,problem):
        #在表尾添加一个问题
        self.problem_list.append(problem)
            
    '''分析问题集是否符合规范并统计集合中的问题数'''
    def analysis(self,strErrorLog):
        for problem in self.problem_list:
            if 1== problem.risk:
                self.num_risk['high'] += 1
            elif 2== problem.risk:
                self.num_risk['middle'] += 1
            elif 3 == problem.risk:
                self.num_risk['low'] += 1
            else:
                strErrorLog = "error 问题风险 of problem of " + problem.project + problem.index + ".\n"
                QMessageBox.information(None,'消息',strErrorLog,QMessageBox.Yes | QMessageBox.No) 
                return False
                
            if "1" == problem.status:
                self.num_status['start'] += 1
            elif "2" == problem.status:
                self.num_status['analysis'] += 1
            elif "3" == problem.status:
                self.num_status['action'] += 1
            elif "4" == problem.status:
                self.num_status['follow'] += 1
            elif "5" == problem.status:
                self.num_status['check'] += 1
            elif "6" == problem.status:
                self.num_status['close'] += 1
            else:
                strErrorLog = "error 问题状态 of problem of " + problem.project + problem.index + ".\n"
                QMessageBox.information(None,'消息',strErrorLog,QMessageBox.Yes | QMessageBox.No) 
                return False

            if '造型' == problem.area_division:
                self.num_division['造型'] += 1
            elif 'DTS前部' == problem.area_division:
                self.num_division['DTS前部'] += 1
            elif 'DTS后部' == problem.area_division:
                self.num_division['DTS后部'] += 1
            elif '下车体' == problem.area_division:
                self.num_division['下车体'] += 1
            elif '上车体' == problem.area_division:
                self.num_division['上车体'] += 1
            elif '门盖' == problem.area_division:
                self.num_division['门盖'] += 1
            elif '内外饰前部' == problem.area_division:
                self.num_division['内外饰前部'] += 1
            elif '内外饰后部' == problem.area_division:
                self.num_division['内外饰后部'] += 1
            elif '工艺' == problem.area_division:
                self.num_division['工艺'] += 1
            elif '测量方案' == problem.area_division:
                self.num_division['测量方案'] += 1
            else:
                strErrorLog = "error 专业区域 of problem of " + problem.project + problem.index + ".\n"
                QMessageBox.information(None,'消息',strErrorLog,QMessageBox.Yes | QMessageBox.No) 
                return False
                
        self.sum = self.num_risk['high'] + self.num_risk['middle'] + self.num_risk['low']
        return True