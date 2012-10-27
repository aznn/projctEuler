#
#
# Starting in the top left corner of a 2x2 grid, there are 6 routes 
# (without backtracking) to the bottom right corner.

# How many routes are there through a 20x20 grid?
# 
#

# Using Dynamic Programming. Cache previously calculated values
# to avoid recalculation which is very expensive

import timeit

gridSize = 20

cache = [[-1 for col in range(gridSize+1)] for row in range(gridSize+1)]

def count(right, down):
    if(right == gridSize and down == gridSize):
        return 1

    tmp = cache[right][down]
    if(tmp != -1):
        return tmp

    tmp = 0
    if(right < gridSize):
        tmp += count(right + 1, down)
    
    if(down < gridSize):
        tmp += count(right, down + 1)

    #print "Caching R({}) D({}) = {}".format(right, down, tmp)
    cache[right][down] = tmp
    return tmp


def init():
    print count(0, 0)

if __name__ == "__main__":
    init()
