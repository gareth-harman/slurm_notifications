#!/usr/bin/python3

import subprocess

# 1 JobId
# 2 Running
# 3 JobName
# 4 User



result = subprocess.run(['squeue', '-u', 'harmang'], stdout=subprocess.PIPE).stdout.decode('utf-8')
result = result.split('\n')[1:]

content = [list(filter(None, x.split(' '))) for x in result]
content = list(filter(None, content))

jobIds = [x[0] for x in content]

for ii in jobIds:

	maxRAM = subprocess.run(['sstat', '-job', str(ii), '--format=MaxRSS'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	maxRAM = list(filter(None, maxRAM.split('\n')[2:]))[0]
	#maxRAM = list(filter(None, maxRAM.split(' ')))

	maxRAM_flt = float(maxRAM.split('K')[0])
	maxRAM_mb = maxRAM_flt/1024
	maxRAM_gb = maxRAM_mb/1024

	print('JobID: {} Max RAM {}'.format(ii, round(maxRAM_gb, 4)))
