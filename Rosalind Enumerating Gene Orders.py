# Done
# http://rosalind.info/problems/perm/
import itertools

# Basically take in an int, count and list all permutations
# Uses intertools

"""
Ex:
Input 2
Output:
2
12
21



"""
# Function I previously created
def permutations(n,k):
    top = 1
    b1 = 1
    b2 = 1
    for i in range(1,n+1):
        top = top*i
    for i in range(1,n-k+1):
        b2 = b2*i
    answer = int(top/b2)
    return answer

list2 = []
x = int(input())
list1 = []

print(permutations(x,x))

for i in range(1,x+1):
    list1.append(i)

r = list(itertools.permutations(list1))
for i in r:
    y = str(i)
    z = y.strip('(').strip(')').replace(',', '')
    list2.append(z)
    print(z)


























