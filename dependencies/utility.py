import string
import random
from . import validation as vv
from . import login_check as lc
import os

def random_captcha():
    
    '''
    generates a random alphanumeric captcha
    '''
    
    s = 5
    sentence = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))
    return sentence

def registration_status_code(var_dict):
    
    '''
    checks registration status
    '''
    
    if(var_dict['user_captcha']!=var_dict['real_captcha']):
        return 0
    elif(not(vv.email_validation(var_dict['username']))):
        return 1
    elif(lc.check_email_present(var_dict['username'],1)):
        return 2
    elif(vv.passcheck(var_dict['password'])):
        return 3
    else:
        arr = var_dict
        lc.add_xls_row(arr)
        return 4    

def login_status_code(var_dict):
    
    '''
    checks login status
    '''
    
    if(var_dict['user_captcha']!=var_dict['real_captcha']):
        return 0
    elif(not(lc.check_email_present(var_dict['username'],1))):
        return 1
    else:
        return lc.creditional_check(var_dict['username'],var_dict['password'],1)
    
def admin_status_code(var_dict):
    
    '''
    checks admin login status
    '''
    
    #status_dict = {0:'Wrong Captcha', 1:'Invalid Credentials'}
    if(var_dict['user_captcha']!=var_dict['real_captcha']):
        return 0
    elif(not(lc.check_email_present(var_dict['username'],0))):
        return 1
    else:
        return lc.creditional_check(var_dict['username'],var_dict['password'],0)
    #return the status_code only
    #just for testing

def open_file():
    
    '''
    opens excel file
    '''
    
    loc = os.path.dirname(__file__) +'\databases\studentinfo.xlsx'
    lc.check_file(loc,1)
    os.system(f'start EXCEL.EXE {loc}')
    
def submit(var,row):
    
    '''
    checks for successful submission
    '''
    if not vv.phone_number_validation(var[8]):
        return 1
    elif not vv.phone_number_validation(var[9]):
        return 2
    elif int(var[15]) > 100 or int(var[15]) < 0:
        return 3
    for c in var[-1]:
        try:
            c = int(c)
            if c < 0 and c > 100:
                return 4
        except:
            return 4
    if '' in var[1:]:
        return 5
    else:
        var = var[:-1] + [','.join(var[-1])]
        lc.submit_save(var,row)
        return 6
        
    
if __name__ == '__main__':
    
    open_file()