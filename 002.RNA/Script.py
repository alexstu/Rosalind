import sys

argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

string_d = 'GATGGAACTTGACTACGTAAATT'
string_r=''

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')

string_d = fd_in.readline()

for i in range(len(string_d)):

	if (string_d[i] != 'T'):
		string_r = string_r +  string_d[i]
	else:
		string_r = string_r + 'U'

print string_r

fd_out.write(string_r)

fd_in.close()
fd_out.close()
