#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=4
#SBATCH --time=96:00:00
#SBATCH --mail-type=fail
#SBATCH --mail-type=end
#SBATCH --mail-user=dhlee1@sheffield.ac.uk

module load Anaconda3/2019.07
source activate cosmos
module load OpenMPI/4.0.3-GCC-9.3.0
module load OpenBLAS/0.3.9-GCC-9.3.0
module load CFITSIO/3.48-GCCcore-9.3.0

source /users/smp24dhl/cosmo/code/planck/clik/bin/clik_profile.sh

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

mpirun -np 4 cobaya-run act-wmap.yaml
