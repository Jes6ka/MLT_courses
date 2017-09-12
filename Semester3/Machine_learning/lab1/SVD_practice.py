#get singular value
from scipy.linalg import svdvals
from scipy.linalg import svd

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

svdvals(a)
#array([  1.68481034e+01,   1.06836951e+00,   4.41842475e-16])

u,s,v = linalg.svd(a)
origin_a = np.dot(v.transpose(), np.dot(np.diag(s**1), u.transpose())).transpose()

S = np.diag(s)
#array([[  1.68481034e+01,   0.00000000e+00,   0.00000000e+00],
#       [  0.00000000e+00,   1.06836951e+00,   0.00000000e+00],
#       [  0.00000000e+00,   0.00000000e+00,   4.41842475e-16]])

#s[0] is most informative? value

#obtaining original matrix is important, or how to do dot. product to get useful information.
#reference : https://stackoverflow.com/questions/31251689/how-to-invert-numpy-matrices-using-singular-value-decomposition
