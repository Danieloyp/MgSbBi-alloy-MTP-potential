#!/bin/bash
#SBATCH -p batch
#SBATCH -J lammps
# Number of nodes
#SBATCH -N 1
# Number of tasks per node
#SBATCH --ntasks-per-node=8
# Number of cores per task
#SBATCH --cpus-per-task=1


#intel oneapi
source /home/share/intel/oneapi/setvars.sh intel64 --force
export LD_LIBRARY_PATH=/home/share/intel/oneapi/mkl/2023.1.0/lib/intel64:/home/share/intel/oneapi/compiler/2023.1.0/linux/compiler/lib/intel64_lin:$LD_LIBRARY_PATH
INPUT=in.mcmd

MPIRUN=”/home/share/intel/oneapi/2021.9.0/bin/mpirun”
cd $SLURM_SUBMIT_DIR
mpirun -np ${SLURM_NTASKS} /home/softpackages/lammps-nep/src/lmp_mpi -in ${INPUT}
