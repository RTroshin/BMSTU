#include <stdio.h>

unsigned int dec_number(unsigned int);
void print_dec_binary_number(unsigned int);

int main(void)
{
    unsigned int number;
    int rc;

    printf("Enter number:\n");
    rc = scanf("%u", &number);
    if (rc != 1)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    printf("Result: ");
    number = dec_number(number);
    print_dec_binary_number(number);

    return 0;
}

unsigned int dec_number(unsigned int number)
{
    number = (((number << 1) & 0xAAAAAAAA) | ((number >> 1) & 0x55555555));

    return number;
}

void print_dec_binary_number(unsigned int number)
{
    for (int i = 31; i >= 0; --i)
        if (number & (1 << i))
            printf("%d", 1);
        else
            printf("%d", 0);
    printf("\n");
}
