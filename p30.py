#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#
# Performance : 15,601ms
# Answer : 443,839
# Note : 6 * (9^5) = 354,294    7 * (9^5) = 413,343
#        So clearly the last number that can satisfy this condition could possibly be a 6 digit number
#        So we check only til 355,000


def p30():
    l = []
    for i in range (2, 355000):

        mSum = 0
        mString = str(i)
        # Converting the number to a string and then iterating over it is faster in python than getting
        # every last digit using % operator and dividing to reduce the integer..
        for c in mString:
            mSum += int(c)**5

        if mSum == i:
            print i
            l.append(i)

    return sum(l)


def init():
    print p30()