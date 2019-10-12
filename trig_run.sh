#!/bin/bash

jid=$1

strigger --set --jobid=${jid} --fini --program=/group_shares/dbil/bulk/nagel_lab/staff/gareth/slurm_complete/run_fin.sh
