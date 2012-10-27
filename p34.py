#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
# Performance : 51,033ms (to check all numbers from 11 - 1,000,000)
# Answer : 40,730
# Note : Since there are ONLY 4 of these, i.e 1, 2, 145 and 40585. We need not even write a program. 
#        And this program need not check till the millionth number. But what the hell.

def f(number):
    if f <= 1 : return 1
    
    answer = 1
    for i in range(2, number+1):
        answer *= i

    return answer


def p34():
    # Pre cache factorials
    fact = {}
    for i in range(0, 10):
        fact[i] = f(i)
    
    answer = []
    for i in range(11, 1000000):
        total = 0
        for j in str(i):
            total += fact[int(j)]

            if total > i : break

        if total == i :
            answer.append(i)


    return sum(answer)
def init():
    print p34()