# coding: utf-8

#from openpyxl import Workbook
from File_EXCEL import File_EXCEL
from File_EXCEL import excel_cell_style
import datetime

from PyQt5.QtWidgets import QMessageBox

class OverveiwSheetEXCEL(File_EXCEL):
    """问题清单EXCEL类"""
    def __init__(self):
        super().__init__()        
        
        #问题数汇总字典
        self.num_status = {}
        #状态
        self.num_status['close'] = 0
        self.num_status['check'] = 0
        self.num_status['follow'] = 0
        self.num_status['action'] = 0
        self.num_status['analysis'] = 0
        self.num_status['start'] = 0

        #汇总
        self.sum = 0

        self.version = "V0.0"  #SE问题单系统版本号
        
    """初始化EXCEL表格"""
    def initial_EXCEL(self,style):
        cellStyle = excel_cell_style()
        '''初始化SE问题清单页'''
        ws = self.workbook.active
        ws.title = "同步工程问题清单"
        the_row = 1
        the_column = 1 
        #写问题表页标题
        if style:
            ws.row_dimensions[1].height = 50
            ws.cell(row=1, column=2, value="同步工程问题清单")
            ws.merge_cells('B1:AE1')
            the_row += 1
        #else:
            #the_row = 1

        #初始化问题表页标题行与列 
        #设置问题表页标题行行高
        ws.row_dimensions[the_row].height = 30              
        if not style:
            ws.cell(row=the_row, column=the_column, value="项目")
            ws.column_dimensions['A'].width = 20
        else:
            ws.column_dimensions['A'].width = 1
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="问题序号")
        ws.column_dimensions['B'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="问题描述")
        ws.column_dimensions['C'].width = 40
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="建议措施")
        ws.column_dimensions['D'].width = 40
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="问题进展")
        ws.column_dimensions['E'].width = 40
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="状态")
        ws.column_dimensions['F'].width = 10
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="MIR")
        ws.column_dimensions['G'].width = 10
        '''if self.version == "V2.0":
            the_column += 1
            ws.cell(row=the_row, column=the_column, value="MIR")
            ws.column_dimensions['G'].width = 10
        else:
            the_column += 1
            ws.column_dimensions['G'].width = 0'''
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="干系人")
        ws.column_dimensions['H'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="创建时间")
        ws.column_dimensions['I'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="计划关闭时间")
        ws.column_dimensions['J'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="实际关闭时间")
        ws.column_dimensions['K'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="产品区域")
        ws.column_dimensions['L'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="专业区域")
        ws.column_dimensions['M'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="问题类型")
        ws.column_dimensions['N'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="相关MR索引")
        ws.column_dimensions['O'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="是否EP/PPV验证")
        ws.column_dimensions['P'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="是否触发LLR")
        ws.column_dimensions['Q'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="触发类型")
        ws.column_dimensions['R'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="是否更新MR")
        ws.column_dimensions['S'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="创建者")
        ws.column_dimensions['T'].width = 20
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（发生时）-1")
        ws.column_dimensions['U'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（解决时）-1")
        ws.column_dimensions['V'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（发生时）-2")
        ws.column_dimensions['W'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（解决时）-2")
        ws.column_dimensions['X'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（发生时）-3")
        ws.column_dimensions['Y'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（解决时）-3")
        ws.column_dimensions['Z'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（发生时）-4")
        ws.column_dimensions['AA'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="零件号&版本（解决时）-4")
        ws.column_dimensions['AB'].width = 35
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="EWO号")
        ws.column_dimensions['AC'].width = 20    
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="预防措施or验证结果")
        ws.column_dimensions['AD'].width = 40         
        the_column += 1
        ws.cell(row=the_row, column=the_column, value="备注")
        ws.column_dimensions['AE'].width = 40    
        
        #设置问题表页标题行样式
        cellStyle.set_as_sheet_title()
        if style:
            cell = ws.cell(row=1, column=2)
            cell.font = cellStyle.font
            cell.alignment = cellStyle.alignment
            cell.border = cellStyle.border
            the_row = 2
        else:
            the_row = 1
        cellStyle.set_as_title()
        for y in range(1,32):
            cell = ws.cell(row=the_row, column=y)
            cell.font = cellStyle.font
            cell.alignment = cellStyle.alignment
            cell.border = cellStyle.border
                        
        #初始化SE问题汇总表页
        ws_overview = self.workbook.create_sheet("Overview")        
        the_row = 1
        ws_overview.cell(row=the_row, column=1, value="专业区域")
        ws_overview.cell(row=the_row, column=2, value="状态6：问题关闭")
        ws_overview.cell(row=the_row, column=3, value="状态5：措施验证&EP/PPV验证")
        ws_overview.cell(row=the_row, column=4, value="状态4：措施实施")
        ws_overview.cell(row=the_row, column=5, value="状态3：措施提出")
        ws_overview.cell(row=the_row, column=6, value="状态2：问题分析")
        ws_overview.cell(row=the_row, column=7, value="状态1：问题提出")
        ws_overview.cell(row=the_row, column=8, value="问题总数")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="造型")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="DTS前部")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="DTS后部")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="下车体")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="上车体")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="门盖")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="内外饰前部")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="内外饰后部")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="工艺")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="测量方案")
        the_row += 1
        ws_overview.cell(row=the_row, column=1, value="合计")
        
        #设置单元格样式
        for y in range(1,9):
            cell = ws_overview.cell(row=1, column=y)
            cell.font = cellStyle.font
            cell.alignment = cellStyle.alignment
            cell.border = cellStyle.border
        for x in range(1,the_row+1):
            cell = ws_overview.cell(row=x, column=1)
            cell.font = cellStyle.font
            cell.alignment = cellStyle.alignment
            cell.border = cellStyle.border
        cellStyle.set_as_text_in_center()
        for x in range(2,the_row+1):
            for y in range(2,9):
                cell = ws_overview.cell(row=x, column=y)
                cell.font = cellStyle.font
                cell.alignment = cellStyle.alignment
                cell.border = cellStyle.border
        
        #设置列宽
        ws_overview.column_dimensions['A'].width = 20
        ws_overview.column_dimensions['B'].width = 25
        ws_overview.column_dimensions['C'].width = 40
        ws_overview.column_dimensions['D'].width = 25
        ws_overview.column_dimensions['E'].width = 25
        ws_overview.column_dimensions['F'].width = 25
        ws_overview.column_dimensions['G'].width = 25
        ws_overview.column_dimensions['H'].width = 15
        #设置行高
        ws_overview.row_dimensions[1].height = 20
        ws_overview.row_dimensions[2].height = 20
        ws_overview.row_dimensions[3].height = 20
        ws_overview.row_dimensions[4].height = 20
        ws_overview.row_dimensions[5].height = 20
        ws_overview.row_dimensions[6].height = 20
        ws_overview.row_dimensions[7].height = 20
        ws_overview.row_dimensions[8].height = 20
        ws_overview.row_dimensions[9].height = 20
        ws_overview.row_dimensions[10].height = 20
        ws_overview.row_dimensions[11].height = 20
        ws_overview.row_dimensions[12].height = 20
        if style:
            ws_overview.row_dimensions[13].height = 20
        
    '''写SE问题'''
    def write_problem_set(self,ws,problem_set,style,project_id):
        cellStyle = excel_cell_style()
        row_now = ws.max_row + 1
        #写入问题集内问题信息至Overview Sheet
        for problem in problem_set.problem_list:
            #设置行高            
            ws.row_dimensions[row_now].height = 50     
            #向单元格内填写数据
            the_column = 1
            if not style:
                ws.cell(row=row_now, column=the_column, value=project_id)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.index)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.brief_and_reason)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.suggestion)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.detail_and_progress)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.status)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.MIR_id)
            '''if self.version == "V2.0":
                the_column += 1
                ws.cell(row=row_now, column=the_column, value=problem.MIR_id)'''
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.stakeholder)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.date_created.date_string)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.date_planed.date_string)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.date_closed.date_string)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.area_product)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.area_division)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.style_SE)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.MR_id)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.EPorPPV)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.LLR)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.stlye_LLR)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.update_MR)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.creater)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_start_1)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_end_1)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_start_2)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_end_2)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_start_3)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_end_3)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_start_4)
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.version_end_4)  
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.EWO_id)  
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.prevention_and_result)                    
            the_column += 1
            ws.cell(row=row_now, column=the_column, value=problem.note)

            #设置数据行样式
            #项目号  问题序号
            cellStyle.set_as_text_in_center() 
            for y in range(1,3):
                cell = ws.cell(row=row_now, column=y)
                cell.font = cellStyle.font
                cell.alignment = cellStyle.alignment
                cell.border = cellStyle.border

            #问题详述  建议措施  问题进展
            cellStyle.set_as_text_in_left() 
            for y in range(3,6):
                cell = ws.cell(row=row_now, column=y)
                cell.font = cellStyle.font
                cell.alignment = cellStyle.alignment
                cell.border = cellStyle.border
                
            #写问题单状态及设置单元格格式
            cell = ws.cell(row=row_now, column=6)
            if 1 == problem.risk:
                cellStyle.set_as_text_in_center_and_red() 
            elif 2 == problem.risk:
                cellStyle.set_as_text_in_center_and_yellow()
            elif 3 == problem.risk:
                cellStyle.set_as_text_in_center_and_green()
            else:
                print("error problem risk.")
            cell.fill = cellStyle.fill
            cell.font = cellStyle.font
            cell.alignment = cellStyle.alignment
            cell.border = cellStyle.border

            cellStyle.set_as_text_in_center()
            for y in range(7,30):
                cell = ws.cell(row=row_now, column=y)
                cell.font = cellStyle.font
                cell.alignment = cellStyle.alignment
                cell.border = cellStyle.border

            #设置验证列、备注列单元格格式
            for y in range(30,32):
                cell = ws.cell(row=row_now, column=y)   
                cellStyle.set_as_text_in_left()         
                cell.font = cellStyle.font
                cell.alignment = cellStyle.alignment
                cell.border = cellStyle.border             

            #移动至下一行
            row_now += 1
    
    '''写汇总表'''
    def write_overview(self,ws,problemPPT,row_now):
        #循环遍历SE PPT列表，将PPT汇总内容写入EXCEL        
        problem_set = problemPPT.problem_set
        ws.cell(row=row_now, column=2, value=problem_set.num_status['close'])
        ws.cell(row=row_now, column=3, value=problem_set.num_status['check'])
        ws.cell(row=row_now, column=4, value=problem_set.num_status['follow'])
        ws.cell(row=row_now, column=5, value=problem_set.num_status['action'])
        ws.cell(row=row_now, column=6, value=problem_set.num_status['analysis'])
        ws.cell(row=row_now, column=7, value=problem_set.num_status['start'])
        ws.cell(row=row_now, column=8, value=problem_set.sum)
    
    """写PPT list至worksheet"""
    def write_information(self,sePPTlist,proressBar,style):
        self.initial_EXCEL(style)
        ws_list = self.workbook["同步工程问题清单"]
        ws_overview = self.workbook["Overview"]
        proressBar.setMaximum(len(sePPTlist))
        #循环遍历SE PPT列表，将PPT内容写入EXCEL
        current_index = 0
        while current_index < len(sePPTlist):          
            aProblemPPT = sePPTlist[current_index]            
            if not aProblemPPT.iswrite:            
                '''写SE问题'''
                self.write_problem_set(ws_list,aProblemPPT.problem_set,style,aProblemPPT.project_id)
                '''写汇总表'''
                if '造型' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,2)
                elif 'DTS前部' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,3)
                elif 'DTS后部' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,4)
                elif '下车体' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,5)
                elif '上车体' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,6)
                elif '门盖' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,7)
                elif '内外饰前部' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,8)
                elif '内外饰后部' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,9)
                elif '工艺' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,10)
                elif '测量方案' == aProblemPPT.name:
                    self.write_overview(ws_overview,aProblemPPT,11)
                else:
                    QMessageBox.information(None,'消息',"error of problem PPT name of %s"%(aProblemPPT.name),QMessageBox.Yes | QMessageBox.No)

                '''汇总数据'''
                #状态
                self.num_status['close'] += aProblemPPT.problem_set.num_status['close']
                self.num_status['check'] += aProblemPPT.problem_set.num_status['check']
                self.num_status['follow'] += aProblemPPT.problem_set.num_status['follow']
                self.num_status['action'] += aProblemPPT.problem_set.num_status['action']
                self.num_status['analysis'] += aProblemPPT.problem_set.num_status['analysis']
                self.num_status['start'] += aProblemPPT.problem_set.num_status['start']

                #汇总
                self.sum += aProblemPPT.problem_set.sum

                '''写汇总数据'''
                ws_overview.cell(row=12, column=2, value=self.num_status['close'])
                ws_overview.cell(row=12, column=3, value=self.num_status['check'])
                ws_overview.cell(row=12, column=4, value=self.num_status['follow'])
                ws_overview.cell(row=12, column=5, value=self.num_status['action'])
                ws_overview.cell(row=12, column=6, value=self.num_status['analysis'])
                ws_overview.cell(row=12, column=7, value=self.num_status['start'])
                ws_overview.cell(row=12, column=8, value=self.sum)
                
                aProblemPPT.iswrite = True
            
            proressBar.setValue(current_index + 1)
            current_index += 1

        proressBar.setValue(len(sePPTlist))

    '''保存EXCEL文件'''
    def save_EXCEL_file(self):
        self.workbook.save("sample.xlsx")
