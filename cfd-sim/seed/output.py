'''
Author: wanglei
Date: 2022-11-03 15:59:29
LastEditTime: 2022-11-10 17:31:41
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
                    output[dict0[key]]=float(re.search("(?<=\s)\d*\.+\d*e.\d*",line,re.I).group())
                    dict0.pop(key)
                    break
    return output

def casesDataAppend(output,file,input):
    x=', '.join([str(t) for t in input.tolist()])
    y=', '.join([str(t) for t in output.tolist()])
    with open(file,'r') as fid:
        n = len(fid.readlines())
    with open(file,'a') as fid:
        line = str(n)+', '+ x+', '+y+'\n'
        fid.write(line)
    print("\n-----------------------------------------------------------------------")
    print("\nBoth input and output values have been added into %s successfully!\n"%file)
    print("-----------------------------------------------------------------------\n")





