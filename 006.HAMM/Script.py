import sys

def get_hamming_dist(s1,s2):

	result = 0

	for i in range(len(s1)):
		if (s1[i] != s2[i]):
			result = result + 1 

	return result













argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

string_1 = ''
string_2= ''

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')

string_1 = fd_in.readline()[:-1]
string_2 = fd_in.readline()[:-1]

print get_hamming_dist(string_1, string_2)

#for i in reversed(range(len(string_d))):






#fd_out.write(string_r)

fd_in.close()
fd_out.close()
