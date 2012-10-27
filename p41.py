#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?
#
# Performance : 126ms
# Answer : 7,652,413
# Note : pandigital of 9 will have sum of 45. and always divisible by 3. Pandigital of 7 have
#        sum of 36, also divisble by 3. So we start from 7
#

from eulerUtils import isPandigital, pTest_sieve, list_to_int, get_sieve_erosthane
from itertools import permutations

def p41():
    numbers = ['0', '1', '21', '321', '4321', '54321', '654321', '7654321']

    # sqrt(999999999) = 31622
    sieve = get_sieve_erosthane(32000, sort = True)

    for i in range(7, 1, -1):
        perm = permutations(numbers[i])
        for p in perm:
            num = list_to_int(p)
            if pTest_sieve(num, sieve) : 
                return num
            

def init():
    print p41()
