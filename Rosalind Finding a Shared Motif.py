

# Finding a Shared Motif
# http://rosalind.info/problems/lcsm/
# Completed

seq = []
s= ''
while True:
    x = input()
    if x == "":
        break
    elif '>' in x:
        seq.append(s)
        s = ''
    else:
        s = s + x
seq.append(s)

# The First Entry is blank so may as well remove
del(seq[0])
# Each Sequence is an Entry in Seq
# Now create SS from the first entry.
ss = []

# Maybe Try 10bp to 4bp
# Also should probably use a set


subset = set()


# Note, narrow this range to get a faster answer
# ie Increase the bottom value, if nothing gets returned lower the bottom value.
for j in range(150,250):
    for i in range(len(seq[0])-j):
        try:
            x = seq[0]
            s = x[i:i+j]
            subset.add(s)
            ss.append(s)
        except:
            pass


# Convert set to List
sublist = list(subset)
todelete = []
count = 0
print(len(sublist))
for sub in sublist:
    for i in seq:
        if sub in i:
            pass
        else:
            todelete.append(sub)
            break

for i in todelete:
    sublist.remove(i)
sublist.sort()

for i in sublist:
    print(i)

print(len(sublist))

ans = ''
largest = 0
for i in sublist:
    length = len(i)
    if length > largest:
        largest = length
        ans = i

print(largest)
print(ans)




