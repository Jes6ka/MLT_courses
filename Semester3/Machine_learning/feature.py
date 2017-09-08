# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.

#========================== import Module ==========================#

import numpy as np                        # np.log, np.log2
from collections import Counter
from collections import defaultdict

#import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist

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
word_scale_book_dict = defaultdict(list)
#defaultdict is not dict, cannot be re-called.
attr_num = 1

stops = set(stopwords.words('english'))
punctuation = ['.', ',', '\/', '\'', '"', '?', '!', '@', '#', '$', '-', '--', '...', '[', ']', '{', '}', ':', ';', '/', ',"', '."', "!\""]

#========================== Constant ==========================#



def tokenize(use_book_dict_here):
    global word_scale_book_dict

    for each_book_name in use_book_dict_here:
        for sent in use_book_dict_here[each_book_name]:
            word_scale_book_dict[each_book_name] = sent.split(' ')
    return None

def punct_number(sent):
    sum = 0
    for word in sent:
        if word in punctuation: sum+=1
    return sum




#########################################################################################
                      # START     Getting attributes       START #
#########################################################################################

def feature1(sent_scale_dict_here):
    """ punct_sentence_ratio  : len(sent)/#_of_punctuation"""

    feature1_dict = defaultdict(list)
    for each_book_name in sent_scale_dict_here:
        for sent in sent_scale_dict_here[each_book_name]:
            print(len(sent), sent,punct_number(sent))
            feature1_dict[each_book_name] = 50*len(sent)/(punct_number(sent)+0.00000001)
    print(feature1_dict)
    return feature1_dict

def feature2(word_scale_book_dict):
    """ # of long words"""

    feature2_dict = defaultdict(list)
    for each_book_name in word_scale_book_dict:
        score = 0
        for word in word_scale_book_dict[each_book_name]:
            print(word, len(word))
            if len(word) >= 4 : score+=1
        print("score is {0}".format(score))
        feature2_dict[each_book_name] = score

    return feature2_dict


def feature3():
    return None


class attributes_collection():
    """
    collections of authors + attributes
    """
    def __init__(self):     # e.g., attributes_collection(feature1)
        
        self.author_name = {}
        
    #{author1 : {attribute1 : [142, 252, 234], attribute2 : [1,2,2]}
    def add(self, input_feature_here):
        global attr_num
        for author in input_feature_here:
            if attr_num == 1 :
                self.author_name[author] = {}
                self.author_name[author]['attribute%d'%(attr_num)] = input_feature_here[author]
            else :
                self.author_name[author]['attribute%d'%(attr_num)] = input_feature_here[author]
        attr_num +=1
        print(attr_num, '\n')

    def __str__(self):
        return self.__name__





#==========================      RUNNING    ==========================#
#==========================      RUNNING    ==========================#

if __name__ == "__main__":
    book_dict = {'a' : ['a b c , . aasd basdasdws abbbb a b a a a,'], 'b' : ['gsswa q we r : ; ,, e']}
    tokenize(book_dict) # save to "word_scale_book_dict"
    feature1 = feature1(book_dict)
    feature2 = feature2(word_scale_book_dict)
    test = attributes_collection()
    test.add(feature1)
    test.add(feature2)
    print(vars(test), dir(test))
    
    #output : {'author_name':{
    #           'b': {'attribute2': 212.49999946875, 'attribute1': 212.49999946875}, 
    #           'a': {'attribute2': 433.3333318888889, 'attribute1': 433.3333318888889}}}

#==========================      RUNNING    ==========================#
#==========================      RUNNING    ==========================#
