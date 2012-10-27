#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
# Performance : Original (22,556ms)
#               Only-odd (14,376ms)
# Answer : 872,187
# Note : Only possibilities would be odd numbers. As any number ending with an even number would end with 
#        a zero in binary. Hence cannot be a palindrome

from eulerUtils import toBinary, isPalindrome

def p36():
    answer = []
    for n in range(1, 1000000, 2):
        if isPalindrome(n) :
            if isPalindrome(toBinary(n)):
                #print n, toBinary(n)
                answer.append(n)

    return sum(answer)

def init():
    print p36()