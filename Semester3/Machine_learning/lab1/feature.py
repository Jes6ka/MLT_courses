# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.

#========================== import Module ==========================#

import numpy as np
import collections
from collections import defaultdict

#import nltk
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
author_word_dictionary = defaultdict(list)
word_in_sent = []           # defaultdict(list) #looks like, 
#defaultdict is not dict, cannot be re-called.

track_attr_num = 1
stops = set(stopwords.words('english'))
punctuation = ['.', ',', '\/', '\'', '"', '?', '!', '@', '#', '$', '-', '--', '...', '[', ']', '{', '}', ':', ';', '/', ',"', '."', "!\""]

#========================== Constant ==========================#


#  annotated_sents = [('a', "This is glory"), ('b', "sent3"), ...]
def tokenize(annotated_sents):
    global word_in_sent
    global author_word_dictionary

    for author, sent in annotated_sents:
        tokenized_sent = sent.rstrip().split(' ')
        word_in_sent.append((author, tokenized_sent))
        #word_in_sent : [(author, [word1, word2, word3...])]

        for word in tokenized_sent:
            author_word_dictionary[author].append(word)
        #author_word_dictionary : {'author1' : [word1, word2, word3,...])]

    return None

def punct_number(sent):
    sum = 0
    for word in sent:
        if word in punctuation: sum+=1
    return sum

#author_word_dictionary : {'author1' : [word1, word2, word3,...])]
def remove_punct(author_word_dictionary):
    punt_removed_dict = defaultdict(list)
    for author in author_word_dictionary:
        for word in author_word_dictionary[author]:
            if word in punctuation : pass
            else : punt_removed_dict[author].append(word)
    return punt_removed_dict

def remove_stopword(author_word_dictionary):
    stop_removed_dict = defaultdict(list)
    for author in author_word_dictionary:
        for word in author_word_dictionary[author]:
            if word in stops : pass
            else : stop_removed_dict[author].append(word)
    return stop_removed_dict

#########################################################################################
                      # START     Getting attributes       START #
#########################################################################################

#  annotated_sents = [('a', "This is glory"), ('b', "sent3"), ...]
def feature1(annotated_sents):
    """ punct_sentence_ratio  : len(sent)/#_of_punctuation"""

    feature1_list = []
    for author, sent in annotated_sents:
            #print(len(sent), sent, punct_number(sent))
            feature1_list.append( (author, float("{0:.2f}".format(np.exp(len(sent)/10)/(punct_number(sent)+0.00001)))))
    #print("THis is feature1: ",feature1_list)
 
    return feature1_list

#word_in_sent : [(author, [word1, word2, word3...]), (aut2, [w1, w2...])]

def feature2(annotated_sents):
    """ # of long words"""

    #tokenize(annotated_sents)
    feature2_list = []

    for author, word_list in word_in_sent:
        score = 0
        for word in word_list:
            #print(word, len(word))
            if len(word) >= 7 : score+=1
    # """
    # Here is amazing part. if I set len(word)>=7, I'll get 41percent or so in real data.
    # But when I set it as 7, 64percent at validation(10folds), 
    #         68percent in real test set.
    # """
        #print("score is {0}".format(score))
        feature2_list.append((author, score))

    #print("THis is feature2: ", feature2_list)

    return feature2_list


#author_word_dictionary : {'author1' : [word1, word2, word3,...])]
#  annotated_sents = [('a', "This is glory"), ('b', "sent3"), ...]
def feature3(annotated_sents):
    #tokenize(annotated_sents) # <== already excuted before in feature1, or just put it in class function
    feature3_list = []
    for author, sent in word_in_sent:
        feature3_list.append((author, 9999))
    
    # counter=collections.Counter(author_word_dictionary['austen-persuasion.txt'])
    # print(counter.most_common(50))
    # counter=collections.Counter(author_word_dictionary['milton-paradise.txt'])
    # print(counter.most_common(50))
    
    # punt_removed_dict = remove_punct(author_word_dictionary)
    # counter=collections.Counter(punt_removed_dict['austen-persuasion.txt'])
    # print(counter.most_common(50))
    # counter=collections.Counter(punt_removed_dict['milton-paradise.txt'])
    # print(counter.most_common(50))

    #print(author_word_dictionary['austen-persuasion.txt'][:40])
    return feature3_list

