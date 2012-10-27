#
# Starting with the number 1 and moving to the right in a clockwise direction a 
# 5 by 5 spiral is formed as follows:

#            21 22 23 24 25
#            20  7  8  9 10
#            19  6  1  2 11
#            18  5  4  3 12
#            17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# Performance : 25ms
# Answer : 669,171,001
# 
# Note : Let i be the length of the side
#        Then the four corner numbers of that row would be n + (i-1) (Where n is the previous corner found)
#        i starts from 3(skipping 1) and gets incremented by 2 (since the length if always odd)
#



def p28(side):
    sum = n = 1
    for i in range(3, side+1, 2):
        for _ in range(4):
            n = n + i -1
            sum += n
            #print n
            
    return sum

def init():
    n = 1001
    print p28(n)