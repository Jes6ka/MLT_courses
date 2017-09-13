#get singular value
from numpy.linalg import svd
from scipy.linalg import svd

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

svdvals(a)
#array([  1.68481034e+01,   1.06836951e+00,   4.41842475e-16])

u,s,v = linalg.svd(a)
origin_a = np.dot(v.transpose(), np.dot(np.diag(s**1), u.transpose())).transpose()

U, s, V = np.linalg.svd(a, full_matrices=True)
S = np.diag(s)
#array([[  1.68481034e+01,   0.00000000e+00,   0.00000000e+00],
#       [  0.00000000e+00,   1.06836951e+00,   0.00000000e+00],
#       [  0.00000000e+00,   0.00000000e+00,   4.41842475e-16]])

#s[0] is most informative? value

#obtaining original matrix is important, or how to do dot. product to get useful information.
#reference : https://stackoverflow.com/questions/31251689/how-to-invert-numpy-matrices-using-singular-value-decomposition
#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.svd.html


#file = austen-sdkf.txt

def flatted(any_list):
	return [a for b in any_list for a in b]

def make_sent_voca_matrix(file):
	whole_voca = []
	sent_voca_list  = []
	num_sent   = 0

	

	with open(file) as f:
		for sent in f:
			whole_voca.appned(sent.split(' '))
			sent_voca_list.append(flatted(sent.split(' ')))
			num_sent+=1

	whole_voca = set(flatted(whole_voca))

	final = []

	
	for voca_in_sent in sent_voca_list:
		if voca_in_sent in whole_voca:


	return(sent_voca_matrix)


	
