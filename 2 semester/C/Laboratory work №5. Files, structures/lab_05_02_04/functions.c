#include "constants.h"

// Проверка файла на корректность
int test_file(int argc, char **argv)
{
    FILE *f;

    double temp;
    int count = 0;

    if (argc != 2)
        return FILE_READING_ERROR;

    f = fopen(argv[1], "r");

    if (f == NULL)
        return FILE_READING_ERROR;

    while (fscanf(f, "%lf", &temp) == 1)
        count++;

    if (count < 2)
        return FILE_DATA_ERROR;

    if (feof(f) == 0)
        return FILE_READING_ERROR;

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}

// Вычисление среднего значения чисел между минимальным и максимальным
// числом в файле
int find_average_sum(FILE* f, int *imin, int *imax, double *average_sum)
{
    double num, sum_num = 0;
    int count = 0, num_count = 0;
    int flag = FALSE;

    while (fscanf(f, "%lf", &num) == 1)
    {
        if ((count == *imin || count == *imax) && flag == FALSE)
        {
            flag = TRUE;
            ++count;
            continue;
        }
        if (flag == TRUE)
        {
            if (count == *imin || count == *imax)
                break;
            sum_num += num;
            ++num_count;
        }
        ++count;
    }

    if (num_count == 0)
        return FILE_DATA_ERROR;
    else
    {
        *average_sum = sum_num / num_count;
        return SUCCESS;
    }
}

// Поиск максимального числа в файле
void find_max_num(FILE* f, int *imax)
{
    double num, max;
    int count = 1;

    fscanf(f, "%lf", &max);
    while ((fscanf(f, "%lf", &num) == 1))
    {
        if (num > max)
        {
            max = num;
            *imax = count;
        }
        ++count;
    }
}

// Поиск минимального числа в файле
void find_min_num(FILE* f, int *imin)
{
    double num, min;
    int count = 1;

    fscanf(f, "%lf", &min);
    while ((fscanf(f, "%lf", &num) == 1))
    {
        if (num < min)
        {
            min = num;
            *imin = count;
        }
        ++count;
    }
}
