
/*
 * A palindromic number reads the same both ways. 
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

 * Find the largest palindrome made from the product of two 3-digit numbers./
 *
 */
 
#include <stdio.h>
#include <time.h>

int isPalindrome(int x) {
	int rev = 0, orig = x, rem;
	int i;
	
	for(i = 0; x != 0; i *= 10) {
		rem = x % 10;
		x /= 10;
		rev = rev * 10 + rem;
		
		if(i == 0)
			i = 1;
	}
	
	if(rev == orig)
		return 1;
	else
		return 0;
}

int main() {
	int i, j, x;
	
	int palindrome = 1, count = 0;
	
	for(i = 999; i > 100; i--) {
		for(j = 999; j > 100; j--) {
			x = i * j;
			
			if(x < palindrome)
				continue;
			
			count++;
			if(isPalindrome(x)) {
				if(x > palindrome) {
					palindrome = x;
					printf("%d : Palindrome  : %d x %d = %d\n", count, i, j, palindrome);
				}
			}
		}
		
		if(i * 999 < palindrome)
			break;
	}	
	
	printf("\n\nisPalindrome() : %d", count);
	
	return 0;
}
