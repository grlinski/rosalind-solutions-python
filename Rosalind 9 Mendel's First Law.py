
a,b,c = input().split()
k = float(a)
m = float(b)
n = float(c)
p = k+m+n
p2 = p-1

#Proportion of Dom/Het/Rec
k1 = k/p
m1 = m/p
n1 = n/p








#Alt Proportions
#If AA picked
DAAk = (k-1)/p2
DAAm = m/p2
DAAn = n/p2

#If Aa picked
HAak = k/p2
HAam = (m-1)/p2
HAan = n/p2

#If aa picked
Raak = k/p2
Raam = m/p2
Raan = (n-1)/p2










#"""

#Easier to find probability of hom-rec

#Probability AA and AA
prob1 = k1*DAAk
print(prob1)
#Probability AA and Aa
prob2 = k1*DAAm
print(prob2)
#Probability AA and aa
prob3 = k1*DAAn
print(prob3)

#Probability Aa and AA
prob4 = m1*HAak
print(prob4)
#Probability Aa and Aa
prob5 = m1*HAam
print(prob5)
#Probability Aa and aa
prob6 = m1*HAan
print(prob6)


#Probability aa and AA
prob7= n1*Raak
print(prob7)
#Probability aa and Aa
prob8 = n1*Raam
print(prob8)
#Probability aa and aa
prob9 = n1*Raan
print(prob9)

total = prob1+prob2+prob3+prob4+prob5+prob6+prob7+prob8+prob9
print()
print(total)

answer = prob1+prob2+prob3+prob4+(prob5*0.75)+(prob6*0.5)+prob7+(prob8*0.5)

print(answer)

print(p)
print(p2)



print(DAAk+DAAm+DAAn)
print(HAak+HAam+HAan)
print(Raak+Raam+Raan)

print(answer)
#"""
#     100 75 50