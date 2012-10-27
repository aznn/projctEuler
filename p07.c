
/*
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

 * What is the 10001st prime number?
 
 */
 
#include <stdio.h>

int isPrime(int x) {
	int i;
	
	if(x == 2)
		return 1;
	
	for(i = 2; i*i <= x; i++) {
		if(x % i == 0) {
			return 0;
		}
	}
	
	return 1;
}

int main() {
	int count = 6, i = 15;
	
	while(count != 10001) {
		i += 2;
		
		if(isPrime(i)) {
			count++;
		}
	}
	
	printf("%d", i);
	
	return 0;
}
