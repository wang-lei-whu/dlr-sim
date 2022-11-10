#!/bin/bash
###
 # @Author: wanglei
 # @Date: 2022-11-03 15:59:29
 # @LastEditTime: 2022-11-10 20:27:40
 # @Description: Do not edit
### 
# cd cfd-sim

rm  *.trn
rm *.log
source /home/wanglei/.bashrc


export PBS_O_WORKDIR=`pwd`
export PBS_JOBNAME='test-auto-dlr'
export RESULTDIR=$PBS_O_WORKDIR/results
mkdir $RESULTDIR
touch $RESULTDIR/casedata.dat


conda activate sm_optimized

function  pythoninput (){

    python3 control.py $PBS_O_WORKDIR $PBS_JOBNAME $RESULTDIR "input" >>output.log 2>&1

    if [ $? -eq 0 ]; then
        echo "python input succeed"
    else
        echo "python input failed"
        exit 1
    fi
}
function fluentcal(){
    fluent 3ddp -g -ssh -pdefault -t32 -i $PBS_JOBNAME.jou >>output.log 2>&1
    if [ $? -eq 0 ]; then
        echo "fluent calculation succeed"
    else
        echo "fluent calculation failed"
        exit 2
    fi
}
function cfdpostcal(){
    cfdpost -batch $PBS_JOBNAME.cse >>output.log 2>&1
    if [ $? -eq 0 ]; then
        echo "cfdpost calculation succeed"
    else
        echo "cfdpost calculation failed"
        exit 3
    fi
}
function pythonoutput(){
    python3 control.py $PBS_O_WORKDIR $PBS_JOBNAME $RESULTDIR "output" >>output.log 2>&1
    if [ $? -eq 0 ]; then
        echo "python output succeed"
    else
        echo "python output failed"
        exit 4
    fi
}

## 处理参数
if [ ! -n "$1" ] ;then
    echo "do all works"
    pythoninput
    fluentcal
    cfdpostcal
    pythonoutput
else
    case $1 in 
    4) 
        pythonoutput;;
    3)
        cfdpostcal;;
    2)
        fluentcal;;
    1)
        pythoninput;;
    0)
        bash cleanup*.sh
        mv *.jou $RESULTDIR
        mv *.cse $RESULTDIR
        mv *.log $RESULTDIR;;
    -h)
        echo '      0：清理生成文件
        1：进行变量输入
        2：进行fluent运算
        3：进行cfdpost绘图
        4：进行python后处理
        -h:显示帮助
        空：执行全流程';;
    *)
        echo -n "unknown parameter given";;
    esac
fi

conda deactivate

