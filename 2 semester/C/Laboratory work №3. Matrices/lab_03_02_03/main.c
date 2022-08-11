#include <stdio.h>
#include <stdlib.h>

#define N 10 // Размерность массива (максимальное количество строк)
#define M 10 // Размерность массива (максимальное количество столбцов)

int input_size(int*);
int input_matrix(int matrix[N][M], int*, int*);
int input_number(int*);
int user_number_search(int matrix[N][M], int*, int*, int*);
int digit_search(int, int*);
void delete_column(int matrix[N][M], int*, int*, int*);
void print_matrix(int matrix[N][M], int*, int*);

int main(void)
{
    int matrix[N][M], n, m;
    int user_number;
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

    printf("\nEnter number to delete column:\n");
    rc = input_number(&user_number);
    if (rc != 0)
        return rc;
    rc = user_number_search(matrix, &n, &m, &user_number);
    if (rc != 0)
        return rc;

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

/* Ввод пользовательского числа, предназначенного для удаления
 * столбца(ов) массива, содержащих это число */
int input_number(int *user_number)
{
    int rc;

    rc = scanf("%d", user_number);
    if (rc != 1 || *user_number < 0 || *user_number > 9)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    return 0;
}

/* Поиск введенного пользователем числа в массиве */
int user_number_search(int matrix[N][M], int *n, int *m, int *user_number)
{
    for (int i = 0; i < *n; ++i)
        for (int j = 0; j < *m; ++j)
            if (digit_search(matrix[i][j], user_number))
            {
                delete_column(matrix, n, m, &j);
                --j;
            }
    if (*m == 0)
    {
        printf("\nMatrix is empty");
        return 2;
    }

    return 0;
}

/* Поиск цифры в числе */
int digit_search(int number, int *user_number)
{
    if (number == *user_number)
        return 1;

    number = abs(number);

    while (number != 0)
    {
        if (number % 10 == *user_number)
            return 1;
        number /= 10;
    }

    return 0;
}

/* Удаление столбца в массиве */
void delete_column(int matrix[N][M], int *n, int *m, int *j_del)
{
    for (int i = 0; i < *n; ++i)
        for (int j = *j_del; j < *m; ++j)
            matrix[i][j] = matrix[i][j + 1];
    if (*m != 0)
        --(*m);
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
