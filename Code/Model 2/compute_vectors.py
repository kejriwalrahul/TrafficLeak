"""
	Parses network logs to create vector representations amenable for Damerau-Levenshtein distance computation

	Rahul Kejriwal
	CS14B023
"""

import os
import numpy as np

from tqdm import tqdm

# Config vars
DATA_PATH = "../../Datasets/Full Dataset/"
self_ip = '192.168.1.'
discrete_levels = 8

max_pkt_size = 1514

def discretify(line):
	for i in range(1, discrete_levels+1):
		if int(line[6]) < (max_pkt_size / discrete_levels) * i:
			return -i if line[2].startswith(self_ip) else i

	return -i if line[2].startswith(self_ip) else i

def log2vector(domain_dir, file):
	with open(domain_dir + '/' + file) as fp:
		lines = fp.readlines()

	# Parse into token lists
	lines = [[tok for tok in line.strip().split(" ") if tok != ""] for line in lines]

	# Filter out SSH packets
	lines = [line for line in lines if line[5] == 'SSH']

	# Discretize pkt size and direction
	vector = [discretify(line) for line in lines]

	return vector

"""
	__main__
"""

vectors = []

# Iterate over all domain directories in DATA_PATH
for domain in tqdm(os.listdir(DATA_PATH)):
	domain_dir = DATA_PATH + domain
	if os.path.isdir(domain_dir):

		# Iterate over all traces for that domain
		for file in os.listdir(domain_dir):
			if os.path.isfile(domain_dir + '/' + file) and file != '0.trace':
				vectors.append( (log2vector(domain_dir, file), domain,) )

print "Wrote ", len(vectors), " data points!"

with open('dataset', 'w') as fp:
	np.save(fp, vectors)