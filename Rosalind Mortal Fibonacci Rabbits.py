
# http://rosalind.info/problems/fibd/

# Takes a number x and generates that many fib numbers into a list
def fibbonacci_generator(months, lifespan):
    list_of_fib =[]
    first = 1
    second = 1
    third = 1
    counter = 0
    dead = 0

    list_of_fib.append(first)
    list_of_fib.append(second)
    while len(list_of_fib) != months:

        if len(list_of_fib) >= lifespan:
            dead = list_of_fib[counter-lifespan]
        third = first
        first = first+second - dead
        list_of_fib.append(first)
        second = third
        counter+=1
        print(first, dead)

    return list_of_fib


print(fibbonacci_generator(6,3))

"""

n1,m1 = input().split()

# After n Months
months = int(n1)
lifespan = int(m1)

print(fibbonacci_generator(months,lifespan))
"""





















