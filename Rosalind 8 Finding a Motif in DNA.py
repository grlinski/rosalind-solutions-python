

seq = input()
mot = input()
lengseq = len(seq)
lengmot = len(mot)

for i in range(0,lengseq):
    string1 = seq[i:i+lengmot]
    if string1 == mot:
        print(i+1, end=" ")










