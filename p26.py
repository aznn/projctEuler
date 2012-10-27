#
# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
# Performance : 63ms 
# Answer : 983
# Note : Actually testing only prime numbers will suffice as the length of thesequence would be same
#        for a numbers multiples and all numbers are multiples of primes
#


# Concept : http://stackoverflow.com/questions/8946310/how-to-know-the-repeating-decimal-in-a-fraction/8946506#8946506
# Keep track of previous divions we have done before. Once we see a repeated division
# From there on the answers will be repeated.
def getRecurr(a, b):
    r = a % b

    # Position at which we have done the same division before
    seen = {r : 0}

    # recurring digits
    digits = []
    
    # This loop will run at most (b-1) times because the recurring digits 
    # will be less than b.
    while True:
        r *= 10
        digits.append(r//b)
        r = r % b
        
        # If we have seen the division(r/b) before
        if seen.has_key(r):
            w = seen[r]
            return digits[w:]
        else:
            seen[r] = len(digits)
        

def p26():
    max = 0
    num = 0

    # Checking only odd numbers (We need to check ONLY primes) instead of implementing that
    # Just cutting down the work a bit
    for i in range(999, 0, -2):
        l = len(getRecurr(1, i))
        
        #print (i, l)
        if(l > max):
            max = l
            num = i

        # since number i cannot produce a recurring decimal more than itself
        if i < max:
            break

    return num, max

def init():
    print p26()


if __name__ == "__main__":
    init()