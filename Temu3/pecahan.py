import fractions
#output: 3/2
print(fractions.Fraction(1.5))
#output: 1/3
print(fractions.Fraction(1,3))

from fractions import Fraction as F

#output: 2/3
print(F(1,3) + F(1,3))

#output: 6/5
print(1 / F(5,5))

#output true
print(F(-3,10) < 0)

