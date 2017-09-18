#========================== import Module ==========================#

import collections
from collections import defaultdict
import argparse
import arff #https://pypi.python.org/pypi/liac-arff
import copy

import math
import numpy as np                        # np.log, np.log2
from scipy import stats
import pandas as pd

from draw_tree_v2 import *

import pickle
from sklearn.metrics import confusion_matrix #http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

#========================== import Module ==========================#


#========================== Get Arguments ==========================#

parser = argparse.ArgumentParser(description = "Implementing ID3 decision tree algorithm")
parser.add_argument("test",  type=str, help="input test.arff file" )
parser.add_argument("train_model", type=str, help="input tree.model" )
parser.add_argument("--prune", default = False , action = "store_true")

args = parser.parse_args()

#========================== Get Arguments ==========================#



#========================== Constant ==========================#
REMOVE_CALSS = 1
stamp = 0

#========================== Constant ==========================#



def read_arff(file_name):
	data = arff.load(open(file_name, 'r'))# 'rb' is read as binary
	data = data['data']
	#print(data[:10])
	return(data)

def read_model(train_model):
	with open(train_model, 'rb') as f:
	    # The protocol version used is detected automatically, so we do not
	    # have to specify it.
	    data = pickle.load(f)
	    node_collection, node_relation_list = data
	return node_collection, node_relation_list


if __name__ == "__main__":
	data = read_arff(args.test)
	node_collection, node_relation_list = read_model(args.train_model)
	print(node_collection, node_relation_list)
