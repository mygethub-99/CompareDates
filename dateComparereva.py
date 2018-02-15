# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:22:06 2018

@author: OW4253
"""

from dateutil.relativedelta import *
from datetime import *
import re

tofile = []

with open('compare.csv') as f:
    next(f)
    for line in f:
        trklist = []
        lstarter = line.split(',')
        '''      Orgsiteaq, OrgConStComp, OrgOnAir,  SAQComp'''
        list1 = (lstarter[2],lstarter[3],lstarter[4],lstarter[5])
        '''      SAQComp,   ConStComp,   FcOnAir,    FcOnAir'''
        list2 = (lstarter[5],lstarter[6],lstarter[7],lstarter[7])
        '''      FA,        SAQComp,     FCConStComp,  FcOnAir'''
        list3 = (lstarter[1],lstarter[5],lstarter[6],lstarter[7])
        
        #Loop to organize list for relative date
        for i, y, z in zip(list1, list2, list3):
            ls = date(int(i[0:4]), int(i[4:6]), int(i[6:8]))
            olaq = date(int(y[0:4]), int(y[4:6]), int(y[6:8]))
            comp = str(relativedelta (olaq, ls))
            #comb = (str(z), comp[14:])
            trklist.insert(len(trklist), ((z), comp[14:]))
            if len(trklist) == 4:
                tofile.append([trklist])
                del(trklist)
            
with open('deltplayreva.txt', 'w') as fs:
    fs.write("'FA_Code''Delta_SA''SAQ_Comp''Delta_ConStart''ForConStart'\
    'Delta_OnAir''ForCastOnAir''Delta_SAQ_OnAir'")
    fs.write("\n")
    for i in tofile:
        i = str(i)
        i = re.sub("[]()[,]", "", i)
        fs.write("{}\n".format(i))
fs.close() 
