## Python 2.6+
from __future__ import print_function

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()
fib(2117)
