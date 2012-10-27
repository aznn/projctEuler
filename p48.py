#
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
#
# Performance : 62ms
# Answer : 9,110,846,700
#

def p48():
    sum = 0
    for i in range(1, 1000):
        sum += i**i

    print len(str(sum))
    return sum % 10**10

def init():
    p48()