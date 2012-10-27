#
# If the numbers 1 to 5 are written out in words: 
#      one, two, three, four, five, then there are 
#      3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
#
# Performance : 61.4 ms (average of 10 runs)


# String representation of numbers
strRep = { 
           1  : 'one',       2 : 'two',        3 : 'three',
           4  : 'four',      5 : 'five',       6 : 'six',
           7  : 'seven',     8 : 'eight',      9 : 'nine',
           10 : 'ten',      11 : 'eleven',    12 : 'twelve',
           13 : 'thirteen', 14 : 'fourteen',  15 : 'fifteen',
           16 : 'sixteen',  17 : 'seventeen', 18 : 'eighteen', 
           19 : 'nineteen',  
           
           20 : 'twenty',   30 : 'thirty',    40 : 'forty',
           50 : 'fifty',    60 : 'sixty',     70 : 'seventy',
           80 : 'eighty',   90 : 'ninety',    00 : 'hundred',

           -1 : 'and',
           -2 : 'hundred'
        }

# returns string representation of a number
def toString(x):
    s = []
    if(x < 20):
        s.append(strRep[x])

    # two digit number
    elif (x/100 == 0):

        # 10, 20, 30, 40 .. 90
        if (x % 10 == 0):
            s.append(strRep[x])
        
        # 21, 22, 23 .. 29, 31, 32 .. 99
        else:
            tmp = str(x)
            s.append(strRep[int(tmp[0]) * 10])
            s.append(strRep[int(tmp[1])])

    # three digit number
    elif (x/1000 == 0):
        tmp = str(x)

        #100, 200, 300, 400 .. 900
        if(x % 10 == 0 and x % 100 == 0):
            s.append(strRep[int(tmp[0])])
            s.append(strRep[-2])

        else:
            #hundredth digit
            s.append(strRep[int(tmp[0])])
            s.append(strRep[-2])
            s.append(strRep[-1])

            #first and second digit.
            secondTwo = tmp[1] + tmp[2]
            s = s + toString(int(secondTwo))
    
    # 1000 (function works only from 1 - 1000 inclusive)
    else:
        s.append('one')
        s.append('thousand')

    return s

def init():
    length = 0
    for i in range(1, 1001):
        tmp = toString(i)
    
        for j in tmp:
            length += len(j)

        #print "{} - {}\n".format(i, tmp)

    print 'Total Length : ' + str(length) + ' letters'

if __name__ == "__main__":
    init()
