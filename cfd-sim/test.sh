###
 # @Author: wanglei
 # @Date: 2022-11-03 15:59:29
 # @LastEditTime: 2022-11-03 19:30:28
 # @Description: bash script for test
###
cd cfd-sim
mkdir $RESULTDIR
export PBS_O_WORKDIR=`pwd`
export PBS_JOBNAME='test-auto-dlr'
export RESULTDIR=$PBS_O_WORKDIR/results

python seed/pathconvey.py $PBS_O_WORKDIR $PBS_JOBNAME $RESULTDIR
mv $PBS_JOBNAME* $RESULTDIR
