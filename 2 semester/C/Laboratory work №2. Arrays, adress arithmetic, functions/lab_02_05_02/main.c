#include <stdio.h>

#define N 10 // Размерность массива

int input_size(int*);
int input_array(int*, int*);
int calc_sequence(int*, int*);

int main(void)
{
    int array[N], n;
    int *pa = array;
    int *pa_end;
    int rc;

    printf("Enter size of array:\n");
    rc = input_size(&n);
    if (rc != 0)
        return rc;

    pa_end = array + n;

    printf("Enter elements of array:\n");
    rc = input_array(pa, pa_end);
    if (rc != 0)
        return rc;

    printf("Sum is %d\n", calc_sequence(pa, pa_end));

    return rc;
}

/* Ввод размерности массива */
int input_size(int *size)
{
    int rc;

    rc = scanf("%d", size);
    if (rc != 1 || *size <= 0 || *size > N)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    return 0;
}

/* Ввод элементов в массив */
int input_array(int *pa, int *pa_end)
{
    int rc;

    while (pa != pa_end)
    {
        rc = scanf("%d", &*pa);
        if (rc != 1)
        {
            printf("Error: Incorrect enter\n");
            return 1;
        }
        ++pa;
    }

    return 0;
}

/* Вычисление суммы последовательности */
int calc_sequence(int *pa, int *pa_end)
{
    long int sum = *pa, mult = *pa;

    if (*pa <= 0)
        return sum;

    ++pa;
    while (pa != pa_end)
    {
        if (*pa < 0)
        {
            mult *= *pa;
            sum += mult;
            break;
        }
        else
        {
            mult *= *pa;
            sum += mult;
            ++pa;
        }
    }

    return sum;
}
