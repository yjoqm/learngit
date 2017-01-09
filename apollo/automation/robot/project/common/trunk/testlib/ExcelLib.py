# -*- coding: utf-8 -*-

import os
import sys
import platform
from robot.api import *
from run_cmd import RunCmd
import xlrd
import xlwt
from xlutils.copy import copy
user_module_path = os.path.dirname(os.path.realpath(__file__))

class ExcelLib:
    def __init__(self):
        self.is_selected = False
        self.cell_type = {0 : "EMPTY", 1 : "TEXT", 2 : "NUMBER",
                          3 : "DATE", 4 : "BOOLEAN", 5 : "ERROR", 6 : "BLANK"}
        if "Windows" == platform.system():
            self.tmp_path = os.environ.get("TEMP")
        elif "Linux" == platform.system():
            self.tmp_path = "/tmp"
        self.style = xlwt.Style.default_style
        
    def __tmp_xls_gen(self):
        file_name = self.tmp_path + "/tmp_excel.xls"
        if self.excel_change:
            self.save_as(file_name)
            self.read_book = xlrd.open_workbook(file_name, formatting_info = True)
            self.excel_change = False
        return self.read_book.sheet_by_index(self.current_sheet_index)
        
    
    def open_excel(self, excel_file):
        self.excel_file = excel_file
        excel = xlrd.open_workbook(excel_file, formatting_info = True)
        self.sheet_name_list = map(lambda x:x.name, excel.sheets())
        self.excel = copy(excel)
        self.excel_change = True
        
    def select_sheet(self, selector = "index", value = 1):
        if selector == "index":
            try:
                self.current_sheet_index = int(value) - 1
            except ValueError, ex:
                raise AssertionError("the index of sheet must be int")
        elif selector == "name":
            self.current_sheet_index = self.sheet_name_list.index(value)
        else:
            raise AssertionError("selector must be 'index' or 'name'")
        self.cuurent_sheet = self.excel.get_sheet(self.current_sheet_index)
        self.is_selected = True
        
    
    def __is_selected_sheet(self):
        if not self.is_selected:
            raise AssertionError("you have not selected a sheet yet")
        
    def __get_type(self, type_list, display):
        if display == "char":
            return map(lambda x:self.cell_type[x], type_list)
        elif display == "num":
            return map(lambda x:x, type_list)
        else:
            raise AssertionError("display must be 'char' or 'num'")            
    
    def get_row_values(self, row_num):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()
        return sheet.row_values(int(row_num) - 1)
    
    def get_row_types(self, row_num, display = "char"):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()
        type_list = sheet.row_types(int(row_num) - 1)
        return self.__get_type(type_list, display)
        
    
    def get_col_values(self, col_num):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()
        return sheet.col_values(int(col_num) - 1)
    
    def get_col_types(self, col_num, display = "char"):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()
        type_list = sheet.col_types(int(col_num) - 1) 
        return self.__get_type(type_list, display)
    
    def get_cell_value(self, row_num, col_num):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()
        return sheet.cell_value(int(row_num) - 1, int(col_num) - 1)
    
    def get_cell_type(self, row_num, col_num, display = "char"):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()
        type_list = sheet.cell_type(int(row_num) - 1, int(col_num) - 1) 
        return self.__get_type([type_list], display)[0]    
    
    def get_row_count(self):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()        
        return len(sheet._cell_values)
    
    def get_col_count(self):
        self.__is_selected_sheet()
        sheet = self.__tmp_xls_gen()        
        return reduce(max, map(lambda x:len(x), sheet._cell_values))
    
    def get_sheet_names(self):
        return self.sheet_name_list
    
    def get_sheets_count(self):
        return len(self.sheet_name_list)
    
    def create_blank_excel(self, excel_file):
        self.excel = xlwt.Workbook()
        sheet = self.excel.add_sheet("Sheet1")
        self.excel.save(excel_file)
        self.excel_change = True
        
    def create_excel(self):
        self.excel = xlwt.Workbook()
        self.sheet_name_list = []
        
    def add_sheet(self, sheet_name):
        self.excel.add_sheet(sheet_name, cell_overwrite_ok=True)
        self.sheet_name_list.append(sheet_name)
        self.excel_change = True
        
    def sheet_write(self, row_num, col_num, content):
        self.__is_selected_sheet()
        self.cuurent_sheet.write(int(row_num) - 1, int(col_num) - 1, content, self.style)
        self.excel_change = True
    
    def save(self):
        self.excel.save(self.excel_file)
        pass
    
    def save_as(self, file_name):
        self.excel.save(file_name)
        
    def __del__(self):
        if os.path.exists(self.tmp_path + "/tmp_excel.xls"):
            os.remove(self.tmp_path + "/tmp_excel.xls")
            pass
    
            


if __name__ == '__main__':
    test = ExcelLib()
    test.open_excel("/home/yan_jiawei/vmsystem/share/12345.xls")
    test.select_sheet("index",1)
    #test.create_excel()
    test.add_sheet("asdasd3")
    test.select_sheet("index", 3)
    test.sheet_write(9,17,5)
    test.sheet_write(9,10,6)
    test.save()
    print test.get_row_values(9)
    print test.get_row_types(9)
    print test.get_col_values(10)
    print test.get_col_types(10)
    print test.get_cell_value(9,17)
    print test.get_cell_type(9,17)
    print test.get_row_count()
    print test.get_col_count()
    print test.get_sheet_names()
    print test.get_sheets_count()    