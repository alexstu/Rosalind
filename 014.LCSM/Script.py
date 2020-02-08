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

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')


line = ''
fasta_list = []
cur_fasta = Fasta('1', '')

#cur_fasta_i = Fasta('1', '')
#cur_fasta_j = Fasta('1', '')



#cur_subst_array_ij = []
#subst_matrix = []
#cur_substr = ''

res_string = ''
#set_array = []
#sett = set('0')
#all_substr = []

substr_array = []
del_ind = []
filt_substr_array = []


best_substr = ''




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



#subst_matrix = [[[] for i in xrange(len(fasta_list))] for i in xrange(len(fasta_list))]

for ii in range(len(fasta_list[0].seq)):
	for jj in range(len(fasta_list[1].seq)):
		if (fasta_list[0].seq[ii] != fasta_list[1].seq[jj]):
			continue
		for kk in range(min(len(fasta_list[0].seq), len(fasta_list[1].seq))):
			if (fasta_list[0].seq[ii:ii+kk] != fasta_list[1].seq[jj:jj+kk]):
				break
			substr_array.append(fasta_list[0].seq[ii:ii+kk])

print substr_array

filt_substr_array = copy.copy(substr_array)
ind = 0
for i in range(len(fasta_list)):
	for k in range(len(substr_array)):
		if ((substr_array[k] in fasta_list[i].seq) == False):
			#del_ind.append(k)
			del filt_substr_array[k-ind]
			ind = ind + 1

#print del_ind
#for k in range(len(substr_array)):
#	if ((k in del_ind) == False):
#		filt_substr_array.append(substr_array[k])

#print filt_substr_array
#for i in range(len(filt_substr_array)):
#	if (len(filt_substr_array[i]) > len(best_substr)):
#		best_substr = filt_substr_array[i]

print filt_substr_array
for i in range(len(filt_substr_array)):
	if (len(filt_substr_array[i]) > len(best_substr)):
		best_substr = filt_substr_array[i]


print best_substr



#for i in range(len(fasta_list)):
#	cur_fasta_i = fasta_list[i]
#
#	for j in range(len(fasta_list)):
#		cur_fasta_j = fasta_list[j]
#
#		if (i >= j):
#			continue
#
#		print i, j
#
#		for ii in range(len(cur_fasta_i.seq)):
#			for jj in range(len(cur_fasta_j.seq)):
#
#				if (cur_fasta_i.seq[ii] != cur_fasta_j.seq[jj]):
#					continue
#
#				for kk in range(min(len(cur_fasta_i.seq), len(cur_fasta_j.seq))):
#					if (cur_fasta_i.seq[ii:ii+kk] != cur_fasta_j.seq[jj:jj+kk]):
#						break
#					subst_matrix[i][j].append(cur_fasta_i.seq[ii:ii+kk])

						
#print subst_matrix

#for i in range(len(fasta_list)):
#	for j in range(len(fasta_list)):
#
#		if (i >= j):
#			continue
#		print i, j
#
#		set_array.append(set(subst_matrix[i][j]))


#sett = set_array[0]
#for i in range(len(set_array)):
#	sett = sett & set_array[i]


#all_substr = list(sett)
#for i in range(len(all_substr)):
#	if (len(all_substr[i]) > len(best_substr)):
#		best_substr = all_substr[i]

#print best_substr



fd_out.write(best_substr)



fd_in.close()
fd_out.close()
