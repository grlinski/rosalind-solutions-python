

# RNA Splicing
# http://rosalind.info/problems/splc/

import RGF

# First Create a list of RNA Sequences

###############
s = ""
while True:
    x = input()
    if x == "":
        break
    s = s+x

s +='>'
ns = ''
seq = []
for i in s:
    if i == '>':
        seq.append(ns)
        ns = ""
    elif i == 'A' or i == 'G' or i == 'C' or i == 'T':
        ns = ns+i
del(seq[0])


# seq contains all the RNA sequences

################

for i in seq:
    x = RGF.DNA_to_RNA(x)

















