# Pass the working directory from the pbs file to fluent, cfdpost
# and other softwares.

from genericpath import exists
# from stringprep import c6_set, c7_set
import sys

from matplotlib.cbook import ls_mapper

rootpath = sys.argv[1]  # 获得外部参数,参数0指向脚本名字
jobname = sys.argv[2]
resultdir = sys.argv[3]
# print(rootpath)  # 打印


import re, os
from shutil import copyfile

def alter(file, old_str, new_str):
    ##替换法修改文件内容
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file,
                                                       "w",
                                                       encoding="utf-8") as f2:
        for line in f1:           
                if re.search(old_str, line):
                    f2.write(re.sub(old_str, new_str, line))
                else:
                    f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

## 向cse文件传入
file = "%s/seed/cfdpost-seed.cse" % rootpath
copyfile(file, "%s.bak" % file) 
alter("%s.bak" % file, "rootpath-seed","\"%s/\"" % rootpath)
alter("%s.bak" % file, "jobname-seed","\"%s\"" % jobname)
alter("%s.bak" % file, "resultdir-seed","\"%s/\"" % resultdir)
os.rename("%s.bak" % file,"%s.cse"%jobname)

## 向jou文件传入
file = "%s/seed/simulation.jou" % rootpath
copyfile(file, "%s.bak" % file) 
alter("%s.bak" % file, "rootpath-seed","\"%s/\"" % rootpath)
alter("%s.bak" % file, "jobname-seed","\"%s\"" % jobname)
os.rename("%s.bak" % file,"%s.jou"%jobname)
