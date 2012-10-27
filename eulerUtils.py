#
# Useful utilities for Project Euler
# http://projecteuler.net/
# 
# Author : Aeon Axan
# Email  : azaan@outlook.com

# -------------------------------------------------------------------------------------------------- BEGIN PRIME UTILITIES
# Note about prime checking : 
# If you have a known upperlimit and memory is indespensible its better to get the sieve as a set
# and do a (n in sieve) check. than going for pTest_sieve() or pTest_trial()

# Generate a sieve of Erosthane for given uLimit
# Performance : 37ms for 10,000 Primes
def get_sieve_erosthane(uLimit, method='list', sort = False):
    
    tSieve = range(uLimit+1)
    fin = int(uLimit**0.5)

    for i in xrange(2, fin+1):
        if not tSieve[i]:
            continue

        tSieve[2*i :: i] = [None] * (uLimit/i - 1)

    if method == 'set' :
        sieve = set([i for i in tSieve[2:] if i])

    elif method =='list':
        sieve = [i for i in tSieve[2:] if i]
        if sort : sieve.sort()

    return sieve

# Primality test, uses trial division with a sieve (sorted sieve) and the sieve
# should contain primes till sqrt(n)
# Performance : (1, 10,000)  - 405ms
#               (1,  1,000)  -  44ms
#               (1,    100)  -   5ms
def pTest_sieve(n, sieve):
    if n <= 2 : return False

    for p in sieve:
        if p*p > n : break

        if n % p == 0 : return False

    return True

# Primality Test, trial division till sqrt(n), divides only odd numbers
# Performance : (1, 10,000)  - 752ms
#               (1,  1,000)  -  48ms
#               (1,    100)  -   4ms
def pTest_trial(n):
    from math import sqrt
    if n <= 2 : return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0 : return False

    return True

# Build a prime factor sieve. The sieve index starts from 1. and any position i reperesents i+1th number
def build_prime_fact_sieve(max):
    sieve = [0]*max

    # Since 2 is the first prime
    for i in range(2, max):
        # It will be 0 if it is a prime number
        if sieve[i] == 0 :
            for j in range(2*i, max, i):
                sieve[j] += 1

    return sieve

# --------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------- BEGIN PYTHOGOREAN TRIPLETS
# Get Pythogerean triplet for the given m and n value
# Performance : 7,320ms for m(1, 1000) and n(m, 1000)
def buildTriplet(m, n, type = 'list'):
    if not m < n : raise Exception("'n' must be less than 'm'")
    n2 = n**2
    m2 = m**2

    if type == 'list' : return [n2-m2, 2*n*m, n2+m2]
    elif type == 'tuple' : return (n2-m2, 2*n*m, n2+m2)

# Returns a list of all pythogorean triplets whose value of a, b or c dosent exceed the max provided
# by default returns a list of tuples. i.e [(a1, b1, c1), (a2, b2, c2), (a3, b3, c3)]
# Performance : 118ms (maximum = 10,000)
def getAllTriplets(maximum, filter = True, type = 'list'):
    done = False
    triplets = []
    for i in range(1, 10000):
        for j in range(i+1, 10000):
            t = buildTriplet(i, j, 'tuple')
            
            #find Max
            maxT = max(t)

            if maxT > maximum : 
                done = True
                break

            # get t in the correct order
            if t[0] < t[1] :
                t = (t[1], t[0], t[2])

            triplets.append(t)
            
            k = 2
            while maxT*k < maximum :
                triplets.append((t[0]*k, t[1]*k, t[2]*k))
                k += 1

        if done : break

    if filter and type == 'list':
        seen = set()
        seen_add = seen.add
        triplets =  [ x for x in triplets if x not in seen and not seen_add(x)]

    if type == 'set':
        triplets = set(triplets)

    return triplets
# -------------------------------------------------------------------------------------------------- 


# -------------------------------------------------------------------------------------------------- BEGIN TRIANGULAR NUMBERS
# Returns a list/set of n triangle numbers from the start value, n not inclusive
# t(n) = 1/2[n(n+1)]
# Performance : 135ms (start = 0, n = 10,000, type='list')
def triangular_n(start, n, type='set'):
    numbers = []
    i = (start*(start+1))/2
    inc = start + 1
    count = 1
    numbers.append(i)
    n = n + inc

    while inc < n :
        i += inc
        inc += 1
        numbers.append(i)

    if type == 'set':
        return set(numbers)

    elif type == 'list':
        return numbers

    else:
        raise Exception("Incorrect Type!")

# Triangle number generator, start inclusive
# t(n) = 1/2[n(n+1)]
def triangular_gen(start):
    i = (start*(start+1))/2
    inc = start + 1

    while 1 :
        yield i
        i += inc
        inc += 1
