# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:22:06 2018

@author: OW
"""

from dateutil.relativedelta import *
from datetime import *

mklist = []

with open('datecompare.csv') as f:
    next(f)
    for line in f:
        lstarter = line.split(',')
        list1 = (lstarter[5] , lstarter[6] , lstarter[7])
        list2 = (lstarter[8] , lstarter[10] , lstarter[11])
        list3 = (lstarter[1], lstarter[10], lstarter[13])
        
        def repeater(list1, list2, list3):
            for i, y, z in zip(list1, list2, list3):
                ls = date(int(i[0:4]), int(i[4:6]), int(i[6:8]))
                olaq = date(int(y[0:4]), int(y[4:6]), int(y[6:8]))
                comp = str(relativedelta (olaq, ls))
                comb = (str(z), comp[14:], )
                mklist.insert(0, comb)
        repeater(list1, list2, list3)
        print (mklist)
        
with open('deltplay.txt', 'w') as fs:
    fs.write("'FA_Code' 'SiteAqDel' 'ConStarDel' 'ConFinDel' 'SA' 'ConStar'\
    'On-Air'")
    fs.write("\n")
    for i in mklist:
        i = str(i).strip('()')
        i = i.replace(",", "")
        fs.write("{}\n".format(i))
fs.close()
