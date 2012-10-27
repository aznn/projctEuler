#
# In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
# It is possible to make $2 in the following way:

# 1($1) + 150p + 220p + 15p + 12p + 31p
# How many different ways can $2 be made using any number of coins?
#
# Performance : 139,345ms
# Answer : 73682
# Note to future self : Look at my solution and laugh at your stupidity.. xD
#

# My recursive solution. Which does work!.... in 1.5 minutes
def countCombinations(value, money):
    #print value, money
    # If money array is empty
    if len(money) == 0:
        return 0

    if value == 0:
        return 0

    count = 0
    for i, m in enumerate(money):
        rem = value % m
        val = value / m

        if m > value : return count

        # Value cannot be split with the given money
        if val == 0 and rem == 0 : pass

        # Current m divides value out evenly, count this as one path
        if rem == 0:
            #print '+ {}x{}p '.format(val, m)
            count += 1

        # Check if there are any possible paths with the remainder of the money
        else:
            count += countCombinations(rem, money[i+1:])
        # Count the paths by taking different values of current m
        for j in range(1, val):
            count += countCombinations(value-(m*j), money[i+1:])

    return count
        
# Iterative solution to the problem (mathblog.dk's solution)
# Performance : 500ms
def solveIterative(target):
    ways = 0
    # second is -1 which implies >= 0
    for i in range(target, -1, -200):
        for j in range(i, -1, -100):
            for k in range(j, -1, -50):
                for l in range(k, -1, -20):
                    for m in range(l, -1, -10):
                        for n in range(m, -1, -5):
                            for o in range(n, -1, -2):
                                ways += 1
    
    return ways

# Solves using dynamic programming concepts.
# Performance : 12ms
def solveDynamic(target, money):
    ways = [0]*(target+1)
    ways[0] = 1

    for i in money:
        for j in range(i, target+1):
            ways[j] += ways[j - i]

    return ways[target]

def p31():
    #print countCombinations(200, [1, 2, 5, 10, 20, 50, 100, 200])
    #print solveIterative(200)
    print solveDynamic(200, [1, 2, 5, 10, 20, 50, 100, 200])
    

def init():
    print p31()