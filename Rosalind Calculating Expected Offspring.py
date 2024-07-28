
# http://rosalind.info/problems/iev/
# Calcuating Expected Offspring


"""
For a random variable X  taking integer values between 1 and n
The expected value of X is ... some large equation

Example: If we roll a six sided die the expected average is 3.5
=(1+2+3+4+5+6)/6 = 3.5

Given six numbers representing the couples in a population
Each possessing every genotype paring for a given factor in order.

So from first to last what each number represents
AAxAA
AAxAa
AAxaa
AaxAa
Aaxaa
aaxaa

Return the expected number of offspring displaying the dominant phenotype in the next generation assuming every
couple has exactly two offspring.



"""
a,b,c,d,e,f = input().split()
AAxAA = int(a)
AAxAa = int(b)
AAxaa = int(c)
AaxAa = int(d)
Aaxaa = int(e)
aaxaa = int(f)

part1 = (AAxAA*2)+(AAxAa*2)+(AAxaa*2)
part2 = AaxAa*1.5
part3 = Aaxaa
total = part1+part2+part3
print(total)
























