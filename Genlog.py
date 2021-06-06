from xlwt import Workbook
import json
import re

class Genlog:
    def __init__(self,path_log,path_field,path_result ,sheet_name) -> None:
        self.log_file = open(path_log, 'r')
        self.log_line = self.log_file.read().splitlines()
        self.field_json = open(path_field ,'r').read()
        self.field = json.loads(self.field_json)['field']
        self.path_result = path_result
        self.wb = Workbook()
        self.sheet=self.wb.add_sheet(sheetname=sheet_name)
        self.temp = None
        pass
    def create_title(self):
        for i in range(0,len(self.field)):
            self.sheet.write(0,i,self.field[i])
    def log_data_processing(self):
        for line in self.log_line:
            for i in range(1,len(self.field)):
                if(self.match(re.search("{\""+self.field[0]+"\":\d+[,]\""+self.field[i]+"\":\d+}", line))):
                    row = self.temp[self.field[0]]
                    col = i
                    value = self.temp[self.field[i]]
                    self.sheet.write(row,0,row)
                    self.sheet.write(row,col,value)
                    break

    def save(self):
        self.wb.save(self.path_result)
    def run(self):
        self.create_title()
        self.log_data_processing()
        self.save()
    def match(self,match):
        if(match):
            self.temp = json.loads(match.group())
            return True
        else :
            return False


a= Genlog("logfile.log", "field.json","result.xls","Door Log")
a.run()
