'''
Author: wanglei
Date: 2022-11-03 15:59:29
LastEditTime: 2022-11-03 21:06:56
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
