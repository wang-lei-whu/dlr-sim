'''
Author: wanglei
Date: 2022-11-03 15:59:29
LastEditTime: 2022-11-03 21:21:59
Description: Pass the working directory from the pbs file to fluent, 
cfdpost and other softwares.
'''

# from stringprep import c6_set, c7_set

import re, os
from shutil import copyfile, move


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


def pathconvey(file, pathdict, rootpath, jobname):
    copyfile(file, "%s.bak" % file)
    end = file[file.rfind('.'):]
    for key, value in pathdict.items():
        alter("%s.bak" % file, key, "%s/" % value)
    move("%s.bak" % file, "%s/%s.%s" % (rootpath, jobname, end))
