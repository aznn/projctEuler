#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and 
# it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
#  that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# Performance :  64,546ms (63,000ms spent in function p23())
# Answer : 4,179,871


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

# Prime Factorisation
def d(number):
    global sieve, timeSpent

    n = number
    sum = 1
    p = sieve[0]

    i = 0
    while p * p <= n:
        p = sieve[i]
        i += 1

        if n % p == 0 :
            j = p * p
            n = n / p
            
            while n % p == 0:
                j = j * p
                n = n / p


            sum = sum * (j-1)/(p-1)

        if n < 1:
            break
    
    # prime larger than the square root remains
    if n > 1 :
        sum *= n + 1

    return sum - number


def findAbundantNumbers(uLimit):
    a = []
    for i in xrange(10, uLimit):
        if d(i) > i:
            a.append(i)

    return a

import time
def p23(abundant, uLimit):
    start = time.clock()
    probable = [True]*uLimit

    length = len(abundant)
    print 'calculating sums of abundant numbers...'
    
    for iC, i in enumerate(abundant):
        #print 'Checking for ' + str(abundant[i])

        for j in abundant[iC:]:
            if i + j < uLimit:
                #print abundant[i], abundant[j]
                probable[i+j] = False
            else:
                break


    sum = 0
    for i in xrange(0, uLimit):
        if probable[i]:
            sum += i
            #print i

    print 'Time spent : ', str(time.clock() - start)
    return sum

def init():
    limit = 28123
    initESieve(limit)
    abundant = findAbundantNumbers(limit)
    #print abundant
    
    # Finds the sum of numbers that cannot be written as sum
    print p23(abundant, limit)

if __name__ == "__main__":
    init()