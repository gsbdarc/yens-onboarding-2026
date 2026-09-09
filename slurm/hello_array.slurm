#!/bin/bash
#SBATCH --job-name=hello-array
#SBATCH --partition=normal
#SBATCH --output=logs/hello_%A_%a.out
#SBATCH --error=logs/hello_%A_%a.err
#SBATCH --time=00:01:00
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1
#SBATCH --array=0-3

cd $HOME/yens-onboarding-2026

echo "Hello, world! My task number is $SLURM_ARRAY_TASK_ID"
