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

string_s = ''
string_t=''

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')


line = ''
fasta_list = []
cur_fasta = Fasta('1', '')
seq_len = 0
seq_n = 0

cons_matrix = []
prof_matrix=[]

n_A=0
n_T=0
n_G=0
n_C=0

cons_string = ''
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

seq_len = len(fasta_list[0].seq)
seq_n = len(fasta_list)

print seq_n, seq_len
cons_matrix = [['' for i in xrange(seq_n)] for i in xrange(seq_len)]
prof_matrix = [[0 for i in xrange(4)] for i in xrange(seq_len)]

#print cons_matrix
#print prof_matrix
for i in range(seq_len):
	for j in range(seq_n):
		cur_fasta = fasta_list[j]
		#print cur_fasta.name, cur_fasta.seq
		cons_matrix[i][j] = copy.copy(cur_fasta.seq[i])

#print 

for i in range(seq_len):

	n_A = cons_matrix[i].count('A')
	#print prof_matrix[i]
	n_T = cons_matrix[i].count('T')
	n_G = cons_matrix[i].count('G')
	n_C = cons_matrix[i].count('C')

	#print n_A, n_G, n_C, n_T

	prof_matrix[i][0] = n_A
	prof_matrix[i][3] = n_T
	prof_matrix[i][2] = n_G
	prof_matrix[i][1] = n_C


for i in range(seq_len):

	if (prof_matrix[i][0] == max(prof_matrix[i])):
		cons_string = cons_string + 'A'
		continue
	if (prof_matrix[i][1] == max(prof_matrix[i])):
		cons_string = cons_string + 'C'
		continue
	if (prof_matrix[i][2] == max(prof_matrix[i])):
		cons_string = cons_string + 'G'
		continue
	if (prof_matrix[i][3] == max(prof_matrix[i])):
		cons_string = cons_string + 'T'
		continue

print cons_string

res_string = res_string + cons_string + '\n'
for i in range(4):

	if (i == 0):
		res_string = res_string + 'A:'
	if (i == 1):
		res_string = res_string + 'C:'
	if (i == 2):
		res_string = res_string + 'G:'
	if (i == 3):
		res_string = res_string + 'T:'

	for j in range(seq_len):
		res_string = res_string + ' ' + str(prof_matrix[j][i])

	res_string = res_string + '\n'


print res_string 
fd_out.write(res_string)



fd_in.close()
fd_out.close()
