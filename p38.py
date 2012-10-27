#
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192  1 = 192
# 192  2 = 384
# 192  3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
#concatenated product of an integer with (1,2, ... , n) where n  1?

#
# Performance : 674ms
# Answer : 932,718,654
# Note : 10,000 upper limit is a guess

from eulerUtils import isPandigital
from functools import reduce
def p38():
    answer = []
    for i in range(1, 10000):
        number = ""
        j = 1
        while(len(number) < 9):
            number += str(i * j)
            j += 1

        if len(number) != 9: continue
        if not isPandigital(int(number)) : continue

        answer.append(number)

    return reduce(lambda a, b : a if a > b else b, answer)

def init():
    print p38()
