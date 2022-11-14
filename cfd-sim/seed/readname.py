import re


def getname(file, old_str):
    out = 0
    with open(file, "r") as f1:
        for line in f1:
            if re.search(old_str, line):
                out = line.split("#PBS -N ")[1]
    return out


print(getname("/home/wanglei/dlr-auto-test/cfd-sim/dlr-flu.pbs", "#PBS -N "))
