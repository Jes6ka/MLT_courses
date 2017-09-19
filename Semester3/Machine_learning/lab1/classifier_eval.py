#========================== import Module ==========================#

import collections
from collections import defaultdict
import argparse
import arff #https://pypi.python.org/pypi/liac-arff


from draw_tree_v2 import *

import pickle
from sklearn.metrics import confusion_matrix #http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
# from pandas_ml import ConfusionMatrix
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
predicted_class = list()
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

def predict(one_line, node_relation_list, node_collection, flag=0):
	global 	predicted_class
	parent, child, attr, sp = node_relation_list[flag]

	if node_collection[flag][1] == "terminal" :
		#print("reached the terminal\n", node_collection[flag][0][0], '\n\n')
		predicted_class.append(node_collection[flag][0][0])
		return node_collection[flag][0][0]

	if one_line[int(attr[-1])-1] <= sp:	#if it's small
		#print("-----flag@@-----",flag, parent, child, attr, sp)
		predict(one_line, node_relation_list, node_collection, flag=child)
	else :							#if it's big
		#print("-----flag-----",flag, parent, child, attr, sp)
		for parent_, child_, attr_, sp_ in node_relation_list[flag+1:]:
			if parent == parent_ :
				#print("-----flag-$$$---",flag, parent_, child_, attr_, sp_, len(node_relation_list))
				if child_ == len(node_relation_list) :
					predicted_class.append(node_collection[child_][0][0])
					pass
				else : predict(one_line, node_relation_list, node_collection, flag=child_)

def classifer(raw_data, node_relation_list, node_collection):
	global 	predicted_class
	for line in raw_data:
		predict(line, node_relation_list, node_collection)
		#print("succeful", len(predicted_class), predicted_class)
	return None

def evaluation(raw_data, predicted_class):
	y_true = [l[-1] for l in raw_data]
	y_pred = predicted_class
	print("true, pred lengths are ",len(y_true), len(y_pred))
	conf_matrx= confusion_matrix(y_true, y_pred)
	#tn, fp, fn, tp = conf_matrx.ravel()
	# conf_matrx = ConfusionMatrix(y_true, y_pred)
	# conf_matrx.print_stats()
	print(conf_matrx)
	#print("total precision : " (tn+tp)/(tn+tp+fn+fp))
	return None


if __name__ == "__main__":
	data = read_arff(args.test)
	node_collection, node_relation_list = read_model(args.train_model)
	print(node_collection, '\n\n', node_relation_list)
	classifer(data, node_relation_list, node_collection)
	print('heyhey \n',predicted_class[:20])
	conf_matrx = evaluation(data, predicted_class)



# >>> def t(a,b,c,d):
# 	return (a+d)/(a+b+d+c)
# >>> t(527,222,206,164)
# 0.6175156389633601
# >>> t(616,133,231,139)
# 0.6747095621090259
# >>> t(666,83,320,50)
# 0.6398570151921358

#python classifer_eval.py exp2_test.arff exp1_train.model
