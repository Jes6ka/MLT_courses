#Simple_Naive_Bayes
#naive_bayes_text_classification.py



import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
#print [i for i in sentence.lower().split() if i not in stop]

def read_corpus(corpus_file):
    out = []
    with open(corpus_file) as f:
        for line in f:
            tokens = line.strip().split()
            #tokens = [i for i in line.lower().split() if i not in stop]
            out.append( (tokens[0], tokens[3:]) )
    return out


class naive_bayes(object):
	def __init__(self, training_data):
		self.traing_data = training_data
		self.get_dictionaries()
		self.generate_words_prob()
		self.prob_author()

	#Training
	def get_dictionaries(self):
		author_dict = {} # {'CBronte': 10696, 'Eliot': 21423}
		content_dict = {} #{"CBronte" : ['take','care', 'of', ......],  "Eliot" : [...]}
		simple_content_dict = {}  #{"CBronte" : set(content_dict[author]),  "Eliot" : [...]}
		words_count_dict = {} # {"CBronte" : FreqDist(content_dict[author]), }


		for author, words in self.traing_data:
			if author not in author_dict:
				author_dict[author]=1
				content_dict[author]=[]
				content_dict[author].append(words)
			else:
				author_dict[author]+=1
				content_dict[author].append(words)

		#dict_keys(['CBronte', 'Eliot'])
		for author in author_dict.keys():
		    flat_list = [a for b in content_dict[author] for a in b]
		    content_dict[author]=flat_list
		    simple_content_dict[author]=set(flat_list)
		    words_count_dict[author] = FreqDist(content_dict[author])

		    print(len(content_dict[author]))# Number of total words. 271069    539095
		    print(flat_list[:10])

		self.dictionaries=[]
		self.dictionaries.append(author_dict)
		self.dictionaries.append(content_dict)
		self.dictionaries.append(simple_content_dict)
		self.dictionaries.append(words_count_dict)# FreqDist()
		return self.dictionaries

	def generate_words_prob(self):
		words_prob_dict = {}
		for author in self.dictionaries[3].keys():
			words_prob_dict[author]={}
			fd = self.dictionaries[3][author]
			words_prob_dict[author]["null"] = 1/(fd.N()+len(fd))
			for word, freq in set(fd.items()):
				temp=(fd[word]+1)/(fd.N()+len(fd))#fd[word]+1 is smoothing, len(fd) is Vocabulary
				#same with --- temp=(freq+1)/(fd.N()+len(fd))

				words_prob_dict[author][word] = temp
				#words_prob_dict[author].append((word, temp)) #each word get own probability.

		self.words_prob_dict=words_prob_dict
		return self.words_prob_dict

	def prob_author(self):
		total=sum(self.dictionaries[0].values())
		author_prob_diction_local = {}
		for author in self.dictionaries[0].keys():
			author_prob_diction_local[author] = float(self.dictionaries[0][author]/total)

		self.author_prob_dict = author_prob_diction_local
		return self.author_prob_dict



#fd.N()#total number of words
#len(fd) # number of different words.

#data_from_training = get_dictionaries(training_set)


#0.3330116130639186




# print(test["CBronte"][:10])


"""
{'CBronte': {'repulse', 1.0472337320966667e-05,
  'fierce', 6.28340239258e-05,
  'mixed', 3.4907791069888885e-05,
  'swimming', 1.0472337320966667e-05,
  'frustrated', 6.981558213977778e-06,
  'impediments', 6.981558213977778e-06, ...... }

  'Eliot' : { '': , '': ,'': ,'': , ....}


"""


#[('Eliot', ['i', 'don', 't', 'know', 'said', 'maggie'])....
#classifier(['i', 'don', 't', 'know', 'said', 'maggie'], words_prob )

# unlabeld_data = for author, words_list in labeled_data
def classifier(unlabeled_data, dictionaries, words_prob_data,  author_prob_data):
	authors_score={}
	for author in words_prob_data.keys():
		result=1*author_prob_data[author]#P(class)
		for target_word in unlabeled_data:
			if target_word in set(dictionaries[2][author]):#dictionaries[2] is simple dict == set(one author words_list)
				result = result*words_prob_data[author][target_word]
			elif target_word not in set(dictionaries[2][author]):
				result = result*words_prob_data[author]["null"]#1/(fd.N()+len(fd))

		authors_score[author]=result			


	#print(authors_score)
	predicted_author=max(authors_score, key=lambda key: authors_score[key])
	#print("Therefore, biggest prob class is ", predicted_author)

	return(predicted_author) #return author's name "Eliot"

#classifier(['i', 'don', 't', 'know', 'said', 'maggie'], words_prob, dict_data)



def get_evaluation(labeled_data, dictionaries, words_prob_data, author_prob_data):
	correct=0
	total=0
	i=0
	#make it unlabeled_data , test_data -> [('Eliot', ['i', 'don', 't', 'know', 'said', 'maggie'])...
	for author, words_list in labeled_data:
		if author==classifier(words_list, dictionaries, words_prob_data,  author_prob_data):
			correct+=1
			total+=1
		else: total+=1
		i+=1
		if i%200==0: print(author)
	return(correct/total)




#extract feature(pattern)
#def feature_extract(words_list):


if __name__ == "__main__":
	training_set = read_corpus("Training_Set.txt")
	test_set= read_corpus("Test_Set.txt")

	ml_class = naive_bayes(training_set)
	#ml_class.words_prob_dict == ml_class.generate_words_prob() <-- right one is calling function. left one is already maden in class.
	classifier(['i', 'don', 't', 'know', 'said', 'maggie'], ml_class.dictionaries, ml_class.words_prob_dict, ml_class.author_prob_dict)
	get_evaluation(test_set, ml_class.dictionaries, ml_class.words_prob_dict,  ml_class.author_prob_dict) # without setword 0.7548169857205212

#type(ml_class.get_dictionaries())
