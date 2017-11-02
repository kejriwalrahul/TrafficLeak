"""
	Parse network logs to build featurified dataset

	Rahul Kejriwal
	CS14B023
"""

import os
import numpy as np

from tqdm import tqdm

# Config vars
DATA_PATH = "../../Datasets/Full Dataset/"
self_ip = '192.168.1.'

def server_len(lines):
	server_lines = [line for line in lines if not line[2].startswith(self_ip)]
	return len(server_lines)

def client_len(lines):
	client_lines = [line for line in lines if line[2].startswith(self_ip)]
	return len(client_lines)

def server_avg_pkt_len(lines):
	lengths = [int(line[6]) for line in lines if not line[2].startswith(self_ip)]
	return sum(lengths) / len(lengths)

def client_avg_pkt_len(lines):
	lengths = [int(line[6]) for line in lines if line[2].startswith(self_ip)]
	if len(lengths):
		return sum(lengths) / len(lengths)
	else:
		return 0

def server_std_dev_pkt_len(lines):
	lengths = [int(line[6]) for line in lines if not line[2].startswith(self_ip)]
	return np.std(lengths)

def client_std_dev_pkt_len(lines):
	lengths = [int(line[6]) for line in lines if line[2].startswith(self_ip)]
	return np.std(lengths)

def server_num_full_pkts(lines):
	lengths = [0 for line in lines if int(line[6]) == 1514 and not line[2].startswith(self_ip)]
	return len(lengths)

def client_num_full_pkts(lines):
	lengths = [0 for line in lines if int(line[6]) == 1514 and line[2].startswith(self_ip)]
	return len(lengths)

def total_time(lines):
	return float(lines[-1][1])

def num_lag_periods(lines):
	count = 0
	for i in range(len(lines)-1):
		if float(lines[i+1][1]) - float(lines[i][1]) > 1:
			count += 1

	return count

"""
	Convert log file to features
"""
def log2feature(domain_dir, file):
	with open(domain_dir + '/' + file) as fp:
		lines = fp.readlines()

	# Parse into token lists
	lines = [[tok for tok in line.strip().split(" ") if tok != ""] for line in lines]

	# Filter out SSH packets
	lines = [line for line in lines if line[5] == 'SSH']

	features = {
		'client_num_packets': client_len(lines),
		'client_avg_pkt_len': client_avg_pkt_len(lines),
		'client_std_dev_pkt_len': client_std_dev_pkt_len(lines),
		'client_num_full_pkts': client_num_full_pkts(lines),
		'server_num_packets': server_len(lines),
		'server_avg_pkt_len': server_avg_pkt_len(lines),
		'server_std_dev_pkt_len': server_std_dev_pkt_len(lines),
		'server_num_full_pkts': server_num_full_pkts(lines),
		'total_time': total_time(lines),
		'num_lag_periods': num_lag_periods(lines)
	}

	return [
		features['client_num_packets'], 
		features['client_avg_pkt_len'], 
		features['client_std_dev_pkt_len'], 
		features['client_num_full_pkts'],
		features['server_num_packets'], 
		features['server_avg_pkt_len'], 
		features['server_std_dev_pkt_len'], 
		features['server_num_full_pkts'],
		features['total_time'],
		features['num_lag_periods']
	]

"""
	__main__
"""

dataset = []

# Iterate over all domain directories in DATA_PATH
for domain in tqdm(os.listdir(DATA_PATH)):
	domain_dir = DATA_PATH + domain
	if os.path.isdir(domain_dir):

		# Iterate over all traces for that domain
		for file in os.listdir(domain_dir):
			if os.path.isfile(domain_dir + '/' + file) and file != '0.trace':
				dataset.append( (log2feature(domain_dir, file), domain,) )

print "Wrote ", len(dataset), " data points!"

with open('dataset', 'w') as fp:
	np.save(fp, dataset)