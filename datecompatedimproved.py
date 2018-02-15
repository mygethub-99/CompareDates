# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:22:06 2018

@author: OW4253
"""

from dateutil.relativedelta import *
from datetime import *
tofile = []

with open('datecompare.csv') as f:
    next(f)
    for line in f:
        trklist = []
        lstarter = line.split(',')
        '''OrgSiteAq, OrgConSt, OrgConfin'''
        list1 = (lstarter[5] , lstarter[6] , lstarter[7])
        '''SiteAqComp, ConSt, ConCompl'''
        list2 = (lstarter[8] , lstarter[10] , lstarter[11])
        '''FA, ConSt, OnAir'''
        list3 = (lstarter[1], lstarter[10], lstarter[13])
        
        #Loop to organize list for relative date
        for i, y, z in zip(list1, list2, list3):
            ls = date(int(i[0:4]), int(i[4:6]), int(i[6:8]))
            olaq = date(int(y[0:4]), int(y[4:6]), int(y[6:8]))
            comp = str(relativedelta (olaq, ls))
            #comb = (str(z), comp[14:])
            trklist.insert(1, (str(z), comp[14:]))
            if len(trklist) == 3:
                tofile.insert(0, [trklist])
                del(trklist)
            
with open('deltplay.txt', 'w') as fs:
    fs.write("'FA_Code' 'SiteAqDel' 'ConStarDel' 'ConFinDel' 'SA' 'ConStar'\
    'On-Air'")
    fs.write("\n")
    for i in tofile:
        i = str(i).strip('[]')
        #i = i.replace(",", "")
        fs.write("{}\n".format(i))
fs.close() 
