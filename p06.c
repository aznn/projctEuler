/*
 * The sum of the squares of the first ten natural numbers is,
 * 1^2 + 2^2 + ... + 10^2 = 385
 
 * The square of the sum of the first ten natural numbers is,
 * (1 + 2 + ... + 10)^2 = 552 = 3025
 * 
 * Hence the difference between the sum of the squares of the first ten 
 * natural numbers and the square of the sum is 3025 - 385 = 2640.

 * Find the difference between the sum of the squares of the 
 * first one hundred natural numbers and the square of the sum.
 
 */
 
#include <stdio.h>
#include <time.h>

int main() {
	int squareOfSum = 0, sumOfSquare = 0;
	int i;
	clock();
	for(i = 1; i <= 100; i++) {
		sumOfSquare += i*i;
		squareOfSum += i;
	}
	
	squareOfSum *= squareOfSum;
	
	printf("Square of sum - sum of square\n%d - %d = %d\n\n", squareOfSum, sumOfSquare, squareOfSum - sumOfSquare);
	
	return 0;
}
