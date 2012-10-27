#
# It was proposed by Christian Goldbach that every odd composite number 
# can be written as the sum of a prime and twice a square.

# 9 = 7 + 2 x 1^2
# 15 = 7 + 2 x 2^2
# 21 = 3 + 2 x 3^2
# 25 = 7 + 2 x 3^2
# 27 = 19 + 2 x 2^2
# 33 = 31 + 2 x 1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#
# Performance : 380ms
# Answer : 5,777
#

from eulerUtils import get_sieve_erosthane, pTest_sieve

def p46():
    n = 10000
    sieve = get_sieve_erosthane(n, method='set')
    
    for i in range(3, n, 2):
        # Since only composite numbers
        if i in sieve : continue

        # Count down from the number to 2 (smallest prime)
        success = False
        for j in range(1, i):
            # 2 x (j ^ 2)
            diff = i - (2 * j * j)

            if diff in sieve:
                #print i, diff, j
                success = True
                break

        if not success : return i


def init():
    print p46()