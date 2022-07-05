#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 10 // Размерность массива

int input_size(int*);
int input_array(int*, int*);
int add_number_to_array(int*, int*, int*, int*);
int search_armstrong_number(int*);
void print_array(int*, int*);

int main(void)
{
    int array[N], n;
    int new_array[N], new_n = 0;
    int rc;
    
    printf("Enter size of array:\n");
    rc = input_size(&n);
    if (rc != 0)
        return rc;

    printf("Enter elements of array:\n");
    rc = input_array(array, &n);
    if (rc != 0)
        return rc;
    rc = add_number_to_array(array, new_array, &n, &new_n);
    if (rc != 0)
        return rc;

    printf("\nResult:\n");
    print_array(new_array, &new_n);

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

/* Добавление числа армстронга в новый массив */
int add_number_to_array(int *array, int *new_array, int *n, int *new_n)
{
    for (int i = 0; i < *n; ++i)
    {
        if (search_armstrong_number(&array[i]))
        {
            new_array[*new_n] = array[i];
            ++(*new_n);
        }
    }

    if (*new_n == 0)
    {
        printf("\nThere are no armstrong numbers\n");
        return 1;
    }
    else
        return 0;
}

/* Поиск числа армстронга */
int search_armstrong_number(int *number)
{
    int number_copy = *number;
    int armstrong_number = 0, armstrong_pow = 0;

    if (number_copy <= 0)
        return 0;
    else if (number_copy > 0 && number_copy < 10)
        return 1;

    while (number_copy != 0)
    {
        number_copy /= 10;
        ++armstrong_pow;
    }

    number_copy = *number;
    while (number_copy != 0)
    {
        armstrong_number += (int) pow(number_copy % 10, armstrong_pow);
        number_copy /= 10;
    }

    if (armstrong_number == *number)
        return 1;
    else
        return 0;
}

/* Вывод одномерного массива на экран */
void print_array(int *array, int *n)
{
    for (int i = 0; i < *n; i++)
        printf("%d ", array[i]);
    printf("\n");
}
