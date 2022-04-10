#include <stdio.h>

int input_number(int);
int euclidean_algorithm(int, int);

int main(void)
{
    int m = 0, n = 0;
    int result;

    printf("Enter two numbers:\n");
    m = input_number(m);
    if (m < 0)
        return 1;
    n = input_number(n);
    if (n < 0)
        return 1;

    result = euclidean_algorithm(m, n);

    printf("Greatest common divisor is %d\n", result);

    return 0;
}

/* Ввод числа */
int input_number(int number)
{
    int rc;

    rc = scanf("%d", &number);
    if (rc != 1 || number <= 0)
    {
        printf("Error: Incorrect enter\n");
        return -1;
    }

    return number;
}

/* Вычисление НОД по алгоритму Евклида */
int euclidean_algorithm(int m, int n)
{
    while (m != 0 && n != 0)
    {
        if (m > n)
            m %= n;
        else
            n %= m;
    }
    return m + n;
}