# -------------------------------------------------------------------------------------------------- 


# -------------------------------------------------------------------------------------------------- BEGIN PENTAGONAL NUMBERS
# Returna  list/set of n pentagonal numbers from the start value, n not inclusive
# p(n) = 1/2[n(3n-1)], diff = 3n + 1
def pentagonal_n(start, n, type='set'):
    numbers = []
    i = (start*(3*start-1))/2
    inc = 3*start + 1
    numbers.append(i)
    count = 1

    while count < n :
        i += inc
        inc += 3
        count += 1
        numbers.append(i)

    if type == 'set':
        return set(numbers)

    elif type == 'list':
        return numbers

    elif type == 'dict':
        ans = {}
        for i in range(start, n):
            ans[i] = numbers[i]
        return ans

    else:
        raise Exception("Incorrect Type!")

# Pentagonal number generator, start inclusive
# p(n) = 1/2[n(3n-1)], diff = 3n + 1
def pentagonal_gen(start):
    i = (start*(3*start-1))/2
    inc = 3*start + 1

    while 1 :
        yield i
        i += inc
        inc += 3
# -------------------------------------------------------------------------------------------------- 


# -------------------------------------------------------------------------------------------------- BEGIN HEXAGONAL NUMBERS
# Returna  list/set/dict of n hexagonal numbers from the start value, n not inclusive
# h(n) = [n(2n-1)], diff = 3n + 1
def hexagonal_n(start, n, type='set'):
    numbers = []
    i = start*(2*start-1)
    inc = 4*start + 1
    numbers.append(i)
    count = 1

    while count < n :
        i += inc
        inc += 4
        count += 1
        numbers.append(i)

    if type == 'set':
        return set(numbers)

    elif type == 'list':
        return numbers

    elif type == 'dict':
        ans = {}
        for i in range(start, n):
            ans[i] = numbers[i]
        return ans

    else:
        raise Exception("Incorrect Type!")

# -------------------------------------------------------------------------------------------------- BEGIN MISC
# Returns the alphabetical value of a word
# Words must be in either uppercase or lowercase
# Performance : 155ms (1786 words)
def alphabetical_value(word, case):
    if case == 'lowercase':
        diff = 96
    elif case == 'uppercase':
        diff = 64

    else : raise Exception("Case must be 'uppercase' or 'lowercase' only")

    val = 0
    for c in word:
        val += (ord(c) - diff)

    return val

# Generator for all rotations of the given list
# Ex : [1, 2, 7] returns (1, 2, 7) (2, 7, 1) (7, 1, 2)
def rotate(list):
    for i in range(0, len(list)):
        yield list[i:] + list[:i]

# Converts an integer to binary
# Returns binary representation in integer format
def toBinary(number, format='int'):
    if format == 'int':
        return int(bin(number)[2:])

    elif format == 'string':
        return str(bin(number)[2:])

# Checks for palindrome. returns True or False. 
# Works with numbers and strings
# Performance : 1,727ms (1 - 100,000)
def isPalindrome(n):
    n = str(n)

    # Rough verification
    if n[0] != n[-1] : return False

    l = [i for i in n]
    orig = list(l)
    l.reverse()

    if l == orig :
        return True
    else : 
        return False

# Sum of divisors using prime Factorisation, needs a sorted prime sieve (1 - maxNumber)
# Performance : 185ms for d() of first 1,000 numbers
def d(number, sieve):
    n = number
    sum = 1
    p = sieve[0]
    s = []
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

# Check if number is a pandigital number.
# a number with a 0 will ALWAYS evaluate to false
# Performance : 0.29ms for 300 checks
def isPandigital(number, base = 9):
    number = str(number)
    if len(number) != base : return False

    nl = [int(i) for i in number]

    sums = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    if sum(nl) != sums[base] : return False

    res = [False]*(base+1)
    res[0] = True
    for n in nl:
        n = int(n)
        if n > base or res[n] : return False

        res[n] = True

    return True

# Convert a list of numbers to an integer
def list_to_int(l):
    return int(''.join(map(str, l)))
# -------------------------------------------------------------------------------------------------- 



# Timing module
def init():
    isPandigital(4132, 4)
    isPandigital(123456789, 9)
    isPandigital(12344, 6)




# Deprecated methods (Better methods used now)
# --------------------------------------------------------------------------------------------------------

# Check for palindrome. Works ONLY with an integer.
# Performance : 5,481ms (1 - 100,000)
def dep_isPalindrome(n):
    rev, nOrig = 0, n
    while(n != 0):
        rev = (rev * 10) + (n % 10)
        n = n / 10

    if nOrig == rev : 
        return True
    else :
        return False