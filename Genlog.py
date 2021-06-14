from xlwt import Workbook
import json
import re
from datetime import date, datetime

class Genlog:
    def __init__(self,path_log,path_field,path_result ,sheet_name) -> None:
        self.log_file = open(path_log, 'r')
        self.log_line = self.log_file.read().splitlines()
        self.field_json = open(path_field ,'r').read()
        self.field = json.loads(self.field_json)['field']
        self.path_result = path_result
        self.wb = Workbook()
        self.sheet=self.wb.add_sheet(sheetname=sheet_name,cell_overwrite_ok=True)
        self.temp = None
        pass
    def create_title(self):
        for i in range(0,len(self.field)):
            self.sheet.write(0,i,self.field[i])
    def log_data_processing(self):
        for line in self.log_line:
            for i in range(1,len(self.field)):
                if(self.match(self.field[0],self.field[i],line)):
                    row = self.temp[self.field[0]]
                    col = i
                    if(self.field[i] == "STARTTIME"):
                        value = datetime.fromtimestamp(self.temp[self.field[i]]).strftime("%Y/%M/%D %H:%M:%S")
                    else:
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
    def match(self,stt,args,line):
        match = re.search("{\""+stt+"\":\d+[,]\""+args+"\":\d+}", line)
        if(match):
            self.temp = json.loads(match.group())
            return True
        else :
            match_1 = re.search("{\""+stt+"\":\d+[,]\""+args+"\":\d+[.]\d+}", line)
            if(match_1):
                self.temp = json.loads(match_1.group())
                return True
            else:
                match_2 = re.search("{\""+stt+"\":\d+[,]\""+args+"\":\"\w+\"}", line)
                if(match_2):
                    self.temp = json.loads(match_2.group())
                    return True
                else:
                    return False


a= Genlog("logfile.log", "field.json","result2.xls","Door Log")
a.run()
