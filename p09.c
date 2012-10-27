
/*
 * A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

 * a2 + b2 = c2
 * For example, 32 + 42 = 9 + 16 = 25 = 52.

 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 
 */
 

#include <stdio.h>

int isTriplet(int a, int b, int c) {
	return (a*a + b*b == c*c) ? 1 : 0;
}

int main() {
	int i, j, k;
	
	for(i = 100; i < 1000; i++) {
		for(j = 100; j < 1000; j++) {
			for(k = 100; k < 1000; k++) {
				if(i + j + k == 1000) {
					if(isTriplet(i, j, k)) {
						printf("%d + %d + %d = %d\n", i, j, k, i+j+k);
						printf("%d + %d = %d\n", i*i, j*j, k*k);
						printf(" = %d\n", i*i + j*j);
						printf("\n\n");
						
						printf("Product = %d\n", i*j*k);
						return 0;
					
					} else if(i + j + k > 0)
						break;
				}
			}
		}
	}
	
	return 0;
}
