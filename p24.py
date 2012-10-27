#
# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 

# The lexicographic permutations of 0, 1 and 2 are:

# 012,   021,   102,   120,   201,   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Performance : 0.78ms
# Answer : 2 7 8 3 9 1 5 4 6 0
#

from math import factorial
from copy import deepcopy

# Implemented Using an algorithm to find the nth Permutation
# Source : http://stackoverflow.com/questions/352203/generating-permutations-lazily
#          Second Answer
# Performance : 0.78ms (1000 runs)
def nthPerm1(list, n):
    l = len(list)
    #print list, n
    if l == 1 :
        return list

    # The first elements index
    p = (n/factorial(l-1)) % l
    
    elem = list[p]
    del(list[p])

    return [elem] + nthPerm1(list, n % factorial((l - 1)))


# Implemented using factroid method. Fact that factroids can be directly mapped to a 
# Permutation
# Source : http://msdn.microsoft.com/en-us/library/Aa302371
# Performance : 0.92 (1000 runs)
# Note : 1.08ms with xrange()
def nthPerm2(list, n):
    l = len(list)
    fact = factorial(l-1)
    
    factoid = [0] * l
    for i in range(9, 0, -1):
        factoid[i] = n / fact
        n = n % fact
        fact = fact / i

    for i in range(1, 10):
        for j in range(i-1, -1, -1):
            if factoid[j] >= factoid[i]:
                factoid[j] += 1

    factoid.reverse()
    return factoid

def init():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 1 Mil - 1 since the permutations are 0 based
    print nthPerm1(l, 1000000-1)

if __name__ == "__main__":
    init()