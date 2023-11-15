#include <stdio.h>

void hanoi(char a, char b, char c, int n)
{
    if(n == 1){
        printf("przeloz z %c na %c\n", a, c);
    }
    else{
        hanoi(a, c, b, n-1);
        printf("przeloz z %c na %c\n", a, c);
        hanoi(b, a, c, n-1);
    }
}

int main(void)
{
    hanoi('A', 'B', 'C', 3);
    return 0;
}
