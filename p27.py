#
# Euler published the remarkable quadratic formula:

# n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly 
# when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, 
# which produces 80 primes for the consecutive values n = 0 to 79. 
# The product of the coefficients, 79 and 1601, is 126479.

# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n

# e.g. |11| = 11 and |4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the 
# maximum number of primes for consecutive values of n, starting with n = 0.
#
# Performance : 2,900ms
# Answer : -59,231
# Note : Can be made much much faster if we decrease the search space using mathematical constraints
#        Like it can be proved the discriminant must be negative ... can be proved that search space of 
#        a need only be from -63 to 63.. 
# 


from eulerUtils import get_sieve_erosthane, pTest_sieve

sieve = ()
def check(a, b):
    global sieve
    for n in range(1, 100):
        number = n*n + a*n + b
        if not number in sieve : return n
        #if not pTest_sieve(number, sieve) : return n
    


def p27():
    global sieve
    testSieve = get_sieve_erosthane(15000)
    testSieve.sort()
    sieve = set(testSieve)
    primes = get_sieve_erosthane(1000)
    primes.sort()

    max, a, b = 0, 0, 0
    for j in primes:
        # A must be prime too
        for i in primes:
            # i + j > 0 
            if not i + j > 0 : pass

            # 1 + i + j is also a prime
            if not 1+i+j in sieve : pass

            n = check(i, j)
            if n > max : 
                max, a, b = n, i, j

            n = check(-i, j)
            if n > max : 
                max, a, b = n, -i, j

            # skipping -j as -ve numbers are not considered primes

    return (max, a, b)


def init():
    max, a, b = p27()
    print max, a, b
    print 'Answer = ', a*b

if __name__ == "__main__":
    init()