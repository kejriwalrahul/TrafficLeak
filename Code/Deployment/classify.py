"""
	Program to classify collected traces to corresponding website

	Rahul Kejriwal
	CS14B023
"""

import cPickle

from ..Model_1.featurify import log2feature
from ..Model_2.compute_vectors import log2vector
from ..Model_2.train_model import my_kernel as model2_kernel
from ..Model_3.compute_vectors import log2vector as log2binvector
from ..Model_3.train_model import my_kernel as model3_kernel

"""
	Model Paths
"""
MODEL_1_PATH = "../Model_1/model_1.pkl"
MODEL_2_PATH = "../Model_2/model_2.pkl"
MODEL_3_PATH = "../Model_3/model_3.pkl"

# Load Model-1
with open(MODEL_1_PATH, "rb") as fp:
	model_1 = cPickle.load(fp)

# Load Model-2
with open(MODEL_2_PATH, "rb") as fp:
	model_2 = cPickle.load(fp)

# Load Model-3
with open(MODEL_3_PATH, "rb") as fp:
	model_3 = cPickle.load(fp)

print "hello"