'''def Fibb(n, m):

	result = 0

	if (n == 1):
		result = 1

	if (n == 2):
		result = 1

	if ((n > 2) and (n <= m)):
		result = Fibb(n-1, m) + Fibb(n-2, m)

	if (n == m+1):
		result = Fibb(n-1, m) + Fibb(n-2, m) - Fibb(1, m) 

	if (n > m + 1):
		result = Fibb(n-1, m) + Fibb(n-2, m) - Fibb(n-m-1, m) 
	#print result
	return result

print Fibb(98, 18)'''

n = 96
m = 17
ff = [0]*n
for i in range(n):

	if (i == 0):
		ff[i] = 1

	if (i == 1):
		ff[i] = 1

	if ((i > 1) and (i < m)):
		ff[i] = ff[i-1] + ff[i-2]

	if (i == m):
		ff[i] = ff[i-1] + ff[i-2] - ff[0]

	if (i > m):
		ff[i] = ff[i-1] + ff[i-2] - ff[i-m-1]

print ff
	
