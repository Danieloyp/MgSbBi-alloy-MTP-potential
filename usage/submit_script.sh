#!/bin/bash
#SBATCH -J lammps
#SBATCH -N 1
#SBATCH --ntasks-per-node=72
#SBATCH -p xhacnormalb
module purge
module load mpi/intelmpi/2020.1.217

srun --mpi=pmi2 lmp_intel_cpu_intelmpi -i in.elastic

