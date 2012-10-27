/*

 * The following iterative sequence is defined for the set of positive integers:

 * n = n/2 (n is even)
 * n = 3n + 1 (n is odd)

 * Using the rule above and starting with 13, we generate the following sequence:

 * 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
 * It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
 * Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

 * Which starting number, under one million, produces the longest chain?

 * NOTE: Once the chain starts the terms are allowed to go above one million.
 
 */
 
#include <stdio.h>
#include <conio.h>

int main() {
    
    int chainNum = 0, chainLen = 0;
    int i, tmp;
    long long j;
    
    for(i = 1; i < 1000000; i++) {
        j = i;
        tmp = 1;
        while(j > 1) {
            tmp++;
            if(j % 2 == 0) {
                j = j / 2;
            
            } else {
                j = 3 * j + 1;    
            }
        }
        
        if(tmp > chainLen) {
            printf("Len (%d) for %d\n", tmp, i);    
            chainLen = tmp;
            chainNum = i;
        }
    }
    
    printf("\nLargest Chain Length : %d, number : %d\n", chainLen, chainNum);
    getch();
}
