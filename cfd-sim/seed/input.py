'''
Author: wanglei
Date: 2022-11-03 15:59:29
LastEditTime: 2022-11-10 21:09:22
Description: read input data 
'''

import numpy as np
from seed.pathconvey import alter


def inputparas(inputfile)-> np.ndarray:
    ## read input data
    fid = open(inputfile,'r')
    datastr = fid.readlines()
    fid.close()
    x1 = [t.strip('\n') for t in datastr]
    x2 = [np.float64(t) for t in x1]
    return np.array(x2)


## export geometry parameters to fluent meshing


def input4fluent(input,dict,file):
    ## export inner parameters to jou files for fluent
    for key in dict:
        alter(file, key, "%s" % input[dict[key]])
    


# def input4cfdpost(input):

## 规定输入参数表   
inputdict = {
    "airflow-seed":0,
    "fuelflow-seed":1,
    "inlettem-seed":2
}

## 输入参数归一化
## 思路：区基准值，标定变化范围后最大最小值归一化
inputinitialdict = {
    "airflow-seed":np.array([0.01762,0.9,1.1]),
    "fuelflow-seed":np.array([0.000696,0.9,1.1]),
    "inlettem-seed":np.array([330,1,2])
}

def inputtranslate(input,inputinitialdict,inputdict) ->np.ndarray:
    res = np.zeros(input.size)
    for key,value in inputinitialdict.items():
        min = value[0]*value[1]## 映射-1
        max = value[0]*value[2]## 映射1
        res[inputdict[key]] = (input[inputdict[key]]+1)/2*(max-min)+min
    return res
