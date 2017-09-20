#get singular value
from numpy.linalg import svd
from scipy.linalg import svd
from scipy.sparse.linalg import svds
from sklearn.utils.extmath import randomized_svd
from sklearn.decomposition import TruncatedSVD
import numpy as np

#http://matpalm.com/lsa_via_svd/eg1.html
#http://matpalm.com/lsa_via_svd/eg2.html
c1 = [[2,2,0,0],[2,2,0,0],[3,3,0,0],[0,0,2,2],[0,0,1,1],[0,0,2,2]]
c2 = [[87,99,76,0],[24,23,0,20],[34,33,98,22],[0,44,2,2],[0,0,1,1],[0,0,2,2]]

from sklearn.utils.extmath import randomized_svd
u, s, vt = randomized_svd(np.array(c3), 
                              n_components=3,
                              n_iter=10,
                              random_state=None)


from sklearn.decomposition import TruncatedSVD
svd1 = TruncatedSVD(n_components=2)
svd1.fit(c3)



print(u,'\n',s,'\n',vt)

print(svd1.explained_variance_ratio_)
print(svd1.explained_variance_)
print(svd1.singular_values_) 
print(svd1.fit_transform(c3))
#fit_trnansform means US

#svd1.inverse_transform(svd1) this not works.
k = svd1.fit_transform(c3)
print(svd1.inverse_transform(k))#reconstrunct into original size of matrix -c1- in this case

"""
[ 0.64634146  0.35365854]
[ 2.94444444  1.61111111]
[ 5.83095189  4.24264069]
[[  2.82842712e+00  -2.80896409e-16]
 [  2.82842712e+00   9.47214882e-17]
 [  4.24264069e+00   6.52381468e-17]
 [ -3.70419970e-32   2.82842712e+00]
 [ -1.08947050e-33   1.41421356e+00]
 [ -2.17894100e-33   2.82842712e+00]]
[[  2.00000000e+00   2.00000000e+00   2.18508690e-16   2.18508690e-16]
 [  2.00000000e+00   2.00000000e+00   1.37236235e-15   1.37236235e-15]
 [  3.00000000e+00   3.00000000e+00   1.80885418e-16   1.80885418e-16]
 [  6.86635020e-16   6.86635020e-16   2.00000000e+00   2.00000000e+00]
 [  3.43317510e-16   3.43317510e-16   1.00000000e+00   1.00000000e+00]
 [  6.86635020e-16   6.86635020e-16   2.00000000e+00   2.00000000e+00]]

"""

v = np.transpose(vt)
VS = np.dot(v,s)# np.round(v*s, 2) is proper matrix
print(v, '\n\n', s, '\n\n',np.dot(v,s), 
      '\n\n',np.round(v*s, 2))
US = np.round(u*s, 2)
print('\n',US)

#Reconstruct Matrix after dimension reduction.
print('\n',np.round(np.dot(US, vt), 3))
#print('\n',np.dot(US, vt))
"""
[[  7.07106781e-01  -3.16096536e-19   9.47403935e-04  -7.07106147e-01]
 [  7.07106781e-01  -3.16096536e-19  -9.47403935e-04   7.07106147e-01]
 [  3.16096536e-19   7.07106781e-01  -7.07106147e-01  -9.47403935e-04]
 [  3.16096536e-19   7.07106781e-01   7.07106147e-01   9.47403935e-04]] 

 [  5.83095189e+00   4.24264069e+00   4.37906163e-47  -0.00000000e+00] 

 [ 4.12310563  4.12310563  3.          3.        ] 

 [[ 4.12 -0.    0.    0.  ]
 [ 4.12 -0.   -0.   -0.  ]
 [ 0.    3.   -0.    0.  ]
 [ 0.    3.    0.   -0.  ]]

 [[ 2.83 -0.   -0.   -0.  ]
 [ 2.83  0.    0.   -0.  ]
 [ 4.24 -0.   -0.    0.  ]
 [ 0.    2.83 -0.    0.  ]
 [ 0.    1.41  0.    0.  ]
 [ 0.    2.83  0.    0.  ]]
 
[[ 2.001  2.001  0.     0.   ]
 [ 2.001  2.001  0.     0.   ]
 [ 2.998  2.998  0.     0.   ]
 [-0.    -0.     2.001  2.001]
 [-0.    -0.     0.997  0.997]
 [-0.    -0.     2.001  2.001]]
"""




u,s,v = linalg.svd(a)
origin_a = np.dot(v.transpose(), np.dot(np.diag(s**1), u.transpose())).transpose()

U, s, V = np.linalg.svd(a, full_matrices=True)
S = np.diag(s)
#array([[  1.68481034e+01,   0.00000000e+00,   0.00000000e+00],
#       [  0.00000000e+00,   1.06836951e+00,   0.00000000e+00],
#       [  0.00000000e+00,   0.00000000e+00,   4.41842475e-16]])


#obtaining original matrix is important, or how to do dot. product to get useful information.
#reference : https://stackoverflow.com/questions/31251689/how-to-invert-numpy-matrices-using-singular-value-decomposition
#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.svd.html


#add this when defining features(Matrix-SVD)

terms = ['a','b','c','d','e','f','g','h']
doc1 = ['a','a','c']
doc2 = ['b','e','e']
doc3 = ['d', 'f', 'g']
doc4 = ['g', 'e', 'h']


     
#https://stackoverflow.com/questions/31523575/get-u-sigma-v-matrix-from-truncated-svd-in-scikit-learn
