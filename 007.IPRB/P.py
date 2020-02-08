import sys

m = 2
n = 2
k = 2

def fact(x):

	result = 1

	if ((x == 0) or (x == 1)):
		result = 1
	else:
		result = x*fact(x-1)

	return result

P = (k*(k-1)*(0.5*k*(k-1)) + 0.75*m*(m-1)*(0.5*m*(m-1)) + 0.5*m*n + k*n)/((m+n+k)*(m+n+k-1))
print P
