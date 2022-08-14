#include <stdio.h>
#include <stdlib.h>

#define N 10 // Размерность массива (максимальное количество строк)
#define M 10 // Размерность массива (максимальное количество столбцов)

/* Булевы константы для функции user_number_search */
#define TRUE 1
#define FALSE 0

int input_size(int*);
int spiral_input_matrix(int matrix[N][M], int*, int*);
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

    spiral_input_matrix(matrix, &n, &m);
    printf("\n");
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
int spiral_input_matrix(int matrix[N][M], int *n, int *m)
{
    int i = 0, j = 0, k = 0;
    int count = 1;
    int bool = FALSE;

    while (count - 1 != *n * *m)
    {
        if (i == 0 + k && j == 0 + k)
        {
            if (bool)
            {
                k++;
                i = k;
                j = k;
            }
            else
                bool = TRUE;
            matrix[i][j] = count++;
            i++;
        }
        else if (i < *n - 1 - k && j == 0 + k)
        {
            matrix[i][j] = count++;
            i++;
        }
        else if (i == *n - 1 - k && j < *m - 1 - k)
        {
            matrix[i][j] = count++;
            j++;
        }
        else if (j == *m - 1 - k && i > 0 + k)
        {
            matrix[i][j] = count++;
            i--;
        }
        else if (i == 0 + k && j > 0 + k)
        {
            matrix[i][j] = count++;
            j--;
        }
    }

    return 0;
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
