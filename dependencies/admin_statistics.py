from . import login_check as lc
import pandas as pd
import os
    
def count_applicants():
    
    '''
    Counts number of total applicants
    '''
    
    loc = os.path.dirname(__file__) +'\databases\studentinfo.xlsx'
    lc.check_file(loc,1)
    database = pd.read_excel(loc,index_col=0)
    total_applicants = len(database.dropna(axis=0))
    return total_applicants

if __name__ == '__main__':
    count_applicants()