import os
from tkinter.constants import TRUE
import openpyxl
import pathlib

def check_file(loc,info=0):
    file = pathlib.Path(loc)
    if not(file.exists()):
        if info == 0:
            data=["Email","Password"]
        else:
            data=['Registration Number','Name','DOB','Father\'s Name','Mother\'s Name','Gender','Dept','Domicile','Mother\'s Phone Number','Father\'s Phone Number','Email Id','Present Address','Permanent Address']

        wb =openpyxl.workbook.Workbook()
        ws0 = wb.worksheets[0]
        ws0.append(data)
        wb.save(filename =loc)

def check_email_present(email,log):
    if log == 1:
        loc=os.path.dirname(__file__) +'\studentlogininfo.xlsx'
    else:
        loc=os.path.dirname(__file__) +'\adminlogininfo.xlsx'
    check_file(loc)
    book =openpyxl.load_workbook(loc)
    sheet = book.active
    for i in range(1,sheet.max_row+1):
        if(((sheet.cell(row=i,column=1)).value)==email):
            return True
    return False
def load(email):
    loc2=os.path.dirname(__file__) +'\studentinfo.xlsx'
    check_file(loc2,1)
    book =openpyxl.load_workbook(loc2)
    sheet = book.active
    info_dict={}
    for i in range(1,sheet.max_row+1):
        if(((sheet.cell(row=i,column=11)).value)==email):
            for j in range(1,13):
                if (sheet.cell(row=i,column=j)).value == None:
                    info_dict[(sheet.cell(row=1,column=j)).value]=''
                else:
                    info_dict[(sheet.cell(row=1,column=j)).value]=(sheet.cell(row=i,column=j)).value
            print(info_dict)
            return info_dict
def creditional_check(email,password,log):
    if log == 1:
        loc=os.path.dirname(__file__) +'\studentlogininfo.xlsx'
    else:
        loc=os.path.dirname(__file__) +'\adminlogininfo.xlsx'
    check_file(loc)
    book =openpyxl.load_workbook(loc)
    sheet = book.active
    for i in range(1,sheet.max_row+1):
        if((sheet.cell(row=i,column=1)).value)==email:
#             print((sheet.cell(row=i,column=1)).value)
            
            if((sheet.cell(row=i,column=2)).value)==password:
               
                return load(email)
            else:
                return 1
def save_xls_file(arr,register):
    if register == 1:
        workbook_name = os.path.dirname(__file__) +'\studentinfo.xlsx'
        workbook2_name = os.path.dirname(__file__) +'\studentlogininfo.xlsx'
        check_file(workbook_name,1)
        check_file(workbook2_name)
        
        wb =openpyxl.load_workbook(workbook_name)
        page = wb.active
        record = 10*[''] + [arr['username']] + 2*['']
        page.append(record)
        wb.save(filename =workbook_name)
        
        wb =openpyxl.load_workbook(workbook2_name)
        page = wb.active
        record = [arr['username'], arr['password']]
        page.append(record)
        wb.save(filename =workbook2_name)
        
    else:
        pass
    
if __name__ == '__main__':
    
    save_xls_file({'username':'abracadabra.@gmail.com', 'password':'124josk'},1)