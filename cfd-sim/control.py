'''
Author: wanglei
Date: 2022-11-03 20:41:44
LastEditTime: 2022-11-03 21:20:47
Description: Do not edit
'''
from seed.pathconvey import alter,pathconvey
from seed.output import outputdict,fluentoutputs
from seed.input import inputdict,input4fluent,inputparas

import sys,os
# rootpath =   # 路径尽量传绝对路径
rootpath = os.path.abspath(sys.argv[1])
jobname = sys.argv[2]
resultdir = sys.argv[3]

pathdict = {
    "rootpath-seed":rootpath,
    "jobname-seed":jobname,
    "resultdir-seed":resultdir
}

## 向cse文件传入路径
file = "%s/seed/cfdpost-seed.cse" % rootpath
pathconvey(file, pathdict, rootpath, jobname)


## 向jou文件传入路径
file = "%s/seed/simulation.jou" % rootpath
pathconvey(file, pathdict, rootpath, jobname)

## 读取输入参数
INPUT = inputparas('%s/input'%rootpath)
## 写入fluent脚本
input4fluent(INPUT,inputdict,'%s/%s.jou'%(rootpath,jobname))

## 读取输出表
OUTPUT = fluentoutputs(outputdict,'%s/fluent-outputs.out'%resultdir)
print(OUTPUT)
