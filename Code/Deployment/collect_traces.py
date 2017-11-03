"""
	Program to save traces for urls listed at URLS_FILE

	Rahul Kejriwal
	CS14B023
"""

import os
import sys
import time
import subprocess
from threading import Thread
from tqdm import tqdm

# Config vars
DATA_PATH = "Test_Data"
URLS_FILE = "test_sites"

"""
	Create directory if not already existing
"""
def create_dir(name):
	if not os.path.exists(name):
		os.makedirs(name)

"""
	Spawns tshark for time_val seconds
"""
def tshark_trace_capture(name, time_val):
	with open(DATA_PATH + '/' + str(name) + '.trace', 'w') as fp:
		subprocess.call('tshark -a duration:'+str(time_val), shell=True, stdout=fp)

"""
	Captures network traffic for time_val seconds 
"""
def save_trace(url, time_val):
	tshark_thread = Thread(target=tshark_trace_capture, args= (url, time_val,) )
	tshark_thread.start()

	subprocess.call(['google-chrome', url])
	
	tshark_thread.join()
	

"""
	__main__
"""

# Check usage
if len(sys.argv) != 3:
	print "Usage: python collect_traces.py <time_wait_for_url_load> <i>"
	sys.exit(1)

# Cmd line params
num_traces = 3
time_wait  = int(sys.argv[1])
start_i = int(sys.argv[2])

# Read urls for trace generation
with open(URLS_FILE) as fp:
	urls = [line.strip() for line in fp] 

# Create traces for each url
create_dir(DATA_PATH)
for url in tqdm(urls[start_i:]):
	for i in range(num_traces):
		save_trace(url, time_wait)
	break