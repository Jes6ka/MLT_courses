# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.



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

#scikit-learn
from sklearn.metrics import confusion_matrix #http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

#========================== import Module ==========================#





#========================== Get Arguments ==========================#

parser = argparse.ArgumentParser(description = "Implementing ID3 decision tree algorithm")
parser.add_argument("train",  type=str, help="input train.arff file" )
parser.add_argument("tree", type=str, help="input tree.model" )
parser.add_argument("--prune", default = False , action = "store_true")

args = parser.parse_args()
#========================== Get Arguments ==========================#



#========================== Constant ==========================#
# tag - start symbol 
start_symbol = "start"
REMOVE_CALSS = 1
# For buckets, split point
LOW  = 10
MID  = 20
HIGH = 50
data = None
nan = float('nan')
node_collection = list()
t1,t2,t3 = 0,0,-1
#========================== Constant ==========================#




#==========================      MAIN_START    ==========================#
#==========================      MAIN_START    ==========================#

def read_arff(file_name):
	global data
	data = arff.load(open(file_name, 'r'))# 'rb' is read as binary
	data = data['data']
	#print(data[:10])
	return(None)

"""
arff looks like, aka, the above data looks like
>>> data
{
    u'attributes': [
        (u'outlook', [u'sunny', u'overcast', u'rainy']),
        (u'temperature', u'REAL'),
        (u'humidity', u'REAL'),

    u'data': [
        [u'sunny', 85.0, 85.0, u'FALSE', u'no'],
        [u'sunny', 80.0, 90.0, u'TRUE', u'no'],
        [u'overcast', 83.0, 86.0, u'FALSE', u'yes'],
        [u'rainy', 70.0, 96.0, u'FALSE', u'yes'],
        ....
    ],
}
"""

def make_attr_values_dict(raw_data):
	""" This is used for making attr_sp_dict, when making split points."""
	attr_values_dict = defaultdict(list)
	for line in raw_data:	#line is [sunny, 85, 53, 2, class1]
		for n, attr_value in enumerate(line[:-REMOVE_CALSS]):
			attr_values_dict['attr'+str(n+1)].append(attr_value)
	#print(attr_values_dict.keys(), attr_values_dict['attr1'][:20])
	# test1 = attr_values_dict['attr2']
	# test2 = stats.trimboth(test1, 0.1)
	
	# print('\n\n', max(test1),	'\n',
	# 			  min(test1),	'\n',
	# 			  np.median(test1),'\n',
	# 			  np.mean(test1),  '\n',
	# 			  stats.trim_mean(test1, 0.10),  '\n',
	# 			  np.std(test1, ddof=1),'\n',
	# 			  stats.kurtosis(test1),'\n',
	# 			  stats.skew(test1),'\n',
	# 			  stats.mode(test1),'\n---------\n',

	# 			  max(test2),	'\n',
	# 			  min(test2),	'\n',
	# 			  np.median(test2),'\n',
	# 			  np.mean(test2),  '\n',
	# 			  stats.trim_mean(test2, 0.10),  '\n',
	# 			  np.sqrt(np.std(test2, ddof=1)),'\n',
	# 			  #np.log(np.std(test2, ddof=1)),'\n',
	# 			  stats.kurtosis(test2),'\n',
	# 			  stats.skew(test2),'\n',
	# 			  stats.mode(test2),'\n---------\n',
	# 			  )
	return attr_values_dict 			#looks like, {attr1: [22,24,21,23,...], attr2: [1,2,1,1,...]}
	#works well.

def make_attr_class_dict(raw_data):
	attr_class_dict = defaultdict(list)
	for line in raw_data:		#line is [sunny, 85, 53, 2, class1]
		for n, attr_value in enumerate(line[:-REMOVE_CALSS]):
			attr_class_dict['attr'+str(n+1)].append((attr_value, line[-1])) #line[-1] is class( author.txt)
	
	#print(attr_class_dict.keys(), attr_class_dict['attr1'][:10])
	return attr_class_dict 				#looks like, {attr1: [(22, austen), (13, milton)], attr2 : [(1, austen), (1.3, austen)]}

