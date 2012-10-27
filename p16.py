
# 2^15 = 32768
# the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

# 2.4 ms
def countDigits1():
    sum = 0
    number = 2**1000
    
    while(number != 0):
        #print(str(number))
        sum += number % 10
        number = number / 10

    return sum

# 1.73 ms
def countDigits2():
    sum = 0
    for n in str(2**1000):
        sum += int(n)
    
    return sum

def init():
    print countDigits2()

if __name__ == "__main__":
    init()
