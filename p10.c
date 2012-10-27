
/*
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

 * Find the sum of all the primes below two million.
  
 */

#include <stdio.h>
#define MAX 2000000

int main() {
	
	int sieve[MAX];
	int i, j;
	long sum = 0; 
	int count = 0;
	
	sieve[0] = 0;
	sieve[1] = 0;
	// Fill in Sieve without multiples of 3, 5, 7, 9, 13
	for(i = 2; i < MAX; i++) {
		if(i % 2 == 0)
			sieve[i] = 0;
		else
			sieve[i] = i;
	}
	sieve[0] = 2;
		
	for(i = 1; i < MAX; i++) {
		if(sieve[i] == 0)
			continue;
		
		//printf("No. %d\n", sieve[i]);
		
		for(j = i+sieve[i]; j < MAX; j += sieve[i]) {
				//printf("No. %d, sieve val %d\n", i, sieve[j]);
				sieve[j] = 0;
		}
	}
	
	// Summation and counter could be implemented in the previous loop avoiding an extra loop
	for(i = 0; i < MAX; i++) {
		if(sieve[i] != 0) {
			//printf("%d\n", sieve[i]);
			sum += sieve[i];
			count++;
		}
	}
	
	//printf("%d Primes\n", count);
	printf("Sum of all primes below %d is %ld\n", MAX, sum);
	return 0;
}
