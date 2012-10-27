#
# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?
#
# Performance : 56ms (Brute Force)
# Answer : 4782
#


# Fibonnacci generator
def fib():
	a, b = 0, 1
	while 1:
		a, b = b, a+b
		yield a

# Solves using Brute Force
# Note : Uses a fibonnacci generator
# Performance : 990ms
def p25a():
	gen = fib()
	
	i = 0
	while 1:
		i += 1
		a = gen.next()
		if len(str(a)) >= 1000:
			break

	return i

# Solves using Brute Force
# Note : One combined loop
# Performance : 849ms
def p25b():
	i, j, term = 0, 1, 2
	while True:
		fib = i+j
		if len(str(fib)) >= 1000:
			return term
		
		i, j, term = j, fib, term+1

# Solves using Brute Force
# Note : One loop, avoids len(str()) [ Great Performance Increase]
# Performance : 56ms
def p25c():
	a,b,c = 0,1,1
	while True:
		a,b,c=b,a+b,c+1
		if b >= 10**999:
			return c

def init():
	print p25c()
	

if __name__ == "__main__":
	init()
