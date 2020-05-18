# coding: utf-8

from LDatetime import LDateTime
from Task import Task
#from Project import Project
from PIL import Image
from enum import Enum

'''class SEProblemStatus(Enum):
    start = 1
    analysis = 2
    action = 3
    follow = 4
    check =5
    close = 6    
class Risk(Enum):
    High = 1
    Middle = 2
    Low = 3
class Area_Division(Enum):
    Style = 1
    FrontDTS = 2
    RearDTS = 3
    Unterbody = 4
    UpperBody = 5
    HoodDoorTrunk = 6
    FrontAssembly = 7
    RearAssembly = 8
    Process = 9
    Measurement = 10'''

class SEProblem(Task):
    #问题类
    def __init__(self):
        #初始化车型类
        super().__init__()
        self.index = ""  #索引
        self.project = ""  #所属项目
        self.creater = ""  #创建者
        self.area_product = ""  #产品区域
        self.area_division = ""  #专业区域
        #self.source = ""  #来源
        #self.index_source = ""  #来源清单内序号
        #self.final_solution = ""  #最终措施
        self.brief_and_reason = ""  #简述和原因
        self.suggestion = ""  #建议措施
        self.detail_and_progress = ""  #详述和进展
        self.prevention_and_result = ""  #预案与结果
        self.risk = 0  #风险
        self.stakeholder = ""  #干系人
        self.version_start_1 = ""  #问题提出时数据版本
        self.version_end_1 = ""  #问题关闭时数据版本
        self.version_start_2 = ""  #问题提出时数据版本
        self.version_end_2 = ""  #问题关闭时数据版本
        self.version_start_3 = ""  #问题提出时数据版本
        self.version_end_3 = ""  #问题关闭时数据版本
        self.version_start_4 = ""  #问题提出时数据版本
        self.version_end_4 = ""  #问题关闭时数据版本

        self.MIR_id = ""  #MIR问题单ID号
        self.MR_id = ""  #MR问题点ID号
        self.style_SE = ""  #问题类型
        self.EPorPPV = False  #是否EP或PPV跟踪验证，默认不跟踪
        self.LLR = False  #是否触发LLR，默认不触发
        self.stlye_LLR = ""  #触发LLR类型
        self.update_MR = False  #是否更新MR，默认不更新
        self.EWO_id = ""  #此问题发起的EWO号