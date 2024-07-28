
string2 =""
lister = []
counter = 0
stopword = "Rosalind"


while True:
    string1 = input()
    container = [string1]
    if string1 == "":
        break

    string2 = string2 + string1

string3 = ""
seqleng = 0
x = []
string2 = string2+ ">"


for i in string2:
    string3 = string3 + i
    if i == ">":
        print()
        seqleng = len(string3)
        x.append(string3)
        #print(string3)
        string3 = ""
    else:
        print(i, end="")
print(string3)
print(seqleng)
del(x[0])
print(x)

seqlengx = len(x)
seqleng2 = 0


A = []
G = []
T = []
C = []

filler  = x[0]
fleng = len(filler)
k = 0

for k in range(0,fleng):
    A.append(0)
    G.append(0)
    T.append(0)
    C.append(0)

print(A)
print(G)
print(T)
print(C)




for i in range(0,seqlengx):
    string1 = x[i]
    seqleng1 = len(string1)
    for j in range(0,seqleng1):
        if string1[j] == "A":
            A[j] +=1
        if string1[j] == "G":
            G[j] +=1
        if string1[j] == "T":
            T[j] +=1
        if string1[j] == "C":
            C[j] +=1





# So far everything works, just find the highest amount in each and put into new list
answer = ""

for y in range(0, seqleng1):
    AX = A[y]
    GX = G[y]
    TX = T[y]
    CX = C[y]
    maxer = max(AX,GX,TX,CX)
    if AX >= maxer:
        answer = answer+"A"
    elif GX >= maxer:
        answer = answer+"G"
    elif TX >= maxer:
        answer = answer+"T"
    elif CX >= maxer:
        answer = answer+"C"



print(A)
print(G)
print(T)
print(C)
A = A[13:-1]
G = G[13:-1]
T = T[13:-1]
C = C[13:-1]

print(A)
print(answer)
answer = answer[13:-1]

print(A)
volus = A
print(volus)
print("C3")
# They want the answer A C G T
# I have everything I need just need to format properly

for j in answer:
    print(j, end=" ")


k = 0
stringV = ""
stringG = ""
stringT = ""
stringC = ""

for q in volus:
    stringV = stringV+str(q)
    stringV = stringV + " "
    print(q)

for q in G:
    stringG = stringG+str(q)
    stringG = stringG + " "
for q in C:
    stringC = stringC+str(q)
    stringC = stringC + " "
for q in T:
    stringT = stringT+str(q)
    stringT = stringT + " "


print(answer)
print("A:", stringV)
print("C:", stringC)
print("G:", stringG)
print("T:", stringT)



# No damned idea why the list A doesn't work well
# That's why I transfered it to volus and did other things.



"""






"""


