#
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2  7
# 15 = 3  5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2  7  23
# 645 = 3  5  43
# 646 = 2  17  19.

# Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
#
# Performance : 4030ms
# Answer : 134,043
# Note : fact_sieve = a sieve with prime factorisations of all numbers. The sieve is built by incrementing the count of
#        all multiples of prime numbers in the sieve. Hence we will have a sieve whoose every location indicates the number
#        of prime factors that number has. In this sieve all primes will have a 0 in it. Since it would never be a factor
#        of another number and would never get incremented from the initial zero value.
#


from eulerUtils import build_prime_fact_sieve

def p47():
    n = 150000
    fact_sieve = build_prime_fact_sieve(n)

    for i in range(1, n-4):
        if (fact_sieve[i+3] == 4 and
            fact_sieve[i+2] == 4 and
            fact_sieve[i+1] == 4 and
            fact_sieve[i  ] == 4):
            return (i, i+1, i+2, i+3)

def init():
    print p47()
