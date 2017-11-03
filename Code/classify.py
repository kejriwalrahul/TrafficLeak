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

DATA_PATH = "Deployment/Test_Data/"

"""
	Load Models
"""

MODEL_1_PATH = "Model_1/model_1.pkl"
MODEL_2_PATH = "Model_2/model_2.pkl"
MODEL_3_PATH = "Model_3/model_3.pkl"

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

y_pred = model_1.predict(x_set)

with open("model_1_results", 'w') as fp:
	fp.write("Model-1 Results: \n")
	for i, url in enumerate(y_set):
		fp.write("Actual: " + url + "\n")
		fp.write("Model-1: " + y_pred[i] + "\n\n")

	fp.write("Accuracy: " + str(accuracy_score(y_set, y_pred)))


"""
	Model-2: Read dataset & predict
"""

x_set = []
y_set = []

for trace in os.listdir(DATA_PATH):
	y_set.append(trace.split('.trace')[0])
	x_set.append(log2vector(DATA_PATH, trace))

x_set = pad_proper(x_set)
y_pred = model_2.predict(x_set)

with open("model_2_results", 'w') as fp:
	fp.write("Model-2 Results: \n")
	for i, url in enumerate(y_set):
		fp.write("Actual: " + url + "\n")
		fp.write("Model-2: " + y_pred[i] + "\n\n")

	fp.write("Accuracy: " + str(accuracy_score(y_set, y_pred)))


"""
	Model-3: Read dataset & predict
"""

x_set = []
y_set = []

for trace in os.listdir(DATA_PATH):
	y_set.append(trace.split('.trace')[0])
	x_set.append(log2binvector(DATA_PATH, trace))

x_set = pad_proper(x_set)
y_pred = model_3.predict(x_set)

with open("model_3_results", 'w') as fp:
	fp.write("Model-3 Results: \n")
	for i, url in enumerate(y_set):
		fp.write("Actual: " + url + "\n")
		fp.write("Model-3: " + y_pred[i] + "\n\n")

	fp.write("Accuracy: " + str(accuracy_score(y_set, y_pred)))
