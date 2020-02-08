import sys

argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

string_s = ''
string_t=''

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')

string_s = fd_in.readline()[:-1]
string_t = fd_in.readline()[:-1]
sub_string_cur = ''
pos_array = []
res_string = ''


for i in range(len(string_s)-len(string_t)+1):
	sub_string_cur = string_s[i:i+len(string_t)]
	print sub_string_cur, string_t
	if (sub_string_cur == string_t):
		#print i
		pos_array.append(str(i+1))

#print string_

res_string = ' '.join(pos_array)
fd_out.write(res_string)

fd_in.close()
fd_out.close()
