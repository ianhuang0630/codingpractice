def fib(n):
	coll = {}
	return fib_rec(n, coll)

def fib_rec(n, coll):

	if n <= 1:
		return n
	
	else:
		if (n-1) not in coll:
			coll[n-1] = fib_rec(n-1, coll)
		if (n-2) not in coll:
			coll[n-2] = fib_rec(n-2, coll)

		return coll[n-1] + coll[n-2]
