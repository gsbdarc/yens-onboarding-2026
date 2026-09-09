#!/bin/bash
#SBATCH --job-name=hello
#SBATCH --partition=normal
#SBATCH --output=logs/hello_%j.out
#SBATCH --error=logs/hello_%j.err
#SBATCH --time=00:01:00
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1

cd $HOME/yens-onboarding-2026

echo "Hello, world!"
