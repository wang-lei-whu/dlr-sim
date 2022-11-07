# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:12:54 2022

@author: Guoming
"""
import os
import numpy as np

fid = open('./Xdata.dat','r')
datastr = fid.readlines()
fid.close()
x = ','.join([t.strip('\n') for t in datastr])

fid = open('./Cd.csv','r')
datastr = fid.readlines()
fid.close()
x1 = datastr[-1]
x2 = x1.split(',')
Cd = np.float64(x2[1]) + np.float64(x2[5])
print("Cd = {}".format(Cd))

fid = open('./Cl.csv','r')
datastr = fid.readlines()
fid.close()
x1 = datastr[-1]
x2 = x1.split(',')
Cl = np.float64(x2[1]) + np.float64(x2[5])
print("Cl = {}".format(Cl))

fid = open('./cases_XCdCl.dat','r')
datastrXCdCl = fid.readlines()
fid.close()
n = len(datastrXCdCl)

line = str(n) + ',' + x + ',' + str(Cd) + ',' + str(Cl) + '\n'
fid = open('./cases_XCdCl.dat','a')
fid.write(line)
fid.close()
print("\n-----------------------------------------------------------------------")
print("\nBoth Cd and Cl values have been added into \"cases_XCdCl.dat\" successfully!\n")
print("-----------------------------------------------------------------------\n")

