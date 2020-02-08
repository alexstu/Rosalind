import sys
import copy


class Fasta:
    name = ""
    seq = ""
    def __init__(self, name, seq):
        self.name = name
        self.seq = seq





argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

k = 3

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')


line = ''
fasta_list = []
cur_fasta = Fasta('1', '')

res_string = ''

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
		cur_fasta_i = fasta_list[i]

		for j in range(len(fasta_list)):
			cur_fasta_j = fasta_list[j]

			if (i == j):
				continue

			#print cur_fasta_i.name, cur_fasta_j.name

			if (cur_fasta_i.seq[-3:] == cur_fasta_j.seq[:3]):
				res_string = res_string + cur_fasta_i.name[1:] + ' ' + cur_fasta_j.name[1:] + '\n'

print res_string


fd_out.write(res_string)



fd_in.close()
fd_out.close()
