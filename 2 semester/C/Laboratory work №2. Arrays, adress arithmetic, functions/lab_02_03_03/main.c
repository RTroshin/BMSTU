#include <stdio.h>

#define N 20 // Размерность массива

int input_size(int*);
int input_array(int*, int*);
void reverse_element(int*, int*);
void shift_array(int*, int*, int*);
void print_array(int*, int*);

int main(void)
{
    int array[N], n;
    int rc;

    printf("Enter size of array:\n");
    rc = input_size(&n);
    if (rc != 0)
        return rc;

    printf("Enter elements of array:\n");
    rc = input_array(array, &n);
    if (rc != 0)
        return rc;

    reverse_element(array, &n);

    printf("\nResult:\n");
    print_array(array, &n);

    return rc;
}

/* Ввод размерности массива */
int input_size(int *size)
{
    int rc;

    rc = scanf("%d", size);
    if (rc != 1 || *size <= 0 || *size > 10)
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

/* Выполнение реверса для положительных элементов массива */
void reverse_element(int *array, int *n)
{
    int element, r_element;
    for (int i = 0; i < *n; ++i)
    {
        element = array[i];
        if (array[i] >= 0)
        {
            r_element = 0;
            while (element != 0)
            {
                r_element = r_element * 10 + element % 10;
                element = element / 10;
            }
            shift_array(&i, array, n);
            array[i + 1] = r_element;
            i++;
        }
    }
}

/* Сдвиг массива, освобождение места для вставки нового элемента */
void shift_array(int *i, int *array, int *n)
{
    if (*n != N)
        ++(*n);
    for (int j = *n - 1; j > *i; --j)
        array[j] = array[j - 1];
}

/* Вывод одномерного массива на экран */
void print_array(int *array, int *n)
{
    for (int i = 0; i < *n; ++i)
        printf("%d ", array[i]);
    printf("\n");
}
