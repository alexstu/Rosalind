import sys

argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

string_d = ''
string_r=''

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')

string_d = fd_in.readline()

for i in reversed(range(len(string_d))):

	if (string_d[i] == 'A'):
		string_r = string_r +  'T'
	if (string_d[i] == 'T'):
		string_r = string_r +  'A'
	if (string_d[i] == 'G'):
		string_r = string_r +  'C'
	if (string_d[i] == 'C'):
		string_r = string_r +  'G'



print string_r

fd_out.write(string_r)

fd_in.close()
fd_out.close()
