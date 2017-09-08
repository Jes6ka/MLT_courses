# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.

#========================== import Module ==========================#

import numpy as np                        # np.log, np.log2


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

#========================== Constant ==========================#





# ID3 part,

# feature 1 : mean(len(each sentence))
# feature 2 : diversity of vocabulary
# feature 3 : number of puntuation -> usually 0/1, so better to make normalize
# featrue etc


#########################################################################################
                            # START     ID3 algorithm       START #
#########################################################################################

#GIVEN DATA : {'author_name':{
#           	'b': {'attribute2': 1, 'attribute1': 212.49999946875}, 
#           	'a': {'attribute2': 3, 'attribute1': 433.3333318888889}}}


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



def entropy(labels,n=2):
    if n<=1: n=2#exception, consider bigger than Logorithm 2(in case, channel is bigger than bits)
    fd=nltk.FreqDist(labels)
    probs=[fd.freq(a) for a in nltk.FreqDist(labels)]
    return(-(sum([p*m.log(p,n) for p in probs])))

def gain(gold, file_list(author_list), bp= None):       # bp = bucket point
    # TODO
    # calculate GAIN
    gain = gold
    for author in author_list:#file_list
        gain -= entropy(author)
    return each_gain_value

def search_best_scope( number_bucket_boundary = 10):
    """
    try to find best scope where it gets highest GAIN_VALUE
    """
    # Assume, attributes1~3, each attributes has 10classes, total 30
    n = number_bucket_boundary #let's say we have 10 bucket_boundary. e.g., b1-b10

    for attribute in attribute_list:                     # attribute_list = [attribute1, attribute2...]
        boundary_range = max(attribute) - min(attribute) # @@TODO value of 
        bb_list        = boundary_range/n                # bb == bucket boundary
        
        for 

        gain(attribute, bp= bb)
        for bucket in bucket_list:                       #bucket_list = [1, 1.7, 2.4, ... 8] # look line 196
            for i in range(len(author1.attribute)):      #TODO, have to set&compare bp with given data.
                if i = 0 :
                    if author1.attribute1[0] = bucket

# feature =   {'attribute1' : 
#                     {'author1' : [2,2,3,2,3,1,4,1,2,3] #len == 10
#                     'author2' : [8,7,5,4,3,6,7]}       #len == 7






#########################################################################################
                        # now, here SVM part to reduce "dimension"
#########################################################################################

# np.linalg.svd
# np.linalg.norm() -- cosine distance 

def svd_transform(space, originalnumdimensions,keepnumdimensions):
    # space is a dictionary mapping words to vectors.
    # combine those into a big matrix.
    spacematrix = numpy.empty((len(space.keys()), originalnumdimensions))

    rowlabels = sorted(space.keys())

    for index, word in enumerate(rowlabels):
        spacematrix[index] = space[word]

    # now do SVD
    umatrix, sigmavector, vmatrix = numpy.linalg.svd(spacematrix)

    # remove the last few dimensions of u and sigma
    utrunc = umatrix[:, :keepnumdimensions]
    sigmatrunc = sigmavector[ :keepnumdimensions]

    # new space: U %matrixproduct% Sigma_as_diagonal_matrix   
    newspacematrix = numpy.dot(utrunc, numpy.diag(sigmatrunc))

    # transform back to a dictionary mapping words to vectors
    newspace = { }
    for index, word in enumerate(rowlabels):
        newspace[ word ] = newspacematrix[index]
        
    return newspace

####
### run this:
def test_svdspace():
    numdims = 100
    # which words to use as targets and context words?
    ktw = do_word_count(demo_dir, numdims)
    # mapping words to an index, which will be their column
    # in the table of counts
    wi = make_word_index(ktw)
    words_in_order = sorted(wi.keys(), key=lambda w:wi[w])
    
    print("word index:")
    for word in words_in_order:
        print(word, wi[word], end=" ")
    print("\n")

    space = make_space(demo_dir, wi, numdims)
    ppmispace = ppmi_transform(space, wi)
    svdspace = svd_transform(ppmispace, numdims, 5)
    
    print("some vectors")
    for w in words_in_order[:10]:
        print("--------------", "\n", w)
        print("raw", space[w])
        # for the PPMI and SVD spaces, we're rounding to 2 digits after the floating point
        print("ppmi", numpy.round(ppmispace[w], 2), "\n")
        print("svd", numpy.round(svdspace[w], 2), "\n")

if __name__ == "__main__":
    # for book in book_list:
    #     generate_txt_file_from_gutenberg(book)
    shuffle_sentence_and_save(args)


# Pruning part, Reduced Error Pruning
""" https://www.cs.auckland.ac.nz/~pat/706_98/ln/node90.html

Consider each node for pruning
Pruning = removing the subtree at that node, make it a leaf and assign the most common class at that node
A node is removed if the resulting tree performs no worse then the original on the validation set - removes coincidences and errors
Nodes are removed iteratively choosing the node whose removal most increases the decision tree accuracy on the graph
Pruning continues until further pruning is harmful
uses training, validation & test sets - effective approach if a large amount of data is available
"""




