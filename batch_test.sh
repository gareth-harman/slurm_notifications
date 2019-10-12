#!/bin/bash

#SBATCH --job-name=test
#SBATCH --output=res.txt
#SBATCH --error=res.txt
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=1G
#SBATCH --parsable

/group_shares/dbil/bulk/nagel_lab/staff/gareth/slurm_complete/test_mail.sh
