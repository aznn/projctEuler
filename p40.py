#
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1  d10  d100  d1000  d10000  d100000  d1000000
#
# Performance : 1,506ms
# Answer : 210
#

def p40(digits):
    i, lDigits = 0, len(digits)
    check = digits[i]
    count, num, answer = 1, 1, []
    while True:

        if count >= check:
            # we are doing small - large since we want a negative difference (start counting from right of the number)
            diff = check - count
            answer.append(int(str(num)[diff-1]))

            if i >= lDigits-1:
                break
            else: 
                i+= 1
                check = digits[i]
         
            continue

        num += 1
        count += len(str(num))

    print answer
    return reduce(lambda x, y: x*y, answer)

def init():
    print p40([1, 10, 100, 1000, 10000, 100000, 1000000])
