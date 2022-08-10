#include <stdio.h>

#define N 10 // Размерность массива (максимальное количество строк)
#define M 10 // Размерность массива (максимальное количество столбцов)
#define K 10 // Размерность массива

/* Булевы константы для функции check_monotonic_sequence */
#define TRUE 1
#define FALSE 0

int input_size(int*);
int input_matrix(int matrix[N][M], int*, int*);
void check_monotonic_sequence(int matrix[N][M], int*, int*, int*);
void print_array(int*, int*);

int main(void)
{
    int matrix[N][M], n, m;
    int array[K];
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

    check_monotonic_sequence(matrix, array, &n, &m);

    printf("\nFinal array:\n\n");
    print_array(array, &n);

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

/* Проверка строк матрицы на монотонность */
void check_monotonic_sequence(int matrix[N][M], int *array, int *n, int *m)
{
    int k = 0;
    int bool_1 = FALSE, bool_2 = FALSE;

    for (int i = 0; i < *n; ++i)
    {
        for (int j = 0; j < *m - 1; ++j)
        {
            if (matrix[k][j] <= matrix[k][j + 1])
                bool_1 = TRUE;
            else
            {
                bool_1 = FALSE;
                break;
            }
        }
        for (int j = 0; j < *m - 1; ++j)
        {
            if (matrix[k][j] >= matrix[k][j + 1])
                bool_2 = TRUE;
            else
            {
                bool_2 = FALSE;
                break;
            }
        }
        if (*m == 1 || (!bool_1 && !bool_2))
        {
            array[k] = 0;
            k++;
        }
        else if (bool_1 || bool_2)
        {
            array[k] = 1;
            k++;
        }
    }
}

/* Вывод одномерного массива на экран */
void print_array(int *array, int *n)
{
    for (int i = 0; i < *n; i++)
        printf("%d ", array[i]);
    printf("\n");
}
