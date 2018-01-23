# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:22:06 2018

@author: Me
"""

from dateutil.relativedelta import *
from datetime import *

#fopen = open('nsb_tracker.csv')
#contents = fopen.readlines()
#fopen.close()
mklist = []
today = date.today()

with open('nsb_tracker.csv') as f:
    next(f)
    for line in f:
        lstarter = line.split(',')
        ls = lstarter[5]
        ls2 = lstarter[7]
        ls3 = lstarter[8]
        ls = (int(ls[0:4]), int(ls[4:6]), int(ls[6:8]))
        ls = str(relativedelta(date(ls[0], ls[1], ls[2]), today))
        ls2 = (int(ls2[0:4]), int(ls2[4:6]), int(ls2[6:8]))
        ls2 = str(relativedelta(date(ls2[0], ls2[1], ls2[2]), today))
        ls3 = (int(ls3[0:4]), int(ls3[4:6]), int(ls3[6:8]))
        ls3 = str(relativedelta(date(ls3[0], ls3[1], ls3[2]), today))
        block = (lstarter[1],ls[14:].strip(')'), ls2[14:].strip(')'), ls3[14:].strip(')'))
        mklist.insert(0, block)
        
with open('mstracker.txt', 'w') as fs:
    fs.write("'FA_Code' 'SiteAq' 'ConStart' 'ConFinish'")
    fs.write("\n")
    for i in mklist:
        i = str(i).strip('()')
        i = i.replace(",", "")
        fs.write("{}\n".format(i))
fs.close()
