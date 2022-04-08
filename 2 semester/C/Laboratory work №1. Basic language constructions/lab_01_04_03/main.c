#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int number;
    double mult_digits;

    printf("Enter a three-digit number:\n");
    scanf("%d", &number);

    mult_digits = abs((number / 100) * (number % 100 / 10) * (number % 10));

    printf("Mult digits is %.6f\n", mult_digits);

    return 0;
}
