#!/usr/bin/python3

import subprocess

# 1 JobId
# 2 Running
# 3 JobName
# 4 User

################################################################################
# Function to retrieve current jobIDs for a given user
################################################################################

def get_curr_jobs(user='harmang'):

    # CMD to pass in
    squeue_cmd = ['squeue', '-u', user]

    # Call squeue and parse result
    init_result = subprocess.run(squeue_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    init_result = result.split('\n')[1:]
    
    # Split jobs and remove empyt chars
    content = [list(filter(None, x.split(' '))) for x in result]
    content = list(filter(None, content))
    
    # Get job Ids specifically
    jobIds = [x[0] for x in content]
    
    return jobIds

################################################################################

################################################################################
# Function to retrieve current jobIDs for a given user
################################################################################

def get_max_ram(jobid, val = 'gb'):
    
    # CMD to pass in
    ram_cmd = ['sstat', '-job', str(jobid), '--format=MaxRSS']
    
    # Call to grab maxram of a job
	maxRAM = subprocess.run(ram_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
	maxRAM = list(filter(None, maxRAM.split('\n')[2:]))[0]
    
    # Parse a bit
	maxRAM_flt = float(maxRAM.split('K')[0])
	
	# Return correct format
	if val == 'mb':
	    return round(maxRAM_flt/1024, 4)
	else:
	    return round(maxRAM_flt/1024, 4)
	    
################################################################################


jobIds = get_curr_jobs()

for ii in jobIds:

	maxRAM = subprocess.run(['sstat', '-job', str(ii), '--format=MaxRSS'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	maxRAM = list(filter(None, maxRAM.split('\n')[2:]))[0]
	#maxRAM = list(filter(None, maxRAM.split(' ')))

	maxRAM_flt = float(maxRAM.split('K')[0])
	maxRAM_mb = maxRAM_flt/1024
	maxRAM_gb = maxRAM_mb/1024

	print('JobID: {} Max RAM {}'.format(ii, round(maxRAM_gb, 4)))
