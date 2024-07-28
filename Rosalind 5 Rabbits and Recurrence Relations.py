
a,b = input().split()
n = int(a)
k = int(b)

p0 = 1
p1 = 1
p2 = 1
off = 1

#   5 3
# 1 1 4 7 19

print(p0)

for i in range(0,n-1):
    print(p0)
    off = p1*k
    #print("p0", p0, "p1", p1, "p2", p2, "Off", off)

    p2 = p1
    p1 = p0
    p0 = p0 + off




























