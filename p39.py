#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?
#
# Performance : 13.3ms
# Answer : 840
#

from eulerUtils import getAllTriplets
def p39():
    triplets = getAllTriplets(500)

    tripletSums = {}
    for triplet in triplets:
        s = sum(triplet)

        if s in tripletSums : 
            tripletSums[s] += 1
        else : 
            tripletSums[s] = 1

    largestSum, largestValue = 0, 0
    for s in tripletSums:
        if tripletSums[s] > largestSum : 
            largestSum, largestValue = tripletSums[s], s

    return (largestSum, largestValue)


def init():
    print p39()