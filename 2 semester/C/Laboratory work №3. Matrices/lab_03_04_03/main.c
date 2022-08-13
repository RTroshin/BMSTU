#include <stdio.h>

#define N 10 // Размерность массива (максимальное количество строк)
#define M 10 // Размерность массива (максимальное количество столбцов)

int input_size(int*);
int input_matrix(int matrix[N][M], int*, int*);
void swap_elements(int matrix[N][N], int*);
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
    if (n != m)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    printf("Enter elements of matrix:\n");
    rc = input_matrix(matrix, &n, &m);
    if (rc != 0)
        return rc;

    swap_elements(matrix, &n);

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


/* Функция, меняющая местами элементы массива */
void swap_elements(int matrix[N][N], int *n)
{
    for (int i = 0; i < *n; ++i)
        for (int j = 0; j < *n - i - i; ++j)
        {
            int temp = matrix[j + i][i];
            matrix[j + i][i] = matrix[j + i][*n - 1 - i];
            matrix[j + i][*n - 1 - i] = temp;
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
