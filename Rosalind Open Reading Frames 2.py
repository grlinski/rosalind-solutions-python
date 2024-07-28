
# http://rosalind.info/problems/orf/

"""
Translate DNA string into proteins

# Note need to convert multiple lines into a single string
# I was lazy so I used another program to do it instead.


# Completed!
# I mean except for the multiline thing


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



# Complementing DNA Strand
def complemetary_DNA(a):
    stringer = ""
    for i in a:
        if i == "A":
            stringer += "T"
        if i == "G":
            stringer += "C"
        if i == "C":
            stringer += "G"
        if i == "T":
            stringer += "A"
    return(stringer)


# Converts DNA to RNA
def DNA_To_RNA(a):
    RNA = ""
    for i in a:
        if i == 'A':
            RNA = RNA + "A"
        if i == 'G':
            RNA = RNA + "G"
        if i == 'C':
            RNA = RNA + "C"
        if i == 'T':
            RNA = RNA + "U"
    return RNA


# Converts RNA to Proteins
def RNA_to_Protein(x):
    # Translating the Reading Frames into Proteins
    lengther = len(x)
    fullprot = ""
    startprot = 0
    prot = ""
    listprot = []
    for j in range(0, lengther, 3):
        try:
            holder1 = x[j:j + 3]
            prot = codons[holder1]
        except:
            pass
        if prot == 'Stop':
            listprot.append(fullprot)
            fullprot = ""
            startprot = 0
        if prot == 'M':
            startprot = 1
        if startprot == 1:
            fullprot = fullprot + prot
    return listprot


# Creates Reading Frames
def Reading_Frames(x):
    x2 = x[1:]
    x3 = x[2:]
    return(x,x2,x3)



# Creates Smaller Proteins from Larger Ones that Have multiple starting AAs, which is M
# Returns a list, note that for whatever reason it returns a lot of doubles
# Too lazy to change since it is easy enough to remove duplicates
def create_proteins(x):
    smallerproteins = []
    smallerproteins.append(x)
    for i in range(0,len(x)):
        nostart = x[1:]
        if 'M' in nostart:
            for j in range(0, len(nostart)):
                if nostart[j] == 'M':
                    smallerproteins.append(nostart[j:])
        if 'M' not in nostart:
            break
    return  smallerproteins














# Starting Values
a = input()
lengther = len(a)
stringer = ""
listprot = []





b = complemetary_DNA(a)
RNA1 = DNA_To_RNA(a)
RNA2 = DNA_To_RNA(b)
RNA2 = RNA2[::-1]

RNA1,RNA1RF2,RNA1RF3 = Reading_Frames(RNA1)
RNA2,RNA2RF2,RNA2RF3 = Reading_Frames(RNA2)
listofframes = []

listofframes.append(RNA1)
listofframes.append(RNA2)
listofframes.append(RNA1RF2)
listofframes.append(RNA1RF3)
listofframes.append(RNA2RF2)
listofframes.append(RNA2RF3)

listofproteins = []
for i in listofframes:
    listofproteins.append(RNA_to_Protein(i))

#print(listofproteins)

fulllistofproteins = []
for i in listofproteins:
    for j in i:
        fulllistofproteins.append(create_proteins(j))

#print(fulllistofproteins)
# Creating Smaller Proteins from Proteins

# Turning a List of List into a List
simplelist = []
for i in fulllistofproteins:
    for j in i:
        x = j
        simplelist.append(x)

# Removing Duplicate Info and Blank spots
simplelist = set(simplelist)
simplelist = list(simplelist)
simplelist.remove('')


for i in simplelist:
    print(i)



"""
DNA
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

RNA
AGCCAUGUAGCUAACUCAGGUUACAUGGGGAUGACCCCGCGACUUGGAUUAGAGUCUCUUUUGGAAUAAGCCUGAAUGAUCCGAGUAGCAUCUCAG

ARNA



"""
