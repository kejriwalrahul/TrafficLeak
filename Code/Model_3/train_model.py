"""
	Train SVM using Damerau-Levenshtein distance kernel

	Rahul Kejriwal
	CS14B023
"""

import cPickle
import numpy as np
import weighted_levenshtein as wl
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from tqdm import tqdm 


"""
	Used for padding request sequence so that sklearn doesnt complain
"""
FORBIDDEN_ELEMENT = 999


"""
	Parameters:
	
	IC,DC, SC, TC cost schemes
	SVM C
"""
cost_normalization_factor = 10


"""
	Cache distances
"""
stored_dists = {}


"""
	Normalize max length across train and test 
"""
max_len = 7500


"""
	Pads all sequences to same length using FORBIDDEN_ELEMENT to prevent sklearn cribs
"""
def pad_proper(X):
	# max_len = max([len(x) for x in X])

	new_X = []
	for x in X:
		new_X.append( x + [FORBIDDEN_ELEMENT]*(max_len-len(x)) )

	return new_X


"""
	Removes FORBIDDEN_ELEMENT from sequence for getting back actual sequence
"""
def trim_proper(vec):
	return [int(el) for el in vec if el != FORBIDDEN_ELEMENT]


"""
	Map numeric sequence to character sequence to use library for weighted-levenshtein
"""
def map_join(vector):
	string = ""

	for element in vector:
		if element == -1:
			string += chr(65)
		else:
			string += chr(66)

	return string


"""
	Kernel built from DL-distance metric
"""
def point_level_kernel_function(vec1, vec2, ic, dc, tc, sc):

	vec1 = trim_proper(vec1)
	vec2 = trim_proper(vec2)

	str1 = map_join(vec1)
	str2 = map_join(vec2)

	if (str1, str2) in stored_dists:
		return stored_dists[(str1, str2)]

	dist = wl.dam_lev(str1, str2, insert_costs=ic, delete_costs=dc, transpose_costs=tc, substitute_costs=sc) / (cost_normalization_factor*min(len(str1), len(str2)))
	fin_dist = np.exp([-dist**2])[0]

	stored_dists[(str1, str2)] = fin_dist
	stored_dists[(str2, str1)] = fin_dist

	return fin_dist


"""
	Compute kernel function for different pairs of instances
"""
def model3_kernel(X,Y):

	"""
		Build cost schemes for DL-distance
	"""
	ic = np.ones(128, dtype=np.float64)
	dc = np.ones(128, dtype=np.float64)
	tc = np.ones((128,128), dtype=np.float64)
	sc = np.ones((128,128), dtype=np.float64)

	for i in range(128):
		ic[i] = 20
		dc[i] = 20
		for j in range(128):
			# Alternative Schemes, choose one
			sc[i][j] = 30 + abs(i-j)
			# sc[i][j] = abs(i-j)
			# sc[i][j] = 20
			tc[i][j] = 1


	"""
		Compute actual kernel values
	"""
	gram_matrix = np.zeros((X.shape[0], Y.shape[0]))
	for i, x in tqdm(enumerate(X)):
		for j, y in enumerate(Y):
			gram_matrix[i, j] = point_level_kernel_function(x, y, ic, dc, tc, sc)

	return gram_matrix


"""
	__main__ Code
"""
if __name__ == '__main__':

	# Load Dataset
	dataset = np.load('dataset')
	np.random.shuffle(dataset)

	x_set = pad_proper([el[0] for el in dataset])
	y_set = [el[1] for el in dataset]

	# Train & Evaluate Model
	model = SVC(decision_function_shape='ovo', C=100, kernel=model3_kernel)
	scores = cross_val_score(model, x_set, y_set, cv=4)
	print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)

	# Train & Save Model
	model.fit(x_set, y_set)
	with open("model_3.pkl", "wb") as fp:
		cPickle.dump(model, fp)