def feature4(annotated_sents):
    tokenize(annotated_sents)
    feature4_list = []
    for author, word_list in word_in_sent:
        score = 0
        for word in word_list:
            if word in stops: score+=1
        feature4_list.append((author, score))

    return feature4_list

class attributes_collection():
    """
    collections of authors + attributes
    """
    def __init__(self, args_obj, annotated_sents):     # e.g., attributes_collection(feature1)
        self.args    = args_obj
        self.svd     = args_obj.svd         # 200
        self.novocab = args_obj.novocab # True/False
        self.sents   = annotated_sents
        #feature_list : [f1, f2...]
        self.final_list   = []

        self.features = ['punct_sentence_ratio',
                          '#_of_long_words',
                          'Test_attribute3',
                          'Test_attribute4']

        tokenize(annotated_sents) #for feature1, 2 +
    #sent1 : [aut1, [13, 5133, 0.11]]
    #sent2 : [aut2, [15, 2929, 0.02]]

    #Total : [  [aut1, [13, 5133, 0.11]],
    #           [aut2, [15, 2929, 0.02]] ......]
    def extract_attr(self, svd=0, novocab=False): # [('aut1', 3), ('aut2', 1)...]
        
        for i in range(len(self.features)):
            each_feature_list = eval("feature"+str(i+1))(self.sents)

            #print(each_feature_list[:10])

            if self.final_list ==[]:
                for author, value in each_feature_list:
                    temp = []
                    temp.append(author)
                    temp.append([value]) # ['author', [22]]
                    # print(temp[0], "=-----stop=======",author)
                    # print(temp[0]==author)
                    self.final_list.append(temp)  #[[milton, [0.14]], [austen, [0.05]]]

            else:
                for n, (author, value) in enumerate(each_feature_list):
                    #sometimes it occurs error. simply ignore it by not saving it. maybe one or two sentence afftected.
                    try : self.final_list[n][1].append(value)  # ['author', [22, 1.492]]
                    except : pass
                        #print(len(self.final_list), '------\n', len(each_feature_list), each_feature_list[:10])
                        #print("===========", self.final_list[i][0], author)
                        #assert(self.final_list[i][0]==author)
                    #print('flaggggggg', self.final_list[flag][0], author, self.final_list[flag])
                 # [  ['author1', [22, 1]], ['author2', [10, 2]] ]
            print("one_round successful")

        #print(attr_num, '\n')
        return(print("all successful"))

    def save_to_arff(self, train=False, test=False):
        if train : filename  = self.args.train
        elif test : filename = self.args.test
        print("This is file name",filename)

        with open(filename, 'w') as f:
            f.write("@RELATION {}\n\n".format("text_classifier"))
            for attr_name in self.features:
                f.write("@ATTRIBUTE {} REAL\n".format(attr_name))

            temp = "@ATTRIBUTE class {"
            for class_name in self.args.files:
                temp+=(class_name+',')
            
            f.write(temp[:-1]+"}\n\n@DATA\n")

            for line in self.final_list: # line = [austen, [22, 3]]
                temp = ""
                for score in line[1]:
                    temp += str(score)+","
                temp+=str(line[0])+"\n"
                f.write(temp)
        return(print("arff save successful"))

    def __str__(self):
        return self.__name__





#==========================      RUNNING    ==========================#
#==========================      RUNNING    ==========================#

if __name__ == "__main__":
    #annotated_sents = [('aut1', 'a b c , . aasd basdasdws abbbb a b a a a,'), ('aut2', 'gsswa q we r : ; ,, e')]
    #annotated_sents = [('a', "sent11"), ('b', "sent3"), ...]

    test = attributes_collection(args)
    test.extract_attr()
    #print(vars(test), dir(test))
    
    #output : {'final_list':{
    #           'b': {'attribute2': 1, 'attribute1': 212.49999946875}, 
    #           'a': {'attribute2': 3, 'attribute1': 433.3333318888889}}}

#==========================      RUNNING    ==========================#
#==========================      RUNNING    ==========================#
