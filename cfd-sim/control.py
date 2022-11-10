'''
Author: wanglei
Date: 2022-11-03 20:41:44
LastEditTime: 2022-11-10 21:13:30
Description: Do not edit
'''
from seed.pathconvey import alter, pathconvey
from seed.output import outputdict, fluentoutputs,casesDataAppend
from seed.input import inputdict, input4fluent, inputparas,inputtranslate,inputinitialdict
import sys, os
# rootpath =   # 路径尽量传绝对路径
# rootpath = os.path.abspath(sys.argv[1])

if __name__ == '__main__':
    rootpath = sys.argv[1]+"/"
    jobname = sys.argv[2]
    resultdir = sys.argv[3]+"/"
    module = sys.argv[4]

    if module == "input":
        pathdict = {
            "rootpath-seed": rootpath,
            "jobname-seed": jobname,
            "resultdir-seed": resultdir
        }

        ## 向cse文件传入路径
        file = "%sseed/cfdpost-seed.cse" % rootpath
        pathconvey(file, pathdict, rootpath, jobname)

        ## 向jou文件传入路径
        file = "%sseed/simulation.jou" % rootpath
        pathconvey(file, pathdict, rootpath, jobname)

        ## 读取输入参数
        INPUT = inputparas('%sinput' % rootpath)
        INPUT_trans = inputtranslate(INPUT,inputinitialdict,inputdict)
        ## 写入fluent脚本
        input4fluent(INPUT_trans, inputdict, '%s%s.jou' % (rootpath, jobname))
    elif module == "output":
        ## 读取输出表
        INPUT = inputparas('%sinput' % rootpath)
        INPUT_trans = inputtranslate(INPUT,inputinitialdict,inputdict)
        OUTPUT = fluentoutputs(outputdict, '%sfluent-outputs.out' % resultdir)
        ## 将输入输出写入cases文件
        casesDataAppend(OUTPUT,'%sseed/casesdata.dat'%rootpath,INPUT)
        casesDataAppend(OUTPUT,'%scasedata.dat'%resultdir,INPUT_trans)
    # elif module == "optimize":
    #     ## 根据cases文件生成
