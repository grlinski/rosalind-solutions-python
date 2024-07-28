


holder = input()

a=0
g=0
c=0
t=0
stringer = ""


for i in holder:
    if i == "A":
        stringer += "T"
    if i == "G":
        stringer += "C"
    if i == "C":
        stringer += "G"
    if i == "T":
        stringer += "A"


reverser = stringer[::-1]
print(reverser)









