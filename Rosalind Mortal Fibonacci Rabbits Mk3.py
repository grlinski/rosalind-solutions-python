
# http://rosalind.info/problems/fibd/

# First Just Generate Fibbonacci Numbers up to n months
def fibonnacigen(n,m):
    months = n
    lifespan = m
    listofrabbits = []
    dead = 0
    born = 0


    leader = 1
    lagger = 0
    midway = 0

    for i in range(1,months+1):
        listofrabbits.append(leader)
        midway = leader
        leader = leader + lagger
        born = lagger
        lagger = midway

        # How Many Are Born
        #born, the lagger component is how many are born.

        # How Many Die
        if i >= lifespan:
            #print(listofrabbits[i-lifespan])
            dead =  listofrabbits[i-lifespan]
        leader = leader - dead
        print(leader, born, dead)


    return(listofrabbits)



print(fibonnacigen(6,3))
"""
Want:
1 1 2 2 3 4
Normal:
1 1 2 3 4 8

"""















































