#include <stdio.h>
#include <math.h>

/*
 * The prime factors of 13195 are 5, 7, 13 and 29.

 * What is the largest prime factor of the number 600851475143 ?
 *
 * function fmod used instead because of how windows handles long which is a 4bit number in VS
 */

int isPrime(long x) {
	long i;
	
	if(x % 2 == 0)
		return 0;
	
	for(i = 2; i < x/2; i++) {
		if(x % i == 0) {
			return 0;
		}
	}
	
	return 1;
}

int main() {
	long double number = 600851475143;
	
	long i = sqrt(number);
	if(i % 2 == 0)
		i++;
		
	for(; i > 0; i -= 2) {
		if(fmod(number, i) == 0 && isPrime(i)) {
			printf("%ld", i);
			break;
		}
	}
	
	return 0;
}
