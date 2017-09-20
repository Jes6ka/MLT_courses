#get singular value
from numpy.linalg import svd
from scipy.linalg import svd
from scipy.sparse.linalg import svds
from sklearn.utils.extmath import randomized_svd
from sklearn.decomposition import TruncatedSVD
import numpy as np

#http://matpalm.com/lsa_via_svd/eg1.html
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
k = svd1.fit_transform(c3)
print(svd1.inverse_transform(k))

"""
[ 0.78879092  0.16292015]
[ 3040.17551124   627.9304694 ]
[ 184.05230749   61.67047677]
[[ 149.75573697  -24.62863956]
 [  27.29485698  -15.95208625]
 [  99.77020098   48.1286227 ]
 [  27.32866265  -24.93239495]
 [   0.70895891    0.91870795]
 [   1.41791781    1.83741589]]
[[  81.24762458  103.17242526   75.66759477    7.87654171]
 [  17.48840164   25.7787365     5.3533388    -0.65771528]
 [  39.04059737   29.4710476    97.91647094   17.03264973]
 [  19.60496609   31.26230685   -1.2358611    -2.29482952]
 [   0.14258919   -0.1414542     1.12030055    0.22634647]
 [   0.28517839   -0.28290839    2.24060111    0.45269294]]

"""

v = np.transpose(vt)
VS = np.dot(v,s)
print(v, '\n\n', s, '\n\n',np.dot(v,s), 
      '\n\n',np.round(v*s, 2))
US = np.round(u*s, 2)
print('\n',US)
"""
v : [[ 0.50408518 -0.23379191 -0.818938  ]
 [ 0.58888056 -0.60840479  0.53131639]
 [ 0.62633092  0.73609646  0.13741403]
 [ 0.08262798  0.18261149  0.16781191]] 

s :  [ 184.05230749   61.67047677   26.58449612] 

 [  56.58892848   84.98899167  164.32615406   30.93080329] 

VS: [[  92.78  -14.42  -21.77]
 [ 108.38  -37.52   14.12]
 [ 115.28   45.4     3.65]
 [  15.21   11.26    4.46]]

US: [[ 149.76  -24.63   -8.2 ]
 [  27.29  -15.95   -4.08]
 [  99.77   48.13    6.85]
 [  27.33  -24.93   23.99]
 [   0.71    0.92    0.31]
 [   1.42    1.84    0.61]]
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
