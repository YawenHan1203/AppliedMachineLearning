def fib(n, a=0, b=1):
	if n == 0: # edge case
		return a
	if n == 1: # usual base case
		return b
	return fib(n-1, b, a+b)