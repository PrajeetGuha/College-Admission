import string
import random
from . import validation as vv
from . import login_check as lc
import os

def random_captcha():
    
    s = 5
    sentence = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))
    return sentence

def registration_status_code(var_dict):
    
    #status_dict = {0:'Wrong Captcha', 1:'Username Invalid', 2:'Username Previously Registered', 3:'Password should be atleast 8 character long', 4:'Registration Done Successfully'}
    if(var_dict['user_captcha']!=var_dict['real_captcha']):
        return 0
    if(not(vv.email_validation(var_dict['username']))):
        return 1
    if(lc.check_email_present(var_dict['username'],1)):
        return 2
    if(vv.passcheck(var_dict['password'])):
        return 3
    else:
        arr = var_dict
        lc.save_xls_file(arr,1)
        return 4
    #return the status_code only
    
    pass

def login_status_code(var_dict):
    
    #status_dict = {0:'Wrong Captcha', 1:'Invalid Credentials'}
    if(var_dict['user_captcha']!=var_dict['real_captcha']):
        return 0
    if(not(lc.check_email_present(var_dict['username'],1))):
        return 1
    else:
        return lc.creditional_check(var_dict['username'],var_dict['password'],1)
    #return the status_code only
    #just for testing
    
def admin_status_code(var_dict):
    
    #status_dict = {0:'Wrong Captcha', 1:'Invalid Credentials'}
    '''if(var_dict['user_captcha']!=var_dict['real_captcha']):
        return 0
    if(not(lc.check_email_present(var_dict['username'],0))):
        return 1
    else:
        return lc.creditional_check(var_dict['username'],var_dict['password'],0)'''
    #return the status_code only
    return 2#just for testing

def open_file():
    
    loc = os.path.dirname(__file__) +'\databases\studentinfo.xlsx'
    lc.check_file(loc,1)
    os.system(f'start EXCEL.EXE {loc}')
    
if __name__ == '__main__':
    
    open_file()