def make_attr_sp_dict(raw_data):
	"""Most import part
			I'm gonna use, median, std.
			total 6std coveres more than 99.7%
			from median(M), I will use [M-3sd, M-2sd, M-sd, M-0.5sd, M, M+0.5sd, M+sd, M+2sd, M+3sd]
			So, total spliting point will be nine.
	"""
	attr_sp_dict_global = defaultdict(dict)
	attr_sp_dict = defaultdict(list)

	attr_values_dict = make_attr_values_dict(raw_data) 				#{attr1: [22,24,21,23,...], attr2: [1,2,1,1,...]}
	
	for n in range(len(attr_values_dict)): #len(attr_values_dict) is number of attributes.
			avd = attr_values_dict['attr'+str(n+1)]
			median  = np.median(avd)
			tm  = stats.trim_mean(avd, 0.05)
			sd  = np.std(avd, ddof=1)
			#attr_sp_dict['attr'+str(n+1)].append(stats.mode(avd))  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median-1*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median-0.5*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median-0*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median+0.5*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median+1*sd)  #line[-1] is class( author.txt)
	
			attr_sp_dict_global['attr'+str(n+1)]['sp1']=(median-1*sd)  #line[-1] is class( author.txt)
			attr_sp_dict_global['attr'+str(n+1)]['sp2']=(median-0.5*sd)  #line[-1] is class( author.txt)
			attr_sp_dict_global['attr'+str(n+1)]['sp3']=(median-0*sd)  #line[-1] is class( author.txt)
			attr_sp_dict_global['attr'+str(n+1)]['sp4']=(median+0.5*sd)  #line[-1] is class( author.txt)
			attr_sp_dict_global['attr'+str(n+1)]['sp5']=(median+1*sd)  #line[-1] is class( author.txt)

	#print('\n\n',attr_sp_dict)
	return attr_sp_dict, attr_sp_dict_global		
	#attr_sp_dict = {attr1 : [0.2, 0.4, ...sp9]}, attr2 : [sp1,sp2..sp9]
	#attr_sp_dict_global = {attr1 : {sp1 : 0.2, sp2: 0.4...}}

def split_small_big(attr_class_dict, attr_sp_dict):
	"""
	attr_class_dict : {attr1: [(22, austen), (13, milton)], attr2 : [(1, austen), (1.3, austen)]}
	attr_sp_dict 	: {attr1 : [sp1, sp2, ...sp9]}, attr2 : [sp1,sp2..sp9]}

	return
	candidate_group_dict  : {attr1 : { sp1 : {small : [(value, austen, line0), (v,c,l)...], 
												big : [(value, austen, line)]}
							attr2 : { sp2 : {small :  ...}
	"""
	classes_dict = {}
	for v, c in attr_class_dict['attr1']:
		classes_dict[c]=[] 	# num_classes = {austen : [], milton : [] ...}

	candidate_group_dict = {}


	for attr in attr_sp_dict:
		candidate_group_dict[attr] = defaultdict(dict)
		
		for m, sp in enumerate(attr_sp_dict[attr]): 	# first : attr1.sp1
			split_small_big_dict = defaultdict(list)

			for n, (v, c) in enumerate(attr_class_dict[attr]): # value, class : (22, austen)
				#I need,  attr1 = [22,austen, Small], [43,milton, Big], ...
				# split to two part,  attr1.small = [(22,austen, line1), ...], attr1.big = [(43,milton, line2)]
				#print('\n======================\n', n, v, sp)
				if split_small_big_dict == defaultdict(list): 		#This is for smoothing. for line around #222
					split_small_big_dict['small'].append(('value', c, -1))
					split_small_big_dict['big'].append(('value', c, -1))

				if v <= sp : split_small_big_dict['small'].append((v, c, n))
				else : split_small_big_dict['big'].append((v, c, n))
				#@TODO : get gain from split two lists by using classes.
				#get_gain(split_small_big_dict)
			candidate_group_dict[attr]['sp'+str(m+1)] = split_small_big_dict
			
			#print('this is sp ==========', sp)
			#print('\n======================\n',len(candidate_group_dict[attr]['sp'+str(n+1)]['small']))


	return candidate_group_dict			#looks like, {attr1 : { sp1 : {small : [(value, austen, line0), (v,c,l)...], big : [(value, austen, line)]}
										# 			  attr2 : { sp2 : {small :  ...}

	#return attr_gain_dict			#looks like, {attr1_gain : [.5, .4, ..., .7]}, attr2_gain : [0.2, 0.3, ...]



