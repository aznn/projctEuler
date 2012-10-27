#
# n! means n  (n  1)  ...  3 x 2 x 1
#
# For example, 10! = 10 x 9  ...  3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
#
# Performance : 1.44 ms (1000 runs)
#

# feels like a bit of cheating ;)
import math

def countFact(number):
    sum = 0
    val = math.factorial(number)
    while(val != 0):
        sum += val % 10
        val = val / 10

    return sum

def init():
    print countFact(100)

if __name__ == "__main__":
    init()