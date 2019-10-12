#!/usr/bin/python3

import subprocess
import smtplib, ssl

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


################################################################################
# Function to send email
################################################################################

def send_email(msg, receiver_email='gharman07@gmail.com'):
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "slurm.completed@gmail.com"  # Enter your address
    receiver_email = "gharman07@gmail.com"  # Enter receiver address
    password = 'slurm_done_100'
    
    
    
    message = """\
    Subject: Hi there
    
    This message is sent from Python."""
    
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)

################################################################################



jobIds = get_curr_jobs()

for ii in jobIds:

	jobRAM = get_max_ram(ii)
	
	print('JobID: {} Max RAM {}'.format(ii, jobRAM))
