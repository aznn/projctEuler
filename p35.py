#
# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?
#
# Performance : 8,492ms
# Answer : 55
# Note : Using a set for the sieve instead of a list is imperetive. set has a search time of O(1) while list has O(n)
#        With a set the code runs in 8,000ms but with a list it runs in 200,000ms 
# 

from eulerUtils import get_sieve_erosthane, pTest_sieve
from functools import reduce

def rotate(list):
    for i in range(0, len(list)):
        yield list[i:] + list[:i]

def p35():
    sieve = get_sieve_erosthane(1000000, 'set')

    # Starting with the obvious ones
    circularPrimes = [2, 3, 5, 7]
    for i in list(sieve)[4:]:
        flag = True
        si = str(i)
        if '2' in si or '5' in si or '0' in si:
            flag = False
        else:
            for j in rotate(si):
                # Converts a list of digits to a single integer
                n = reduce(lambda rst, d: int(rst) * 10 + int(d), j)

                if n not in sieve : 
                    flag = False
                    break
            
        if flag : 
            circularPrimes.append(i)
            #print i

    return len(circularPrimes)



def init():
    print p35()