def fitting_data(candidate_group_dict):
	"""
	candidate_group_dict  : {attr1 : { sp1 : {small : [(value, austen, line0), (v,c,l)...], 
												big : [(value, austen, line)]}
							attr2 : { sp2 : {small :  ...}
	return
	fit_data_dict = {'attr1': 
					{'sp1': 
						{'austen': {'small': 23, 'big': 402},
						'milton': {'small': 52, 'big': 387}   }
		}
	"""
	cgd = copy.deepcopy(candidate_group_dict)
	#temp2 = []
	temp3 = []
	fit_data_dict = {}

	#get class list, e.g., austen, milton, ...
	class_list = []
	for sp in cgd['attr1']:
		class_list = list(set([c for small_or_big in cgd['attr1'][sp] for v, c, l in cgd['attr1'][sp][small_or_big]]))
	
	for attr in cgd:
		fit_data_dict[attr]={}
		for sp in cgd[attr]:
			#print('=========calc gain ===========',cgd[attr].keys())
			#print('=========calc gain ===========',sp)
			fit_data_dict[attr][sp]={}
			
			for small_or_big in cgd[attr][sp]:
				temp1 = []
				#print('=========calc gain ===========',small_or_big)
				
				for v,c,l in cgd[attr][sp][small_or_big]:
					temp1.append(c)
					#temp2.append((c,l))
				freq_groupy_by_class = dict(collections.Counter(temp1+class_list))# smoothing. by plus class_list, removing zero value.
				#freq_groupy_by_class = {austen : 2342, milto : 1123}

				for class_ in freq_groupy_by_class:
					#print(attr, sp, class_, small_or_big, freq_groupy_by_class, freq_groupy_by_class[class_])
					try : fit_data_dict[attr][sp][class_][small_or_big] = freq_groupy_by_class[class_]
					except: 
						fit_data_dict[attr][sp][class_] = {}
						fit_data_dict[attr][sp][class_][small_or_big] = freq_groupy_by_class[class_]

				temp3.append( (attr, sp, small_or_big, freq_groupy_by_class )   ) 
	
	#temp3 = [(attr1, sp1, big, {austen : 2996, milton : 1479}), (attr1, sp2, small, {austen : 232, milton : 4053}) ]
	#print('\n=========calc gain ===========',fit_data_dict , '\n')
    #Now, let's calculate GAIN
		#        two split raw_data 1 									split raw_data 2
      	#[u'sunny', 85.0, 85.0, u'FALSE', u'no'],   	[u'sunny', 85.0, 85.0, u'FALSE', u'no'],
        #[u'sunny', 80.0, 90.0, u'TRUE', u'no'],		[u'sunny', 85.0, 85.0, u'FALSE', u'no'],
	return fit_data_dict


def entropy(p):
	calc = p*np.log2(p)+(1-p)*np.log2(1-p)
	return(-calc)

