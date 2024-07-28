
string2 =""
lister = []
counter = 0

while True:
    string1 = input()

    if string1 == "":
        break

    string2 = string2 + string1

lengther = len(string2)

string3 = ""

for i in string2:
    if i == ">":
        print()

        lister.append(string3)
        string3 = ""
    else:
        string3 = string3+i

del(lister[0])
highest = 0.0
title = ""

for i in lister:
    string3 = i
    gc = 0.0
    lengther = float(len(string3))
    lengther = lengther-13
    for j in string3:
        if j == "G" or j == "C":
            gc +=1
    gc=gc/lengther*100
    if gc > highest:
        highest = gc
        title = string3[0:13]

print(title)
print(highest)






