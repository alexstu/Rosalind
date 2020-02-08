import sys
import copy

class Fasta:
    name = ""
    seq = ""
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq




def get_gc(string):

	result = 0.0

	result = (float(string.count('C')) + float(string.count('G')))/float(len(string))

	return result





argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

string_d = ''
string_r=''

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')

line = ''
fasta_list = []
cur_fasta = Fasta('1', '')


cur_gc = 0.0
best_gc = -1.0
best_name = ''




all_lines = fd_in.readlines()
for i in range(len(all_lines)):
	line = all_lines[i]
	if (line[0] == '>'):
		if (i != 0):
			fasta_list.append(copy.copy(cur_fasta))
			cur_fasta = Fasta('1', '')
		cur_fasta.name = line[:-1]
	else:
		cur_fasta.seq = cur_fasta.seq + line[:-1]
		if (i == len(all_lines)-1):
			fasta_list.append(copy.copy(cur_fasta))



for i in range(len(fasta_list)):

	cur_fasta = fasta_list[i]
	print cur_fasta.name, cur_fasta.seq

	cur_gc = get_gc(cur_fasta.seq)
	if (cur_gc > best_gc):
		best_name = cur_fasta.name
		best_gc = cur_gc

print best_name[1:]
print best_gc*100



fd_out.write(string_r)

fd_in.close()
fd_out.close()
