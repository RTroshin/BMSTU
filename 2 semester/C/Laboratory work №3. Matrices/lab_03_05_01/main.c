#include <stdio.h>
#include <stdlib.h>

#define N 10 // Размерность массива (максимальное количество строк)
#define M 10 // Размерность массива (максимальное количество столбцов)
#define K 100 // Размерность массива

int input_size(int*);
int input_matrix(int matrix[N][M], int*, int*);
int number_search(int matrix[N][M], int*, int*, int*, int*);
int digits_sum(int);
void array_shift(int*, int*);
void insert_number(int matrix[N][M], int*, int*, int*, int*);
void print_matrix(int matrix[N][M], int*, int*);

int main(void)
{
    int matrix[N][M], n, m;
    int array[K], k = 0;
    int rc;

    printf("Enter rows and columns of matrix:\n");
    rc = input_size(&n);
    if (rc != 0)
        return rc;
    rc = input_size(&m);
    if (rc != 0)
        return rc;

    printf("Enter elements of matrix:\n");
    rc = input_matrix(matrix, &n, &m);
    if (rc != 0)
        return rc;

    rc = number_search(matrix, array, &n, &m, &k);
    if (rc != 0)
        return rc;
    array_shift(array, &k);
    insert_number(matrix, array, &n, &m, &k);

    printf("\nChanged matrix:\n\n");
    print_matrix(matrix, &n, &m);

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
int input_matrix(int matrix[N][M], int *n, int *m)
{
    int rc;

    for (int i = 0; i < *n; ++i)
        for (int j = 0; j < *m; ++j)
        {
            rc = scanf("%d", &matrix[i][j]);
            if (rc != 1)
            {
                printf("Error: Incorrect enter\n");
                return 1;
            }
        }

    return 0;
}

/* Поиск числа в матрице, сумма цифр которого больше десяти */
int number_search(int matrix[N][M], int *array, int *n, int *m, int *k)
{
    for (int i = 0; i < *n; ++i)
        for (int j = 0; j < *m; ++j)
            if (digits_sum(matrix[i][j]) > 10)
            {
                array[*k] = matrix[i][j];
                ++(*k);
            }

    if (*k == 0)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    return 0;
}

/* Суммирование цифр в числе */
int digits_sum(int number)
{
    int sum = 0;
    number = abs(number);
    while (number != 0)
    {
        sum += number % 10;
        number /= 10;
    }

    return sum;
}

/* Циклический сдвиг массива на три позиции влево */
void array_shift(int *array, int *k)
{
    for (int i = 0; i < 3; ++i)
    {
        int temp = array[0];
        for (int j = 0; j < *k - 1; ++j)
            array[j] = array[j + 1];
        array[*k - 1] = temp;
    }
}

/* Вставка элемента из сдвинутого массива на свое место в матрице */
void insert_number(int matrix[N][M], int *array, int *n, int *m, int *k)
{
    *k = 0;
    for (int i = 0; i < *n; ++i)
        for (int j = 0; j < *m; ++j)
            if (digits_sum(matrix[i][j]) > 10)
            {
                matrix[i][j] = array[*k];
                ++(*k);
            }
}

/* Вывод многомерного массива на экран */
void print_matrix(int matrix[N][M], int *n, int *m)
{
    for (int i = 0; i < *n; i++)
    {
        for (int j = 0; j < *m; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }
}
