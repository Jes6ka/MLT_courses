# SUNG MIN YANG. Master in Language Technology in Gothenburg University in 2017.

#========================== import Module ==========================#
import os, sys, argparse;
import random, copy;

from collections import defaultdict

#import nltk
from nltk.corpus import gutenberg

from feature import *


# arff part, there is handy library
#pip instal liac-arff
#pip install drawtree

#========================== import Module ==========================#




#========================== Get Arguments ==========================#

parser = argparse.ArgumentParser(description = "Process the txt files")
parser.add_argument("files", nargs="+", type=str, help="the input file names" )
parser.add_argument("--train", type=str, required=True, help="name of train file" )
parser.add_argument("--test", type=str, required=True, help="name of test file" )

parser.add_argument("--testpercent", type=int, required=True, help="how much percent to use for test, recommened : 20 or 30" )
parser.add_argument("--svd", type= int, default = 0)
parser.add_argument("--novocab", default = False , action = "store_true")

args = parser.parse_args()
#========================== Get Arguments ==========================#





#========================== Constant ==========================#

gutenberg_book_list = list(gutenberg.fileids())
annotated_sents  = []
txt_length = 0
splitpoint = 0
shuffled_dict = {'shuffled_train' : [], 'shuffled_test' : []}
#========================== Constant ==========================#





#==========================     get some text       ==========================#
#========================== This code is only used  ==========================#
#========================== for creating txt file   ==========================#
#   I used gutenberg_pre_tokenized txt file since it seems like manually tokenized by human, more accurate than tokenizer.
#   txt_name = 'austen-persuasion.txt', 'milton-paradise.txt', 'chesterton-ball.txt'
#   I chose the above books because file sizes are similar which means # of sents are similar

#   how to create gutenberg txt file : for book in gutenberg_book_list : gerate_txt_file_from_gutenberg(book)
def generate_txt_file_from_gutenberg(txt_name): 
    """
    from gutenberg file -> saving to real xxx.txt 
    """
    sense = list(gutenberg.sents(txt_name))[2:]
    # from sense[2], text begin
    # sense[2] : ['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']
    sense = [ ' '.join(sense[i]) for i in range(len(sense))]

    with open(txt_name, "w") as f:
        for i in range(len(sense)):
            f.write(sense[i] +'\n')
    return None
#==========================     END of    ==========================#
#========================== get some text ==========================#




#==========================     BONUS_START    ==========================#
#   Have to use this code when don't have pre-made tokenized books. but we have nltk.
def read_txt_file(txt_file):
    import codecs
    sents = []
    with codecs.open('Prejudice.txt','r','utf8') as f:
            output = [sents.append(wordpunct_tokenize(line.strip().lower())) for line in f if line.strip()!= ''] 
    return output
#==========================     BONUS_END       ==========================#






#==========================      MAIN_START    ==========================#
#==========================      MAIN_START    ==========================#

def shuffle_sentence_and_save(args_obj):
    """
    in order to handle of arbitary cases, randomize sentence order.
    """

    global txt_length
    global annotated_sents
    global splitpoint
    global shuffled_dict

    txt_sents         = defaultdict(list) # looks like this, {'author1' : [sent1, sent2 ...]}
    testpercent_dict  = {'train' : [], 'test' : []} #[[splitpoint], [sent1, sent2, sent3]]
    

    for each_txt_file in args_obj.files:
        with open(each_txt_file, 'r') as f:
                for line in f:
                    txt_sents[each_txt_file].append(line)
                    #didn't make it lower(). because, it seems it helps, classification.
                    #e.g., With, Though, Alice, ... can be used for tree. maybe.

        # mixed all sentence.
        random.shuffle(txt_sents[each_txt_file])
        txt_length = len(txt_sents[each_txt_file])

        splitpoint = split_train_test_set(args_obj, txt_sents[each_txt_file])


        #                                 each_txt_file[:-4]
        testpercent_dict['train'].append((each_txt_file, txt_sents[each_txt_file][:splitpoint]))
        testpercent_dict['test'].append((each_txt_file, txt_sents[each_txt_file][splitpoint:]))
        # testpercent_dict = {'train' : [(author1, [sent1...sent1868]), (author2, [sent1, sent2...]) (author1, sent2)], 'test' : [20, 43]}
        #                     'test'  : [(author1, [sent1869...sent2123]), (author2, [])


    #final shuffle
    for author in testpercent_dict['train']:
        for sent in author[1] : #author[1] is sents of each author
            shuffled_dict['shuffled_train'].append((author[0], sent))
    for author in testpercent_dict['test']:
        for sent in author[1] : #author[1] is sents of each author
            shuffled_dict['shuffled_test'].append((author[0], sent))
    # shuffled_dict looks like this
    # { shuffled_train : [(author1, sent1)... (author2, sent1).....]
    #   shuffled_test  : [(author1, sent1), (author1, sent2).....}
    
    random.shuffle(shuffled_dict['shuffled_train'])
    random.shuffle(shuffled_dict['shuffled_test'])

    with open('shuffled_'+args_obj.train, 'w') as f:
        for each_author_sent in shuffled_dict['shuffled_train']:
            f.write(each_author_sent[0]+' ' +each_author_sent[1])
    with open('shuffled_'+args_obj.test, 'w') as f:
        for each_author_sent in shuffled_dict['shuffled_test']:
            f.write(each_author_sent[0]+ ' ' +each_author_sent[1])


    annotated_sents = shuffled_dict['shuffled_train']

    return(None)

def split_train_test_set(args_obj, sentences):
    splitpoint    = int(txt_length*(100-args_obj.testpercent)/100)
    return(splitpoint)



if __name__ == "__main__":
# for book in gutenberg_book_list:
#     generate_txt_file_from_gutenberg(book)
    #print("inside of propro.py")
    shuffle_sentence_and_save(args)

    
    if args.novocab :
        print('inside of novocab\n')
        #here feature4_vocab
        if args.svd != 0:
            print('inside of svd\n')
            #here feature5_vocab_svd
    
    obj_train = attributes_collection(args, shuffled_dict['shuffled_train'])
    obj_test = attributes_collection(args, shuffled_dict['shuffled_test'])

    print(len(obj_train.final_list))
    print(len(obj_test.final_list))

    obj_train.extract_attr()
    obj_train.save_to_arff(train=True)
    obj_test.extract_attr()
    obj_test.save_to_arff(test=True)
    #print(vars(test), dir(test))
    print("this is svd ", args.svd, "\nthis is novocab", args.novocab)
