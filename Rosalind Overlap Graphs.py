
list1 = []
counter = 0

while True:
    line = input()
    if line == '':
        break
    line2 = line.strip('>')

    if counter == 0:
        list1.append(line2)
    if counter == 1:
        line3 = line2
    if counter == 2:
        line3 = line3+line2
        list1.append(line3)

    counter = counter+1
    if counter == 3:
        counter = 0
print('')



# Create a unique end matching key for every value
# Ex AAA = 111, ATC = 132
# list1.insert(5, “stopgap”)

masterlist = []

for i in list1:
    holder = i
    if 'Rosalind' in i:
        masterlist.append(i)
    else:
        a = i[0:3]
        b = i[-3:]
        first = ""
        last = ""
        for i in range(0,3):
            if a[i] == 'A':
                first += "1"
            if a[i] == 'T':
                first += '2'
            if a[i] == 'G':
                first += "3"
            if a[i] == 'C':
                first += '4'
        for i in range(0, 3):
            if b[i] == 'A':
                last += "1"
            if b[i] == 'T':
                last += '2'
            if b[i] == 'G':
                last += "3"
            if b[i] == 'C':
                last += '4'
        #masterlist.append(holder)
        masterlist.append(first)
        masterlist.append(last)

answerlist = []
vs1 = ''
vs2 = ''
answer = ''
for i in range(1,len(masterlist),3):
    first = masterlist[i]
    second = masterlist[i+1]
    for j in range(1, len(masterlist), 3):
        third = masterlist[j]
        fourth = masterlist[j+1]
        if  (first == fourth) or (second == third):
            vs1 = masterlist[i-1]
            vs2 = masterlist[j-1]
            num1 = int(vs1[-4:])
            num2 = int(vs2[-4:])

            if (vs1 != vs2) and num1 > num2:
                answer = vs1 + " " + vs2
                answerlist.append(answer)
            if (vs1 != vs2) and num2 > num1:
                answer = vs2 + " " + vs1
                answerlist.append(answer)


answerlist = set(answerlist)
answerlist = list(answerlist)


for i in answerlist:
    print(i)

"""

>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG





if (first == third) or (first == fourth) or (second == third) or (second == fourth):

"""



