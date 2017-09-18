#========================== import Module ==========================#

import collections
from collections import defaultdict
import argparse
import arff #https://pypi.python.org/pypi/liac-arff


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

def classify(raw_data, nd, nr, mother_dict = dict(), order=0):

	left, right = list(), list()
	parent, child, attr, sp = nr[order]

	if mother_dict['groups'] != {}:
		left, right = node['groups']
	del(node['groups'])

	for line in raw_data:
		if line[int(attr[-1])-1] <= sp :left.append(line)
		else :							 right.append(line)
		
			if parent=child-1 : classify(left, order=order+1)
			else: 				classify(right,order=order+1 )

	return {'groups': (left, right)}

def predict(one_line, node_relation_list):
	for parent, child, attr, sp in node_relation_list:
		node_relation_list.pop((parent, child, attr, sp))
		if one_line[int(attr[-1])-1] <= sp:
			predict(one_line, node_relation_list)
		else :
			predict(one_line, node_relation_list)
			
	return predict_class

if __name__ == "__main__":
	data = read_arff(args.test)
	node_collection, node_relation_list = read_model(args.train_model)
	print(node_collection, '\n\n', node_relation_list)
