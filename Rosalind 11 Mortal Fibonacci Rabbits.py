
#Copied From Rosalind 5

a,b = input().split()
n = int(a)
m = int(b)
k = 2

#Append to this to keep track of how many die
deadlist = []
for i in range(0,m):
    deadlist.append(0)

# k = Offspring Produced

# n = Number of months to run for
# m = How many months the rabbits live for
# Basically the same as before except the rabbits die


p0 = 1
p1 = 1
p2 = 1
off = 1

dlleng = 0
dead = 0

#   5 3
# 1 1 4 7 19
checker1 = []
checker2 = []


print(p0)

for i in range(0,n-1):
    dleng = len(deadlist)-m
    dead = deadlist[dleng]
    checker1.append(p0)

    print("p0: ", p0, "Dead: ", dead, "Dif: ", (p0-dead))
    p0 = p0-dead

    checker2.append(p0)
   # print("D:", dead)
   # print(p0)
    off = p1*k
    deadlist.append(off)
    #print("p0", p0, "p1", p1, "p2", p2, "Off", off)

    p2 = p1
    p1 = p0
    p0 = p0 + off





print(deadlist)
print(checker1)
print(checker2)




# 6 3
# 4














