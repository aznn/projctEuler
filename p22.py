#
# Using names.txt(p22.txt), a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 
#   3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
#   So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?
#
# Performance : 153.92ms
# Answer : 871,198,282


def readFromFile():
    line = str(open("p22.txt", "r").readline())

    names = []
    for name in line.split(','):
        names.append(name[1:-1])

    return names

def calculateNameScores(names):
    total = 0
    
    i = 1
    for name in names:

        #Calculate each names score
        score = 0
        for c in name:
            score += (ord(c) - 64)

        total += score * i
        
        i += 1

    return total

def init():
    names = readFromFile()
    names.sort()

    print calculateNameScores(names)

if __name__ == "__main__":
    init()