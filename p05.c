/*
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 * 
 */
 
#include <stdio.h>

int main() {
	
	int i, j, div = 0, count = 0;
	
	for(i = 20; div != 17; i += 20) {
		div = 0;
		
		if(i % 7 != 0 || i % 9 != 0)
			continue;
		
		for(j = 3; j <= 19; j++) {
			count++;
			if(i % j == 0)
				div++;
			else 
				break;
		}
	}
	
	printf("I : %d\nCount : %d", i-20, count);
	
	return 0;
}
