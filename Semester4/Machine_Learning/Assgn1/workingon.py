# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.

#========================== import Module ==========================#
import os, sys, argparse;
import arff #https://pypi.python.org/pypi/liac-arff

import numpy as np
from collections import Counter
import random

#import nltk
from nltk.probability import FreqDist
from nltk.corpus import gutenberg
from nltk.corpus import stopwords

#scikit-learn
from sklearn.metrics import confusion_matrix #http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

#========================== import Module ==========================#



#========================== Constant ==========================#
# tag - start symbol 
start_symbol = "start"
end_symbol = "end"
T = 1#len(tag_counter)
V = 1#len(word_counter)
A = 0.01
unseen_word_dict = {}
Z = 1.96 # 95% of confidence
stop = set(stopwords.words('english'))
punkt = {'.', ',', '\/', '\'', '"', '?', '!', '@', '#', '$', '-', '--', '...', '[', ']', '{', '}', ':', ';', '/', ',"', '."', "!\""}

#========================== Constant ==========================#


parser = argparse.ArgumentParser(description = "Process the txt files")
parser.add_argument("files", nargs="+", type=str, help="the input file names" )
parser.add_argument("--train", type=str, required=True, help="the input file names" )
parser.add_argument("--test", type=str, required=True, help="the input file names" )

parser.add_argument("--testpercent", type=int, required=True, help="the input file names" )
parser.add_argument("--svd", default = "False")
parser.add_argument("--novocab", default = "False" , action = "store_true")

args = parser.parse_args()
#now load the files.

trainfile = open(args.train, "w")
trainingdata = {}
trainingdata[u'relation']   = "No_relation_exist" 
trainingdata[u'attributes'] = [
				(u'sentencelength', u'REAL'),
				(u'somelength', u'REAL'),
				(u'class', args.files)
				]
trainingdata[u'description'] = "this is description"



#filehandles = []
for filename in args.files:
	print(filename)
	#filehandles.append(open(filename, "r"))


#loading is, data = arff.load(open('wheater.arff', 'rb'))
trainfile.write(arff.dumps(trainingdata))
trainfile.close()

# arff part, there is handy library
#pip instal liac-arff

#pip install drawtree




def read_corpus(corpus_file):
    out = []
    with open(corpus_file) as f:
        for line in f:
            tokens = line.strip().lower().split()
            #Without stopwords, use below line. but result is not same.
            #tokens = [i for i in line.lower().split() if i not in stop]
            out.append( (tokens[0], tokens[3:]) )
    return out


"""
#primitive style with using only library @sys@
#Arg should get file1...file[n] : total n number of file    
if __name__ == "__main__":
        import sys
        if len(sys.argv) <1 : 
            exit("write some file name")
        else :
        	#sys.argv[1], argv[2]...rgv[n] are txt file name

            print("this is whole", str(sys.argv))
            print("this is whole", len(sys.argv), type(sys.argv))            
            print("this is whole", str(sys.argv[1]), type(sys.argv[1]))
            file_list = []
           	for i in range(len(sys.argv)-1): # finish len-1
           		file_list.append(str(sys.argv[i+1]))	#start from 1
"""




# ID3 part,
"""

ID3 (Examples, Target_Attribute, Attributes)
    Create a root node for the tree
    If all examples are positive, Return the single-node tree Root, with label = +.
    If all examples are negative, Return the single-node tree Root, with label = -.
    If number of predicting attributes is empty, then Return the single node tree Root,
    with label = most common value of the target attribute in the examples.
    Otherwise Begin
        A ← The Attribute that best classifies examples.
        Decision Tree attribute for Root = A.
        For each possible value, vi, of A,
            Add a new tree branch below Root, corresponding to the test A = vi.
            Let Examples(vi) be the subset of examples that have the value vi for A
            If Examples(vi) is empty
                Then below this new branch add a leaf node with label = most common target value in the examples
            Else below this new branch add the subtree ID3 (Examples(vi), Target_Attribute, Attributes – {A})
    End
    Return Root

Entropy(S) = Sum(-PlogP)
Gain(S, A) = Entropy(S) - Sum((S_v / S) * Entropy(Sv))

Sum is each value v of all possible values of attribute A
Sv = subset of S for which attribute A has value v
|Sv| = number of elements in Sv
|S| = number of elements in S

"""

# feature 1 : mean(len(each sentence))
# feature 2 : diversity of vocabulary
# feature 3 : number of puntuation -> usually 0/1, so better to make normalize
# featrue etc


#########################################################################################
                            # START     ID3 algorithm       START #
#########################################################################################

feature =   {'attribute1' : 
                    {'author1' : [2,2,3,2,3,1,4,1,2,3] #len == 10
                    'author2' : [8,7,5,4,3,6,7]}       #len == 7
            'attribute2'  : 
                    {'author1' : [20,24,35,22,33,12,41,15,20,30]
                    'author2' : [80,20,50,40,30,50,30]}

            }
text       = ['text1', 'text2']
categories = ['author1', 'author2']
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
#3.Entropy(attribute1_category1(author1)) = -(7/7*m.log(7/7, 2)     + 0/7*m.log(0/7, 2))   = 0


def entropy(labels,n=2):
    if n<=1: n=2#exception, consider bigger than Logorithm 2(in case, channel is bigger than bits)
    fd=nltk.FreqDist(labels)
    probs=[fd.freq(a) for a in nltk.FreqDist(labels)]
    return(-(sum([p*m.log(p,n) for p in probs])))

def gain():
    return

import nltk; from nltk.corpus import stopwords
stops = set(stopwords.words('english'))



# Pruning part, Reduced Error Pruning
""" https://www.cs.auckland.ac.nz/~pat/706_98/ln/node90.html

Consider each node for pruning
Pruning = removing the subtree at that node, make it a leaf and assign the most common class at that node
A node is removed if the resulting tree performs no worse then the original on the validation set - removes coincidences and errors
Nodes are removed iteratively choosing the node whose removal most increases the decision tree accuracy on the graph
Pruning continues until further pruning is harmful
uses training, validation & test sets - effective approach if a large amount of data is available
"""
