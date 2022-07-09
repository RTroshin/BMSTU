#include <stdio.h>

//#define N 10 // Размерность массива
//#define N 1000
#define N 10000

int input_array(int*, int*);
void bubble_sort(int*, int*);
void print_array(int*, int*);

int main(void)
{
    int array[N], n = 0;
    int rc;

    printf("Enter elements of array:\n");
    rc = input_array(array, &n);
    if (rc != 0 && rc != 100)
        return rc;

    bubble_sort(array, &n);

    printf("\nResult:\n");
    print_array(array, &n);

    return rc;
}

/* Ввод элементов в массив по концевому признаку */
int input_array(int *array, int *n)
{
    int i = 0;
    int rc = 1;

    while (rc)
    {
        rc = scanf("%d", &array[i]);
        if (rc != 0)
        {
            ++(*n);
            ++i;
        }
        if (*n == N + 1)
        {
            --(*n);
            return 100;
        }
    }

    if (*n == 0)
    {
        printf("\nArray is empty\n");
        return 1;
    }
    else
        return 0;
}

/* Сортировка введенного массива */
void bubble_sort(int *array, int *n)
{
    for (int i = 0; i < *n - 1; ++i)
        for (int j = 0; j < *n - i - 1; ++j)
            if (array[j] > array[j + 1])
            {
                int temp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = temp;
            }
}

/* Вывод одномерного массива на экран */
void print_array(int *array, int *n)
{
    for (int i = 0; i < *n; ++i)
        printf("%d ", array[i]);
    printf("\n");
}
