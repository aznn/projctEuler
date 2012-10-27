#
# The number 3797 has an interesting property. Being prime itself, 
# it is possible to continuously remove digits from left to right, and remain prime at each stage: 
# 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#
# Performance : 2,047ms
# Answer : 748,317
# Note : Range to 740,000 since the 11th and largest truncatable prime is 739397
#

from eulerUtils import get_sieve_erosthane

def p37():
    limit = 740000
    sieve = get_sieve_erosthane(limit)
    sieve.sort()
    sieve_set = set(sieve)

    answer = []
    for n in sieve[4:]:
        ns = str(n)

        # Any number with a 0, 2, 5 cannot be a truncatable prime
        if '0' in ns or '2' in ns or '5' in ns : continue

        flag = True
        for i in range(1, len(ns)):
            if int(ns[i:]) not in sieve_set or int(ns[:i]) not in sieve_set :
                flag = False
                break

        if flag : answer.append(n)

    print answer
    return sum(answer)
            
def init():
    print p37()