def gain_calculate(sob_group_by_class_list): # [(23, 402), (52, 387), ... (author_n_small, author_n_big)]
	"""
	milton : 1479	austen : 2998
	case for Attr1, sp3
	Small 	= 		M : 466		A : 1776
	Big 	= 		M : 1015	A : 1224

	1.Entropy(M.small+A.small/M.small+M.big+A.small+A.big) = entropy(2242/4481) = 0.999
	2.Entropy(M.small/M.small + M.big) = entropy(466/1481) = 0.898
	3.Entropy(A.small/A.small+A.big) = entropy(1775/3000) = 0.976

	Gain = 1-(2+3) = 0.999-(0.898+0.976) = -0.875
	"""
	#print('========CHECK=========', sob_group_by_class_list)
	total_small = 0
	total_big 	= 0
	sum_each_prob_entropy = 0

	for small_v, big_v in sob_group_by_class_list:
		if small_v <= 2 or big_v <=2 : 
			total_small, total_big, sum_each_prob_entropy = 2,1,99
			continue
		if small_v <= big_v:
			#print('===s,b,entrop1===', small_v, big_v, entropy(small_v/(small_v+big_v)))
			sum_each_prob_entropy += entropy(small_v/(small_v+big_v))
			total_small += small_v
			total_big 	+= big_v
		else : 
			#print('===s,b,entrop2===', small_v, big_v, entropy(big_v/(small_v+big_v)))
			sum_each_prob_entropy += entropy(big_v/(small_v+big_v))
			total_small += big_v
			total_big 	+= small_v

	#Now, calculate real IG(Information Gain)
	
	IG = entropy(total_small/total_big)- sum_each_prob_entropy
	#print('head entropy is',entropy(total_small/total_big))
	#print('IG is',IG)
	if math.isnan(IG):
		#print('this is nan')
		return(-5000)
	else :	return(IG)


def choose_best_gain(fit_data_dict, attr_sp_dict_global):
	"""
	fit_data_dict :	fit_data_dict
	[{'austen': {'small': 23, 'big': 402}, 
	 'milton': {'small': 52, 'big': 387},
	  other_author : {small...			}	}    ]

	return
	each_gain = -0.87
	"""
	gain_list = []
	
	for attr in fit_data_dict:
		for sp in fit_data_dict[attr]:
			sob_group_by_class_list = [] #small or big by class count list. 
			for c in fit_data_dict[attr][sp]:
				sob_group_by_class_list.append(tuple(fit_data_dict[attr][sp][c].values()))
				#sob_group_by_class_list : [(23, 402), (52, 387), ... (author_n_small, author_n_big)]
			
			#each_gain_list : [(att1, sp1, 0.22), (attr1, sp2, 0.01) ...]
			gain_list.append( (attr, sp, attr_sp_dict_global[attr][sp], gain_calculate(sob_group_by_class_list)  )     )           
	

	best_gain = max(gain_list, key=lambda x : x[-1]) #find max vaule-key is gain.
	print('\n This is best gain', best_gain)
	#print('This is all_gain : ', gain_list, '\n This is best gain', best_gain)
	#print('This is sp_dict : ', attr_sp_dict_global['attr2'], '\n This is best gain', best_gain)

	return best_gain

def test_split(index_attr, value_split_point, raw_data):
    left, right = list(), list()
    for row in raw_data:
        if row[int(index_attr[-1])-1] < value_split_point: #get indx_of_attr
            left.append(row)
        else :
            right.append(row)
    return left, right

def split_in_all_in_one(raw_data):
	global node_collection
	b_index, b_value, b_score, b_groups = 2, 99999, 7777, None

	attr_class_dict 					= make_attr_class_dict(raw_data)
	attr_sp_dict, attr_sp_dict_global	= make_attr_sp_dict(raw_data)
	candidate_group_dict				= split_small_big(attr_class_dict, attr_sp_dict)
	fit_data_dict						= fitting_data(candidate_group_dict)
	attr, sp, sp_v, IG = choose_best_gain(fit_data_dict, attr_sp_dict_global)

	left_right_groups = test_split(attr, sp_v, raw_data)
	node_collection.append((attr, sp, sp_v, t3+1))
	print("all in one split is succussful")
	return {'index':attr, 'value':sp_v, 'groups':left_right_groups, 'stamp' : 0} 

