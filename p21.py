#
# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; 
# so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
#
# Performance : 1,724ms
# Answer : 31,626


# Sieve of Erosthane
sieve = []
def initESieve(uLimit):
    
    tSieve = range(uLimit+1)
    fin = int(uLimit**0.5)

    for i in xrange(2, fin+1):
        if not tSieve[i]:
            continue

        tSieve[2*i :: i] = [None] * (uLimit/i - 1)

    global sieve
    sieve = [i for i in tSieve[2:] if i]

# Sum of divisors using prime factorisation
def d(number):
    global sieve

    n = number
    sum = 1
    p = sieve[0]

    i = 0
    while p * p <= n and n > 1:
        p = sieve[i]
        i += 1

        if n % p == 0 :
            j = p * p
            n = n / p
            
            while n % p == 0:
                j = j * p
                n = n / p


            sum = sum * (j-1)/(p-1)

    
    # prime larger than the square root remains
    if n > 1 :
        sum *= n + 1

    return sum - number


def findAmicable(rangeU):
    # amicables = []
    total = 0
    for i in range(2, rangeU+1):
        b = d(i)
        if i != b and i == d(b):
            # amicables = amicables + [i]
            total += i
    
    # print amicables
    return total

def init():
    initESieve(10000)
    print findAmicable(10000)


if __name__ == "__main__":
    init()