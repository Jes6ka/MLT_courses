# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.



#========================== import Module ==========================#
from collections import defaultdict
import argparse
import arff #https://pypi.python.org/pypi/liac-arff

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
attr_dict = defaultdict(list)
# For buckets, split point
LOW  = 10
MID  = 20
HIGH = 50
data = None
#========================== Constant ==========================#




#==========================      MAIN_START    ==========================#
#==========================      MAIN_START    ==========================#

def read_arff(file_name):
	global data
	data = arff.load(open(file_name, 'r'))# 'rb' is read as binary
	print(data['data'][:10])
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
	attr_values_dict = defaultdict(list)
	for line in raw_data['data']:	#line is [sunny, 85, 53, 2, class1]
		for n, attr_value in enumerate(line[:-REMOVE_CALSS]):
			attr_values_dict['attr'+str(n+1)].append(attr_value)
	print(attr_values_dict.keys(), attr_values_dict['attr1'][:20])
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
	for line in raw_data['data']:		#line is [sunny, 85, 53, 2, class1]
		for n, attr_value in enumerate(line[:-REMOVE_CALSS]):
			attr_class_dict['attr'+str(n+1)].append((attr_value, line[-1])) #line[-1] is class( author.txt)
	
	print(attr_class_dict.keys(), attr_class_dict['attr1'][:10])
	return attr_class_dict 				#looks like, {attr1: [(22, austen), (13, milton)], attr2 : [(1, austen), (1.3, austen)]}

def make_attr_sp_dict(raw_data):
	"""Most import part
			I'm gonna use, median, std.
			total 6std coveres more than 99.7%
			from median(M), I will use [M-3sd, M-2sd, M-sd, M-0.5sd, M, M+0.5sd, M+sd, M+2sd, M+3sd]
			So, total spliting point will be nine.
	"""
	attr_sp_dict = defaultdict(list)
	attr_values_dict = make_attr_values_dict(raw_data) 				#{attr1: [22,24,21,23,...], attr2: [1,2,1,1,...]}
	
	for n in range(len(attr_values_dict)): #len(attr_values_dict) is number of attributes.
			avd = attr_values_dict['attr'+str(n+1)]
			median  = np.median(avd)
			tm  = stats.trim_mean(avd, 0.10)
			sd  = np.std(avd, ddof=1)
			attr_sp_dict['attr'+str(n+1)].append(median-2*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median-1*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median-0*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median+1*sd)  #line[-1] is class( author.txt)
			attr_sp_dict['attr'+str(n+1)].append(median+2*sd)  #line[-1] is class( author.txt)
	

	print('\n\n',attr_sp_dict)
	return attr_sp_dict 							#looks like, {attr1 : [sp1, sp2, ...sp9]}, attr2 : [sp1,sp2..sp9]


def make_split_point(split_number = MID): # let's use stats.trim_mean(x, 0.1) trimming-left-right-10%, total 20% then get mean.
	global attr_dict
	split_interval = 0
	split_point_dict = defaultdict(list)
	
	
	class_index = len(data['data'][0])-remove_class # max-1, it means, removing "Class, Categories, authors"

	for one_line in data['data']:
		for n, attr_value in enumerate(one_line):
			if n == class_index : break
			attr_dict['attr'+str(n)].append(attr_value)
			# {attr0:[21, 24...], attr1:[0.2, 0.1...], ...attr[n-1] :[9999,9999,9999...]]
	for each_attr in attr_dict:
		#print('888888888888888888', np.std(attr_dict[each_attr]), attr_dict[each_attr][:10], type(attr_dict[each_attr][0]))
		#split_interval = round(np.median(attr_dict[each_attr])/split_number, 3) 	# Median
		#split_interval = round(stats.mode(attr_dict[each_attr])/split_number, 3) 	# Mode
		
		# stats.kurtosis(arr), 3 is twisted, 0 for a normal distribution
		# stats.kurtosistest(arr), return Z-score & p-value
		#A z-score equal to 0 represents an element equal to the mean. 
		#A z-score equal to 1 represents an element that is 1 standard deviation greater than the mean; 
		#a z-score equal to 2, 2 standard deviations greater than the mean

		# stats.skew(arr), 0 is equal symmetric to axis
		# stats.skewtest(arr),  return Z-score & p-value

		split_interval = np.std(attr_dict[each_attr], ddof=1)/split_number 	#ddof,  unbiased estimator  (N-1 in the denominator)
		#print('555555555555', split_interval)
		# Simply,  interval = max-min/split_number
		
		temp = [-float("inf")] # This is because, split point must be unique.
		for step in range(split_number):
			print(step, split_number, 'aaaaaaaaaaaaaaaaaaaa', min(attr_dict[each_attr]))
			temp.append(min(attr_dict[each_attr]) + step*round(split_interval, 3))
		
		#split_point must have bigger # than elements, that's why adding +1
		temp.append(round(max(attr_dict[each_attr])+1, 3))
		split_point_dict[each_attr].append(temp)

    # Assume, attributes1~3, each attributes has 10classes, total 30
	print(split_point_dict)
	return split_point_dict
	# {attr0 : [sp1, sp2, ...sp20], attr1 :[sp1, sp2, ... sp20] ...]
	# data[data] : [attr0-value, attr1-value... class]
    # what i need, {class1 : {attr0 : [22, 32, 19,...], attr1:[ ... ]}, class2 : {attr0 : []} }

