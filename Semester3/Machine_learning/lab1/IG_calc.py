import numpy as np

data_struct = {'attr1': 
	{'sp1': 
{'austen': {'small': 23, 'big': 402},
'milton': {'small': 52, 'big': 387}   }
	}
}


a = data_struct
temp = []
for attr in a:
	for sp in a[attr]:
		for c in a[attr][sp]:
			temp.append(tuple(a[attr][sp][c].values()))
#a looks like 
#[{'austen': {'small': 23, 'big': 402}, 
# 'milton': {'small': 52, 'big': 387},
#  other_author : {small...			}	}    ]

#temp = [(23, 402), (52, 387), ...]


def entropy(p):
	calc = p*np.log2(p)+(1-p)*np.log2(1-p)
	return(-calc)

def gain_calculate(temp): #group1 = (23, 402), group2 = (52, 387)
	total_small = 0
	total_big 	= 0
	sum_each_prob_entropy = 0

	for small_value, big_value in temp:
		print(small_value, big_value, entropy(small_value/big_value))
		if small_value <= big_value:
			sum_each_prob_entropy += entropy(small_value/(small_value+big_value))
		else : sum_each_prob_entropy += entropy(big_value/(small_value+big_value))
		total_small += small_value
		total_big 	+= big_value
	
	#Now, calculate real IG(Information Gain)
	print('head entropy is',entropy(total_small/total_big))
	IG = entropy(total_small/total_big)- sum_each_prob_entropy
	return(IG)
