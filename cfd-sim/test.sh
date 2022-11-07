###
 # @Author: wanglei
 # @Date: 2022-11-03 15:59:29
 # @LastEditTime: 2022-11-07 17:02:40
 # @Description: Do not edit
### 
cd cfd-sim
mkdir $RESULTDIR
export PBS_O_WORKDIR=`pwd`
export PBS_JOBNAME='test-auto-dlr'
export RESULTDIR=$PBS_O_WORKDIR/results

python3 control.py $PBS_O_WORKDIR $PBS_JOBNAME $RESULTDIR "input"
mv $PBS_JOBNAME* $RESULTDIR
