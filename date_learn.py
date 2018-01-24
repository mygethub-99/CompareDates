# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:22:06 2018

@author: OW4253
"""

from dateutil.relativedelta import *
from datetime import *

mklist = []
today = date.today()

with open('datecompare.csv') as f:
    next(f)
    for line in f:
        lstarter = line.split(',')
        ls = lstarter[5] ; ls2= lstarter[6]; ls3 = lstarter[7]
        olaq = lstarter[8] ; olcs = lstarter[10] ; olcf = lstarter[11]
        
        ls = date(int(ls[0:4]), int(ls[4:6]), int(ls[6:8]))
        olaq = date(int(olaq[0:4]), int(olaq[4:6]), int(olaq[6:8]))
        comp = str(relativedelta (olaq, ls))
        
        ls2 = date(int(ls2[0:4]), int(ls2[4:6]), int(ls2[6:8]))
        olcs = date(int(olcs[0:4]), int(olcs[4:6]), int(olcs[6:8]))
        comp2 = str(relativedelta (olcs, ls2))
        
        ls3 = date(int(ls3[0:4]), int(ls3[4:6]), int(ls3[6:8]))
        olcf = date(int(olcf[0:4]), int(olcf[4:6]), int(olcf[6:8]))
        comp3 = str(relativedelta (olcf, ls3))
        
        block = (lstarter[1],comp[14:].strip(')'), comp2[14:].strip(')'), \
        comp3[14:].strip(')'), lstarter[8], lstarter[10], lstarter[13])
        mklist.insert(0, block)
        
with open('deltatracker.txt', 'w') as fs:
    fs.write("'FA_Code' 'SiteAqDel' 'ConStarDel' 'ConFinDel' 'SA' 'ConStar'\
    'On-Air'")
    fs.write("\n")
    for i in mklist:
        i = str(i).strip('()')
        i = i.replace(",", "")
        fs.write("{}\n".format(i))
fs.close()
