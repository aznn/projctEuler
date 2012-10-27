#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#
# Performance : 8,569ms
# Answer : 45,228
# Note : Could be improved using the fact that the range needs to be only 1 & 4 digits or 2 & 3 digits for i and j respectively

def p32():
    answer = set()
    for i in range(1, 2500):
        for j in range(1, 2500):
            p = i * j

            string = str(p) + str(i) + str(j)
            length = len(string)

            # Guard Blocks
            if length < 9 : continue
            if length > 9 : break

            # Check if palindigital number
            check = [False]*10
            check[0] = True
            passed = True
            for n in string:
                n = int(n)
                if check[n] == True: 
                    passed = False
                    break

                check[n] = True
                
            if not passed : continue

            print i, j, p
            answer.add(int(p))
    
    #print answer
    return sum(answer) 

def init():
    print p32()