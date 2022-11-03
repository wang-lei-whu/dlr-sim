'''
Author: wanglei
Date: 2022-11-03 15:59:29
LastEditTime: 2022-11-03 21:05:07
Description: output workflow definition
'''

import numpy as np
import re

## 规定输出参数表
outputdict = {
    "out-co2":0,
    "out-tem":1,
}

def fluentoutputs(dict,file)->np.ndarray:
    dict0=dict.copy()
    output=np.zeros(len(dict))
    with  open(file,'r') as fid:
        for line in fid:
            for key in dict0:
                if not re.search(key,line) is None:
                    output[dict0[key]]=float(re.search("\d*\.*\d*e\+\\d*",line,re.I).group())
                    dict0.pop(key)
                    break
    return output