def to_terminal(group):
	outcomes = [row[-1] for row in group]
    #print(outcomes, max(outcomes, key=outcomes.count))
	return {'most_common' : max(set(outcomes), key=outcomes.count), 'stamp' : t3}
def split(node, max_depth, min_size, depth):
	global t1,t2,t3
	#print('this is groups   ',node['groups'])
	left, right = node['groups']
	t3+=1
	node['stamp'] = t3
	#t3+=1
	#print("Left ===========",left[:5])
	del(node['groups'])
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		t3+=1
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		t3+=1
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
		t3+=1
	else:
		node['left'] = split_in_all_in_one(left)
		split(node['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
		t3+=1
	else:
		node['right'] = split_in_all_in_one(right)
		split(node['right'], max_depth, min_size, depth+1)

def build_tree(train, max_depth, min_size):
	root = split_in_all_in_one(train)
	split(root, max_depth, min_size, 1)
	print(len(root), '\n\n', root,
					 '\n\n', root['stamp'], root['index'],  root['value'],		#0
					 '\n\n', root['left']['stamp'], root['left']['index'],root['left']['value'],			#1
					 '\n\n', root['right']['stamp'],root['right']['index'],root['right']['value'],			#7
					 '\n\n', root['left']['left']['stamp'],		#2
					 '\n\n', root['left']['right']['stamp'],	#4
					 '\n\n', root['right']['left']['stamp'],	#8
					 '\n\n', root['right']['right']['stamp'],	#11
					 '\n\n', root['left']['left']['left']['stamp'],		#3
					 '\n\n', root['left']['left']['right']['stamp'],	#3
					 '\n\n', root['left']['right']['left']['stamp'],	#5
					 '\n\n', root['left']['right']['right']['stamp'],	#6
					 '\n\n', root['right']['left']['left']['stamp'],		#9
					 '\n\n', root['right']['left']['right']['stamp'],	#10
					 '\n\n', root['right']['right']['left']['stamp'],	#12
					 '\n\n', root['right']['right']['right']['stamp'],	#13

					 '\n\n--==--', root['left']['right']['right']['left']['stamp'],	#??
					 '\n\n--==--', root['left']['right']['right']['right']['stamp'],

					 # '\n\n--==--', root['left']['left']['right']['left']['stamp'],	#??
					 # '\n\n--==--', root['left']['left']['right']['right']['stamp']
					 )	
	# 0 -> 1, 6 	1 -> 2, 4 		6 -> 7, 9
	stamp = root['stamp']
	print('initial stamp : ',stamp)
	print(print_recursive_stamp(root))

	return root

def print_recursive_stamp(root, K=list()):
	K.append(root['stamp'])
	print('-- one left_or_right is over ---')
	for left_or_right in ['left', 'right']:
		if not isinstance(root[left_or_right], int): continue
		else : return K
		#K.append(root[left_or_right]['stamp'])
		print('----root[left_or_right]----', root[left_or_right]['stamp'], '\n')
		print('-- one left_or_right is over ---')
		print_recursive_stamp(root[left_or_right])


def print_tree(node, depth=0):
	if isinstance(node, dict):
		print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
		print_tree(node['left'], depth+1)
		print_tree(node['right'], depth+1)
	else:
		print('%s[%s]' % ((depth*' ', node)))
def collect_stamp_order():
	return None

def make_tree(stamp_order, node_collection):
	return None


# ID3 part,

# feature 1 : mean(len(each sentence))
# feature 2 : diversity of vocabulary
# feature 3 : number of puntuation -> usually 0/1, so better to make normalize
# featrue etc


#########################################################################################
                            # START     ID3 algorithm       START #
#########################################################################################

#GIVEN DATA : {'author_name':{
#           	'b': {'attribute2': 1, 'attribute1': 1.63}, 
#           	'a': {'attribute2': 3, 'attribute1': 15.08}}}


#Entropy(attribute1) = -(sum(p*m.log(p,2))
#since attributes are continous numbers, it has to be split by somewhere.
#how can i split? maybe, simply, I can do, mean1(author1.attribute1), mean2(author2.attribute2)
# I need random point to split, making decision.
# mean1 ~ Random_value ~ mean2 or could be lower, higher of some point.

# example, for attribute1,  1~8 is range of total values, if 4 is split point,
# author1.attribute1 : [True, True, True, True, True, True, False, True, True, True]
# author2.attribute1 : [True, True, True, True, False, True, True]
#-(15/17*m.log(15/17, 2) + 2/17*m.log(2/17, 2)) == 0.5225593745369408

#if 2 is splitint point,
# author1.attribute1 : [False, False, False, False, False, True, False, True, False, False]
# author2.attribute1 : [True, True, True, True, True, True, True]
#-(9/17*m.log(9/17, 2) + 8/17*m.log(8/17, 2)) == 0.9975025463691153 # entropy increased.

#if 4 is split point
#Gain = -0.23
#Gain(attribute1, splitpoint_4) = Entropy(attribute1)__gold_stand - Entropy(attribute1_category1(author1)) - Entropy(attribute1_category2(author2)) 
#Entropy(attribute1)__gold_stand        = -( 15/17*m.log(15/17, 2) + 2/17*m.log(2/17, 2)) = 0.83
#Entropy(attribute1_category1(author1)) = -(9/10*m.log(9/10, 2)   + 1/10*m.log(1/10, 2)) = 0.47
#Entropy(attribute1_category1(author1)) = -(6/7*m.log(6/7, 2)     + 1/7*m.log(1/7, 2))   = 0.59

#if 2 is splitint point,
#Gain =  1 -(2+3) = 0.28
#Gain(attribute1, splitpoint_4) = Entropy(attribute1)__gold_stand - Entropy(attribute1_category1(author1)) - Entropy(attribute1_category2(author2)) 
#1.Entropy(attribute1)__gold_stand        = -(9/17*m.log(10/17, 2) + 8/17*m.log(7/17, 2)) = 1.0
#2.Entropy(attribute1_category1(author1)) = -(2/10*m.log(2/10, 2)   + 8/10*m.log(8/10, 2)) = 0.72
#3.Entropy(attribute1_category2(author2)) = -(7/7*m.log(7/7, 2)     + 0/7*m.log(0/7, 2))   = 0

#making buckets(classes) # maybe it's better to split by random point. wonder how C4.5 are working on this point.
#   1~8 is value range
#   always make range into 10 buckets, 8-1/10 = 0.7
#   1st : 1< x
#   2nd : 1<= x <1.7
#   3rd : 1.7<= x <2.4 and so on.






if __name__ == "__main__":
	read_arff(args.train)
	#make_attr_values_dict(data)
	#split_in_all_in_one(data)
	tree = build_tree(data, 4, 20)
	
	print(node_collection)
	#print(len(node_collection))
	
	#print_tree(tree)
	#split_point_list = make_split_point()
	#discretize(split_point_list)


# Pruning part, Reduced Error Pruning
""" https://www.cs.auckland.ac.nz/~pat/706_98/ln/node90.html

Consider each node for pruning
Pruning = removing the subtree at that node, make it a leaf and assign the most common class at that node
A node is removed if the resulting tree performs no worse then the original on the validation set - removes coincidences and errors
Nodes are removed iteratively choosing the node whose removal most increases the decision tree accuracy on the graph
Pruning continues until further pruning is harmful
uses training, validation & test sets - effective approach if a large amount of data is available
"""




