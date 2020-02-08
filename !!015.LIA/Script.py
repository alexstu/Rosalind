import sys
import math
argv = sys.argv

k = int(argv[1])
N = int(argv[2])

AA = [0]*(k+1)
Aa = [0]*(k+1)
aa = [0]*(k+1)



for i in range(k+1):

	if (i == 0):
		AA[i] = 0.0
		Aa[i] = 1.0
		aa[i] = 0.0
		continue

	AA[i] = 2*(AA[i-1]*0.5 + 0.25*Aa[i-1] + 0.0*aa[i-1])/(math.pow(2,i))
	Aa[i] = 2*(AA[i-1]*0.5 + 0.5*Aa[i-1] + 0.5*aa[i-1])/(math.pow(2,i))
	aa[i] = 2*(AA[i-1]*0.0 + 0.25*Aa[i-1] + 0.5*aa[i-1])/(math.pow(2,i))

P = Aa[-1]*Aa[-1]*N
print P



#P = (k*(k-1)*(0.5*k*(k-1)) + 0.75*m*(m-1)*(0.5*m*(m-1)) + 0.5*m*n + k*n)/((m+n+k)*(m+n+k-1))

print AA
print Aa
print aa
