
cd cfd-sim
export PBS_O_WORKDIR=`pwd`
export PBS_JOBNAME='test-auto-dlr'
export RESULTDIR=$PBS_O_WORKDIR/results

mkdir $RESULTDIR

python pathconvey.py $PBS_O_WORKDIR $PBS_JOBNAME $RESULTDIR
mv $PBS_JOBNAME* $RESULTDIR
