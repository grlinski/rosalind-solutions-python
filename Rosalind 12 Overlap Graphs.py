# First put each Rosalind File into a list


list1 = []
string1 = ""
string2 = ""
string3 = ""


while True:
    string1 = input()
    if string1 == "":
        break

    string2 = string2 + string1


for i in string2:
    string3 = string3+i

    if i == ">":
        list1.append(string3)
        string3 = ""

del(list1[0])
#print(list1)



# Second create a profile for each of the overlaps.

"""

A large problem is determining how long overlaps can be

Example AAA = 111, 
ATGC
T = 222
G = 333
C = 444
So
TAG = 213

"""
list2 = []
string3 = ""

for i in list1:
    string3 = ""
    string1 = i
    string2 = string1[13:-1]
    for r in range(0, len(string2)):
        j = string2[r]
        if j == "A":
            string3 = string3+"1"
        elif j == "T":
            string3 = string3+"2"
        elif j == "G":
            string3 = string3+"3"
        elif j == "C":
            string3 = string3+"4"
    list2.append(string3)

#print(list2)

# So now I have two lists, list1 and list2
# list1 has the letters and Ros title, and list2 has the numbers
# Problem, strings are different lengths

original = list2
original0 = []
reversed = []
reversed0 = []
middle0 = []
middle0R = []
# May be easier to jam 0s into the middle of each item/string.
# Then I only need a single list to compare

zeroer = 0
largest = 0

for i in original:
    string1 = i
    string2 = string1[::-1]
    reversed.append(string2)



for i in list2:
    r = len(i)
    largest = max(zeroer, r)


for i in original:
    string1 = i
    r = len(string1)
    q = largest-r
    for j in range(0,q):
        string1 = string1+"0"
    original0.append(string1)

# Creates a list with zeroes in the middle
for i in original:
    string1 = i
    r = len(string1)
    q = largest-r
    h = int(len(string1)/2)
    string2 = string1[0:h]
    string3 = string1[h:]
    for j in range(0,q):
        string2 = string2+"0"
    string2 = string2+string3
    middle0.append(string2)

for i in reversed:
    string1 = i
    r = len(string1)
    q = largest-r
    h = int(len(string1)/2)
    string2 = string1[0:h]
    string3 = string1[h:]
    for j in range(0,q):
        string2 = string2+"0"
    string2 = string2+string3
    middle0R.append(string2)





#print(original)
#print(original0)
#print(reversed)
#print(reversed0)


# Now I need to compare the lists and their components to eachother
# Actually I can just compare the 0 lists to eachother


# The shorter the length of z the more a and b match
# Except when it equals 0, then it's the same sequence
# i and j represent the positions of the sequences in the original list.
"""
largeststringlength = len(original0[0])
lengther = len(original0)

for i in range(0, lengther):
    x = int(original0[i])
    for j in range(0, lengther):
        y = int(original0[j])
        a = max(x,y)
        b = min(x,y)
        z = a-b
        t = str(z)
        q = len(t)
        if q < largeststringlength and z != 0:
            print (z)
"""

#print(middle0)

# Probably Easiest to compare middle0 to itself. Prevents repeats and such

answerlist = []
largeststringlength = len(original0[0])-3
lengther = len(original0)
string4 = ""
string2 = ""
string3 = ""

# Compares middle0 vs. middle0
for i in range(0, lengther):
    x = int(middle0[i])
    for j in range(0, lengther):
        y = int(middle0[j])
        a = max(x,y)
        b = min(x,y)
        z = a-b
        t = str(z)
        q = len(t)
        if q < largeststringlength and z != 0:
            #print (z)
            string2 = list1[i]
            string3 = list1[j]
            string4 = string2[0:13]+" "+string3[0:13]
            answerlist.append(string4)

# Compares middle0 vs. middle0R
for i in range(0, lengther):
    x = int(middle0[i])
    for j in range(0, lengther):
        y = int(middle0R[j])
        a = max(x,y)
        b = min(x,y)
        z = a-b
        t = str(z)
        q = len(t)
        if q < largeststringlength and z != 0:
            #print (z)
            string2 = list1[i]
            string3 = list1[j]
            string4 = string2[0:13]+" "+string3[0:13]
            answerlist.append(string4)

# Compares middle0R vs. middle0R
for i in range(0, lengther):
    x = int(middle0R[i])
    for j in range(0, lengther):
        y = int(middle0R[j])
        a = max(x,y)
        b = min(x,y)
        z = a-b
        t = str(z)
        q = len(t)
        if q < largeststringlength and z != 0:
            #print (z)
            string2 = list1[i]
            string3 = list1[j]
            string4 = string2[0:13]+" "+string3[0:13]
            answerlist.append(string4)

print(answerlist)
print(middle0)
print(middle0R)

answerlist.sort()
print()
for i in answerlist:
    print (i)


"""
Unused

for i in reversed:
    string1 = i
    r = len(string1)
    q = largest-r
    for j in range(0,q):
        string1 = string1+"0"
    reversed0.append(string1)














"""


