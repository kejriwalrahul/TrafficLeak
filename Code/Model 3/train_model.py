"""
	Train SVM using Damerau-Levenshtein distance kernel

	Rahul Kejriwal
"""

import numpy as np
import weighted_levenshtein as wl
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from tqdm import tqdm 

"""
	Parameters
"""
cost_normalization_factor = 10

# IC,DC, SC, TC cost schemes
# SVM C

stored_dists = {}

def map_join(vector):
	string = ""

	for element in vector:
		if element == -1:
			string += chr(65)
		else:
			string += chr(66)

	return string

def point_level_kernel_function(vec1, vec2, ic, dc, tc, sc):
	if (vec1[0], vec2[0]) in stored_dists:
		return stored_dists[(vec1[0], vec2[0])]

	str1 = map_join(x_set[int(vec1[0])])
	str2 = map_join(x_set[int(vec2[0])])
	dist = wl.dam_lev(str1, str2, insert_costs=ic, delete_costs=dc, transpose_costs=tc, substitute_costs=sc) / (cost_normalization_factor*min(len(str1), len(str2)))
	fin_dist = np.exp([-dist**2])[0]

	stored_dists[(vec1[0], vec2[0])] = fin_dist
	stored_dists[(vec2[0], vec1[0])] = fin_dist

	return fin_dist

def my_kernel(X,Y):

	ic = np.ones(128, dtype=np.float64)
	dc = np.ones(128, dtype=np.float64)
	tc = np.ones((128,128), dtype=np.float64)
	sc = np.ones((128,128), dtype=np.float64)

	for i in range(128):
		ic[i] = 20
		dc[i] = 20
		for j in range(128):
			sc[i][j] = 30 + abs(i-j)
			# sc[i][j] = abs(i-j)
			# sc[i][j] = 20
			tc[i][j] = 1

	gram_matrix = np.zeros((X.shape[0], Y.shape[0]))
	for i, x in tqdm(enumerate(X)):
		for j, y in enumerate(Y):
			gram_matrix[i, j] = point_level_kernel_function(x, y, ic, dc, tc, sc)

	return gram_matrix

if __name__ == '__main__':

	# Load Dataset
	dataset = np.load('dataset')
	np.random.shuffle(dataset)

	global x_set
	x_set = [el[0] for el in dataset]
	x_ptrs = [[i] for i in range(len(x_set))]
	y_set = [el[1] for el in dataset]

	model = SVC(decision_function_shape='ovo', C=100, kernel=my_kernel)
	scores = cross_val_score(model, x_ptrs, y_set, cv=4)
	print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)