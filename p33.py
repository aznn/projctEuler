#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
#
# Performance : 294ms 
# Answer : 100
#

# Default to floating point division
from __future__ import division
# Used to get the reduced form of the final fraction
from fractions import Fraction

def p33():
    answerN = []
    answerD = []
    for i in range(11, 100):
        for j in range(i, 100):
            
            # Guard Blocks
            if i % 10 == 0 or j % 10 == 0 : continue
            if i == j : continue

            li = [int(n) for n in str(i)]
            lj = [int(n) for n in str(j)]

            for ni in li:
                ni = int(ni)
                if ni not in lj : continue
                # now ni would be the digit common to both
                
                # The other number in both numerator and denominator
                ti = li[(li.index(ni)+1) % 2]
                tj = lj[(lj.index(ni)+1) % 2]

                div = i/ti
                if j/div != tj : continue

                answerN.append(i)
                answerD.append(j)
                  
    productN, productD = 1,1
    for i in range(0, len(answerN)):
        productN *= answerN[i]
        productD *= answerD[i]

    return Fraction(productN, productD)

def init():
    print p33()