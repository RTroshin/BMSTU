#include <stdio.h>
#include <math.h>

#define N 10 // Размерность массива

int input_size(int*);
int input_array(int*, int*);
int mupliply_elements(int*, int*, int*, int*);

int main(void)
{
    int array[N], n;
    int mult_elem = 1, pow_count = 0;
    double geometric_mean;
    int rc;

    printf("Enter size of array:\n");
    rc = input_size(&n);
    if (rc != 0)
        return rc;

    printf("Enter elements of array:\n");
    rc = input_array(array, &n);
    if (rc != 0)
        return rc;

    rc = mupliply_elements(array, &n, &mult_elem, &pow_count);
    if (rc != 0)
        return rc;
    geometric_mean = pow(mult_elem, 1.0 / pow_count);

    printf("Geometric mean is %.6lf\n", geometric_mean);

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
int input_array(int *array, int *n)
{
    int rc;

    for (int i = 0; i < *n; ++i)
    {
        rc = scanf("%d", &array[i]);
        if (rc != 1)
        {
            printf("Error: Incorrect enter\n");
            return 1;
        }
    }

    return 0;
}

/* Произведение положительных элементов массива */
int mupliply_elements(int *array, int *n, int *mult_elem, int *pow_count)
{
    for (int i = 0; i < *n; ++i)
        if (array[i] > 0)
        {
            *mult_elem *= array[i];
            ++(*pow_count);
        }
    if (*pow_count == 0)
    {
        printf("\nThere are no positive numbers\n");
        return 1;
    }
    else
        return 0;
}
