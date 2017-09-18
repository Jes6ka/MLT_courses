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
#========================== import Module ==========================#


#========================== Get Arguments ==========================#

parser = argparse.ArgumentParser(description = "Implementing ID3 decision tree algorithm")
parser.add_argument("train",  type=str, help="input train.arff file" )
parser.add_argument("tree", type=str, help="input tree.model" )
parser.add_argument("--prune", default = False , action = "store_true")

args = parser.parse_args()

#========================== Get Arguments ==========================#




#========================== Constant ==========================#
REMOVE_CALSS = 1
stamp = -1
g_attr, g_sp, g_sp_v, g_IG = str(), str(), int(), int()
node_collection = list()
terminal_collection = list()
#========================== Constant ==========================#







def read_arff(file_name):
	data = arff.load(open(file_name, 'r'))# 'rb' is read as binary
	data = data['data']
	#print(data[:10])
	return(data)

def make_attr_values_dict(raw_data):
	""" This is used for making attr_sp_dict, when making split points."""
	attr_values_dict = defaultdict(list)
	for line in raw_data:	#line is [sunny, 85, 53, 2, class1]
		for n, attr_value in enumerate(line[:-REMOVE_CALSS]):
			attr_values_dict['attr'+str(n+1)].append(attr_value)

	return attr_values_dict 			#looks like, {attr1: [22,24,21,23,...], attr2: [1,2,1,1,...]}

def make_attr_sp_dict(raw_data):
	attr_sp_dict = defaultdict(list)

	attr_values_dict = make_attr_values_dict(raw_data) 				#{attr1: [22,24,21,23,...], attr2: [1,2,1,1,...]}
	for n in range(len(attr_values_dict)): #len(attr_values_dict) is number of attributes.
			avd = attr_values_dict['attr'+str(n+1)]
			median  = np.median(avd)
			tm  = stats.trim_mean(avd, 0.05)
			sd  = np.std(avd, ddof=1)

			for i in range(10):
				attr_sp_dict['attr'+str(n+1)].append(tm-0.3*i*sd)
				attr_sp_dict['attr'+str(n+1)].append(tm+0.3*i*sd)
				# attr_sp_dict_global['attr'+str(n+1)]['sp'+str(i+1)]=(tm-0.3*i*sd)
				# attr_sp_dict_global['attr'+str(n+1)]['sp'+str(i+11)]=(tm-0.3*i*sd)
	
	#print('0000000000	', attr_sp_dict)
	return attr_sp_dict		
	#attr_sp_dict = {attr1 : [0.2, 0.4, ...sp9]}, attr2 : [sp1,sp2..sp9]
	#attr_sp_dict_global = {attr1 : {sp1 : 0.2, sp2: 0.4...}}


def calc_best_gain(raw_data):
	"""
	raw_data
	[	[attr1, attr2, attr3 ,.... class]
		[attr1, attr2, attr3 ,.... class]
		[attr1, attr2, attr3 ,.... class] 	]


	return
	candidate_group_dict  : {attr1 : { sp1 : {small : [raw_data_line1, raw_data_line3...], 
												big : [raw_data_line2, raw_data_line5...]}
							attr2 : { sp2 : {small :  ...}
	"""
	attr_sp_dict = make_attr_sp_dict(raw_data)
	#attr_sp_dict 	: {attr1 : [sp1, sp2, ...sp9]}, attr2 : [sp1,sp2..sp9]}

	class_freq = collections.Counter([line[-1] for line in raw_data])
	classes = set(class_freq)

	small = list()
	big   = list()
	sp_small_freq = list()
	sp_big_freq   = list()
	each_split_freq = defaultdict(dict)
	IG_list = list()

	for attr in attr_sp_dict:
		for sp in attr_sp_dict[attr]:
			for line in raw_data:
				#print('-------',int(attr[-1])-1, attr, sp,  line[int(attr[-1])-1] )
				if line[int(attr[-1])-1] <= sp : small.append(line[-1]) # save class
				else :					 big.append(line[-1])
			sp_small_freq = dict(collections.Counter(small)) 		# {austen : 1232, milton : 232, kate : 98...}
			sp_big_freq = dict(collections.Counter(big))			# {austen : 332, milton : 622}
			merged_freq = merge_dicts(sp_small_freq, sp_big_freq) 	#  {austen : [1232, 332], milton : [232, 622]}
			try :
				each_IG = gain_calculate(merged_freq)
				IG_list.append((attr, sp, each_IG))
			except : pass
			

	#print(IG_list)
	if IG_list == []:
		return (False,False,False)

	best_gain = max(IG_list, key=lambda x : x[-1])
	print('best gain is ', best_gain)

	return best_gain			#looks like, {attr1 : { sp1 : {small : [(value, austen, line0), (v,c,l)...], big : [(value, austen, line)]}



