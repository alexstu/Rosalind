import sys


argv = sys.argv

#print argv

int1 = int(argv[1])
int2 = int(argv[2])


def Fib(n, k):

	result = 0

	if (n == 1):
		result = 1

	if (n == 2):
		result = 1

	if (n > 2):
		result = Fib(n-1, k) + k*Fib(n-2, k)

	return result

print Fib(int1,int2)




