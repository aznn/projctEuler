#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?
#
# Performance : 412ms
# Answer : 2969 + 6299 + 9629
#

from eulerUtils import get_sieve_erosthane, list_to_int
from itertools import permutations

def p49():
    s = get_sieve_erosthane(9999, sort = True)
    sieve = [n for n in s if n >= 1000]
    sieveSet = set(sieve)

    answers = set()
    for n in sieve:

        perm = permutations(str(n))
        num = set([list_to_int(i) for i in perm if list_to_int(i) in sieveSet])
        if len(num) < 3 : continue

        num = list(num)
        num.sort()

        l = len(num)
        for i in range(0, l):
            for j in range(i+1, l):
                diff = num[j] - num[i]

                if num[i] + diff not in num or num[i] + 2 * diff not in num :
                    continue

                answers.add((num[i], num[i]+diff, num[i]+diff+diff))

    return answers

def init():
    ans = p49()
    ans = list(ans)

    for a, b, c in ans : 
        print str(a) + str(b) + str(c)