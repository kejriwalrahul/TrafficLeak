"""
	Train some basic models using sklearn on ad-hoc featured data

	Rahul Kejriwal
"""

import numpy as np
from sklearn.model_selection import cross_val_score

# Load Dataset
dataset = np.load('dataset')
np.random.shuffle(dataset)

x = [el[0] for el in dataset]
y = [el[1] for el in dataset]

"""
	Logistic Regression

	Avg accuracy at C=0.2, ~67% [Toy Dataset]
	Avg accuracy at C=0.005, ~56% [Full Dataset]
"""

"""
from sklearn.linear_model import LogisticRegressionCV as LR

model = LR()
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores) 
"""

"""
	SVM

	[Toy Dataset]
	Linear ~70%, C=1
	Poly ~71%, C=1, degree=2
	RBF ~60%, C=100, gamma=0.0001

	[Full Dataset]
	Linear ~60%, C=100
	Poly ~59%, C=1, degree=2
	RBF ~56%, C=100, gamma=0.0000005
"""

"""
from sklearn.svm import SVC

model = SVC(decision_function_shape='ovo', C=1, kernel='poly', degree=2)
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	Decision Trees
	
	min_samples_leaf = 2, 65% [Toy Dataset]
	min_samples_leaf = 2, 47% [Full Dataset]
"""

"""
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(min_samples_leaf=3)
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	Random Forests

	77% accuracy at 15 estimators [Toy Dataset]
	67% accuracy at 20 estimators [Full Dataset]
"""

"""
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=20)
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	LDA

	59.5% [Full dataset]
"""

"""
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

model = LDA(solver='lsqr', shrinkage='auto')
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	k-NN

	57% [Full dataset]
"""

"""
from sklearn.neighbors import KNeighborsClassifier as knn

model = knn(n_neighbors=3, weights='distance', p=1)
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	ExtraTreesClassifier
	
	67% [Full dataset]
"""

"""
from sklearn.ensemble import ExtraTreesClassifier as ETC

model = ETC(n_estimators=30)
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	MLP Classifier

	38% [Full dataset]
"""

"""
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(hidden_layer_sizes=480, alpha=0.1)
scores = cross_val_score(model, x, y, cv=4)
print "Cross Val Avg Accuracy: ", sum(scores) / len(scores)
"""

"""
	Save Model
"""

import cPickle

with open("model_1.pkl", "wb") as fp:
	cPickle.dump(model, fp)