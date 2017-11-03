"""
	Program to classify collected traces to corresponding website

	Rahul Kejriwal
	CS14B023
"""

import cPickle
import os
import builtins

from Model_1.featurify import log2feature
from Model_2.compute_vectors import log2vector
from Model_2.train_model import model2_kernel, pad_proper
from Model_3.compute_vectors import log2vector as log2binvector
from Model_3.train_model import model3_kernel

from sklearn.metrics import accuracy_score


"""
	Relaxed classification factor
"""
RELAXATION_FACTOR = 5


"""
	PATHS
"""

MODEL_1_PATH = "Model_1/model_1.pkl"
MODEL_2_PATH = "Model_2/model_2.pkl"
MODEL_3_PATH = "Model_3/model_3.pkl"

DATA_PATH = "Deployment/Test_Data/"


"""
	Write report to file
"""
def write_report(y_pred, y_set, model_i, model):
	y_fin_pred = []
	relaxed_count = 0

	with open("model_" + str(model_i) + "_results", 'w') as fp:
		for i, url in enumerate(y_set):
			fp.write("Actual: " + url + "\n")
			fp.write("Model-" + str(model_i) + ": \n")

			# Sort predicted classes by probability
			curr_res = sorted(enumerate(y_pred[i]), key=lambda x:-float(x[1]))
			
			# Print top picks
			for i in range(RELAXATION_FACTOR):
				fp.write("\t" + model.classes_[curr_res[i][0]] + "\n")

			fp.write("\n")
			
			# Update normal count
			y_fin_pred.append(model.classes_[curr_res[0][0]])
			
			# Update relaxed count
			if url in [model.classes_[curr_res[i][0]] for i in range(RELAXATION_FACTOR)]:
				relaxed_count += 1

		# Print accuracies
		fp.write("Accuracy: " + str(100 * accuracy_score(y_set, y_fin_pred)) + "\n")
		fp.write("Relaxed Accuracy: " + str(relaxed_count*100.0 / len(y_set)))


"""
	__main__ Code
"""


"""
	Load Models
"""

# Load Model-1
with open(MODEL_1_PATH, "rb") as fp:
	model_1 = cPickle.load(fp)

# Load Model-2
with open(MODEL_2_PATH, "rb") as fp:
	model_2 = cPickle.load(fp)

# Load Model-3
with open(MODEL_3_PATH, "rb") as fp:
	model_3 = cPickle.load(fp)


"""
	Model-1: Read dataset & predict
"""

x_set = []
y_set = []

for trace in os.listdir(DATA_PATH):
	y_set.append(trace.split('.trace')[0])
	x_set.append(log2feature(DATA_PATH, trace))

y_pred = model_1.predict_proba(x_set)
write_report(y_pred, y_set, 1, model_1)


"""
	Model-2: Read dataset & predict
"""

x_set = []
y_set = []

for trace in os.listdir(DATA_PATH):
	y_set.append(trace.split('.trace')[0])
	x_set.append(log2vector(DATA_PATH, trace))

x_set = pad_proper(x_set)
y_pred = model_2.predict_proba(x_set)
write_report(y_pred, y_set, 2, model_2)


"""
	Model-3: Read dataset & predict
"""

x_set = []
y_set = []

for trace in os.listdir(DATA_PATH):
	y_set.append(trace.split('.trace')[0])
	x_set.append(log2binvector(DATA_PATH, trace))

x_set = pad_proper(x_set)
y_pred = model_3.predict_proba(x_set)
write_report(y_pred, y_set, 3, model_3)