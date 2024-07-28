

# Problem with pairings of numbers for unknown reasons
# I have the same amount of pairings and the same amount of the name type
# But apparantly with the wrong partners





# Three Lists, Name of Sequence,
name = []
leftend = []
rightend = []

while True:
    t = input()
    if t == "":
        break
    s = input()
    z = input()
    left = s[:3]

    r1 = z[-3:]
    #right = r1[::-1]
    right =r1
    t = t[1:]
    name.append(t)
    leftend.append(left)
    rightend.append(right)


ans = []
ansset = set()

print(name)
print(leftend)
print(rightend)


# Compare Left To Right Ends
for i in range(len(leftend)):
    #del(rightend[0])
    for j in range(len(rightend)):
        if i == j:
            pass
        elif rightend[j] == leftend[i]:
            numj = int(name[j][-4:])
            numi = int(name[i][-4:])
            if numj < numi:
                s = name[j] + " " + name[i]
                ans.append(s)
                ansset.add(s)
            else:
                s = name[i] + " " + name[j]
                ans.append(s)
                ansset.add(s)


print(len(ans))
ans.sort()

for i in ans:
    print(i)













