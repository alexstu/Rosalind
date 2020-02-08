import sys
import copy

argv = sys.argv

#print argv

in_file = argv[1]
out_file = argv[2]

fd_in = open(in_file, 'rb')
fd_out = open(out_file, 'wb')

res_string = ''

N_AA_AA = 17591.0
N_AA_Aa = 19630.0
N_AA_aa = 17100.0
N_Aa_Aa = 18662.0
N_Aa_aa = 19019.0
N_aa_aa = 17075.0


Exp_AA_AA = 2*1.0
Exp_AA_Aa = 2*1.0
Exp_AA_aa = 2*1.0
Exp_Aa_Aa = 2*0.75
Exp_Aa_aa = 2*0.5
Exp_aa_aa = 2*0.0

Exp = N_AA_AA*Exp_AA_AA + N_AA_Aa*Exp_AA_Aa + N_AA_aa*Exp_AA_aa + N_Aa_Aa*Exp_Aa_Aa + N_Aa_aa*Exp_Aa_aa + N_aa_aa*Exp_aa_aa
print Exp
#print N_aa_aa, N_AA_Aa*Exp_AA_Aa, N_AA_aa*Exp_AA_aa, N_Aa_Aa*Exp_Aa_Aa, N_Aa_aa*Exp_Aa_aa, N_aa_aa+Exp_aa_aa



#print res_string


fd_out.write(res_string)



fd_in.close()
fd_out.close()