def discretize(split_point_list):
	#split_point_list = [0, 4, 10, 30, 45, 99999], my case # 22 : [ [0, sp1, sp2, ...sp20, sp20+1], [sp1, sp2, ... sp20] ...]
	#split_point_list(bins) must be one more than the number of Label(bucket_list)
	discretized_attr_dict = defaultdict(list)
	bucket_list = []
	#label = bucket_list

	for i in range(len(split_point_list[0])-1):
		bucket_list.append('b'+str(i))

	print('\n\nbucket list is ',bucket_list, '\n\n split_point_list', split_point_list)
	
	for attr in attr_dict:
		temp = attr_dict[attr]
		print('\n\n',temp[:200], type(temp), type(temp[0]),'\n\n')
		for split_points in split_point_list:
			discretized_attr_dict[attr].append(pd.cut(temp, bins=split_points, labels=bucket_list))
			#pd.cut(temp[:20], bins=split_points, labels=bucket_list)

	# {attr0:[21, 24...], attr1:[0.2, 0.1...], ...attr[n-1] :[9999,9999,9999...]]
	#labels = ['b0', 'b1', 'b2', 'b3','b4' ... 'b18'] #total # is 19
	# Categories (5, object): [High_Fare < Low_Fare < Med_Fare < Very_High_Fare < Very_Low_Fare]
	# reference : https://stackoverflow.com/questions/23267767/how-to-do-discretization-of-continuous-attributes-in-sklearn

	print(discretized_attr_dict['attr1'][:20])
	return discretized_attr_dict



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
#Gain = -0.08
#Gain(attribute1, splitpoint_4) = Entropy(attribute1)__gold_stand - Entropy(attribute1_category1(author1)) - Entropy(attribute1_category2(author2)) 
#Entropy(attribute1)__gold_stand        = -(10/17*m.log(10/17, 2) + 7/17*m.log(7/17, 2)) = 0.98
#Entropy(attribute1_category1(author1)) = -(9/10*m.log(9/10, 2)   + 1/10*m.log(1/10, 2)) = 0.47
#Entropy(attribute1_category1(author1)) = -(6/7*m.log(6/7, 2)     + 1/7*m.log(1/7, 2))   = 0.59

#if 2 is splitint point,
#Gain =  1 -(2+3) = 0.26
#Gain(attribute1, splitpoint_4) = Entropy(attribute1)__gold_stand - Entropy(attribute1_category1(author1)) - Entropy(attribute1_category2(author2)) 
#1.Entropy(attribute1)__gold_stand        = -(10/17*m.log(10/17, 2) + 7/17*m.log(7/17, 2)) = 0.98
#2.Entropy(attribute1_category1(author1)) = -(2/10*m.log(2/10, 2)   + 8/10*m.log(8/10, 2)) = 0.72
#3.Entropy(attribute1_category2(author2)) = -(7/7*m.log(7/7, 2)     + 0/7*m.log(0/7, 2))   = 0

#making buckets(classes) # maybe it's better to split by random point. wonder how C4.5 are working on this point.
#   1~8 is value range
#   always make range into 10 buckets, 8-1/10 = 0.7
#   1st : 1< x
#   2nd : 1<= x <1.7
#   3rd : 1.7<= x <2.4 and so on.


def entropy(prob):		#prob : 10/17
    return(-(p*np.log2(p)+(1-p)*np.log2(1-p)))

def gain(gold, bn= LOW):       # bp = bucket numbers
    # TODO
    # calculate GAIN
    # gain = gold
    # for author in author_list:#file_list
    #     gain -= entropy(author)
    # return each_gain_value
    return None




if __name__ == "__main__":
	read_arff(args.train)
	make_attr_values_dict(data)
	#make_attr_class_dict(data)
	make_attr_sp_dict(data)

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




