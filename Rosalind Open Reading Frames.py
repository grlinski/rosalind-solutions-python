
# http://rosalind.info/problems/orf/

"""
Translate DNA string into proteins



"""
# Codon Dictionary

codons = {"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
"UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
"UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
"UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
"UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
"UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
"UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
"UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
"UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
"UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
"UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
"UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
"UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
"UGG": "W",      "CGG": "R",     "AGG": "R",      "GGG": "G" }








a = input()
lengther = len(a)
stringer = ""

# Complementing DNA Strand
b = a
for i in b:
    if i == "A":
        stringer += "T"
    if i == "G":
        stringer += "C"
    if i == "C":
        stringer += "G"
    if i == "T":
        stringer += "A"
print(stringer)


# Translate into RNA
RNA = ""
for i in a:
    if i == 'A':
        RNA = RNA+"A"
    if i == 'G':
        RNA = RNA+"G"
    if i == 'C':
        RNA = RNA+"C"
    if i == 'T':
        RNA = RNA+"U"














antiRNA = RNA[::-1]

# Then Create the Six Reading Frames

RNA2 = RNA[1:]
RNA3 = RNA[2:]

ARNA2 = antiRNA[1:]
ARNA3 = antiRNA[2:]


readingframes = []

readingframes.append(RNA)#
readingframes.append(RNA2)#
readingframes.append(RNA3)

readingframes.append(antiRNA)
readingframes.append(ARNA2)
readingframes.append(ARNA3)


listprot = []

# Translating the RNA/Reading Frames into Proteins
for i in readingframes:
    lengther = len(i)
    fullprot = ""
    startprot = 0
    print('')
    for j in range(0,lengther,3):
        try:
            holder1 = i[j:j + 3]
            prot = codons[holder1]
            print(prot,end="")
        except:
            pass
        if prot == 'Stop':
            listprot.append(fullprot)
            fullprot = ""
            startprot = 0
        if prot == 'M':
            startprot = 1
        if startprot == 1:
            fullprot = fullprot+prot


print(listprot)
print(listprot)
print(RNA)
print(antiRNA)
print(ARNA2)
print(ARNA3)


"""
DNA
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

RNA
AGCCAUGUAGCUAACUCAGGUUACAUGGGGAUGACCCCGCGACUUGGAUUAGAGUCUCUUUUGGAAUAAGCCUGAAUGAUCCGAGUAGCAUCUCAG

ARNA



"""
