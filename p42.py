#
# The nth term of the sequence of triangle numbers is given by, tn = 1/2[n(n+1)]; 
# so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
# nearly two-thousand common English words, how many are triangle words?
#
# Performance : 173ms
# Answer : 162
#

from eulerUtils import triangular_n, alphabetical_value

def readFromFile(name):
    line = str(open(name, "r").readline())

    words = []
    for word in line.split(','):
        words.append(word[1:-1])

    return words

def p42():
    tnumbers = triangular_n(1, 20, 'set')
    words = readFromFile("p42.txt")

    count = 0
    for word in words:
        val = alphabetical_value(word, 'uppercase')
        if val in tnumbers : count += 1

    return count

def init():
    print p42()