def merge_dicts(dict1, dict2):
	merged_dict = defaultdict(list)
	for d in (dict1, dict2):
		for key, value in d.items():
			merged_dict[key].append(value)
	return merged_dict


def entropy(p_list):
	return(-sum([p*np.log2(p) for p in p_list]))

												  #small, big 			small, big
def gain_calculate(merged_freq_dict): # {austen : [1232, 332], milton : [232, 622]}
	"""
	IG = TOTAL_entropy - (small/TOTAL)*entropy(class_by_small) -(big/TOTAL)*entropy(class_by_big)
	"""
	TOTAL = sum([i for a in merged_freq_dict.values() for i in a])
	each_small_big = [i for i in merged_freq_dict.values()];
	TOTAL_class = [sum(i) for i in each_small_big] 		#[982, 512, 1102(small+big in one class),...]
	TOTAL_entropy_in = [each/sum(TOTAL_class) for each in TOTAL_class]
	TOTAL_entropy    = entropy(TOTAL_entropy_in)
	small_TOTAL 	 = sum([ i[0] for i in each_small_big])/TOTAL
	big_TOTAL 		 = sum([ i[1] for i in each_small_big])/TOTAL

	class_by_small, class_by_big = list(), list()
	for c in merged_freq_dict:
		class_by_small.append(merged_freq_dict[c][0])
		class_by_big.append(merged_freq_dict[c][1])
	
	prob_class_by_small = [e/sum(class_by_small) for e in class_by_small]
	prob_class_by_big = [e/sum(class_by_big) for e in class_by_big]

	IG = TOTAL_entropy - (small_TOTAL)*entropy(prob_class_by_small) -(big_TOTAL)*entropy(prob_class_by_big)
	#print('head entropy is',entropy(total_small/total_big))
	#print('IG is',IG)
	if math.isnan(IG):
		#print('this is nan')
		return(-5000) #jsut random minus value.
	else :	return(round(IG,5))



def node_split(raw_data):
	global stamp, node_collection
	attr, sp, IG = calc_best_gain(raw_data)
	if attr==False and sp==False and IG==False : return
	left, right = list(), list()
	for line in raw_data:
		if line[int(attr[-1])-1] < sp: #get indx_of_attr
			left.append(line)
		else :
			right.append(line)

	status = dict(collections.Counter([line[-1] for line in raw_data]))
	node_collection.append((attr, sp, IG, stamp+1, status))

	print("----one node split is succussful----")
	return {'IG' : IG ,'groups': (left, right), 'status' : status, 'index' : attr, 'split_point' : sp, 'stamp' : stamp}


def to_terminal(group):
	global stamp, node_collection, terminal_collection
	stamp+=1
	#if not node_colletor : node_collection.append((attr, sp, sp_v, stamp+1))
	outcomes = collections.Counter([row[-1] for row in group])
	node_collection.append(('terminal', 'terminal', -7777, stamp, outcomes))
	terminal_collection.append(group)
	print("-=-=-=-to_terminal-=-=-=-=location: ", len(node_collection), 'node order', stamp)
	#print(outcomes, max(outcomes, key=outcomes.count))
	return {'most_common' : ( outcomes.most_common(), outcomes ), 'stamp' : stamp}

def recursive_split(node, max_depth, min_size=10, depth=1, off_set_percent=5):
	global stamp
	#print('this is groups   ',node['groups'])
	if node['groups']:
		left, right = node['groups']
	else : return

	stamp+=1
	node['stamp'] = stamp
	#stamp+=1
	#print("Left ===========",left[:5])
	del(node['groups'])
	# check for a no split
	if not node['IG']:
		node['left'] = node['right'] = to_terminal(left + right)
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	# process left child
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = node_split(left)
		recursive_split(node['left'], max_depth, depth=depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = node_split(right)
		recursive_split(node['right'], max_depth, depth=depth+1)


	# node['left'] = node_split(left)
	# recursive_split(node['left'], max_depth, )
	
	# # process right child
	# node['right'] = node_split(right)
	# recursive_split(node['right'], max_depth, depth=depth+1)

if __name__ == "__main__":
	data = read_arff(args.train)
	root = node_split(data) # attr, sp, each_IG
	recursive_split(root, 5)
	print(node_collection)
	make_tree(node_collection)
	draw_tree_graphviz(node_relation_list)
