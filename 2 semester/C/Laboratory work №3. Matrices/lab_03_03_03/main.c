#include <stdio.h>

#define N 10 // Размерность массива (максимальное количество строк)
#define M 10 // Размерность массива (максимальное количество столбцов)

/* Булевы константы для функции bubble_sort_with_flag */
#define TRUE 1
#define FALSE 0

int input_size(int*);
int input_matrix(int matrix[N][M], int*, int*);
int min_search(int*, int*);
void bubble_sort_with_flag(int matrix[N][M], int*, int*);
void print_matrix(int matrix[N][M], int*, int*);

int main(void)
{
    int matrix[N][M], n, m;
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

    bubble_sort_with_flag(matrix, &n, &m);

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

/* Сортировка строк методом пузырька */
void bubble_sort_with_flag(int matrix[N][M], int *n, int *m)
{
    int flag = FALSE;

    for (int i = 0; i < *n - 1; ++i)
    {
        flag = FALSE;
        for (int j = 0; j < *n - 1 - i; ++j)
            if (min_search(matrix[j], m) < min_search(matrix[j + 1], m))
                for (int k = 0; k < *m; ++k)
                {
                    int temp = matrix[j][k];
                    matrix[j][k] = matrix[j + 1][k];
                    matrix[j + 1][k] = temp;
                    flag = TRUE;
                }
        if (!flag)
            break;
    }
}

/* Поиск минимального элемента в строке */
int min_search(int *matrix, int *m)
{
    int min = matrix[0];

    for (int i = 1; i < *m; ++i)
        if (matrix[i] < min)
            min = matrix[i];

    return min;
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
