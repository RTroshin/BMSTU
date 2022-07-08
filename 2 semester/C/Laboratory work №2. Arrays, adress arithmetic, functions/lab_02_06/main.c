#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <inttypes.h>
#include <sys/time.h>

//#define N 10 // Размерность массива
//#define N 100
//#define N 1000
//#define N 10000
#define N 100000

//#define M 10 // Количество повторов
#define M 100

void form_array(int*, int*);
int process_1(int*, int*);
int process_2(int*, int*);
int process_3(int*, int*);

int main(void)
{
    int array[N];
//    int *pa = array;
//    int *pa_end;

    /* Копия массива для сравнения производительности */
    int array_copy[N];
    int *pa_copy = array_copy;
    int *pa_end_copy;

//    int n = 10;
//    int n = 100;
//    int n = 1000;
//    int n = 10000;
    int n = 100000;

    struct timeval tv_start, tv_stop;
    int64_t elapsed_time = 0;

    int rc = 0;

    pa_end_copy = array_copy + n;

    form_array(array, &n);

    /* Подсчет времени для функции process_1 (индексация a[i]) */
    for (int i = 1; i < M + 1; ++i)
    {
        for (int j = 0; j < n; ++j)
            array_copy[j] = array[j];

        gettimeofday(&tv_start, NULL);
        process_1(array_copy, &n);
        gettimeofday(&tv_stop, NULL);
        elapsed_time += (tv_stop.tv_sec - tv_start.tv_sec) * 1000000LL +
                        (tv_stop.tv_usec - tv_start.tv_usec); // время в микросекундах
    }
    printf("Process_1 = %" PRId64 " us\n", elapsed_time / (M - 2));
    printf("\n");

    /* Подсчет времени для функции process_2 (выражение *(a + i)) */
    elapsed_time = 0;
    for (int i = 1; i < M + 1; ++i)
    {
        for (int j = 0; j < n; ++j)
            array_copy[j] = array[j];

        gettimeofday(&tv_start, NULL);
        process_2(array_copy, &n);
        gettimeofday(&tv_stop, NULL);
        elapsed_time += (tv_stop.tv_sec - tv_start.tv_sec) * 1000000LL +
                        (tv_stop.tv_usec - tv_start.tv_usec); // время в микросекундах
    }
    printf("Process_2 = %" PRId64 " us\n", elapsed_time / (M - 2));
    printf("\n");

    /* Подсчет времени для функции process_3 (указатели) */
    elapsed_time = 0;
    for (int i = 1; i < M + 1; ++i)
    {
        for (int j = 0; j < n; ++j)
            array_copy[j] = array[j];

        gettimeofday(&tv_start, NULL);
        process_3(pa_copy, pa_end_copy);
        gettimeofday(&tv_stop, NULL);
        elapsed_time += (tv_stop.tv_sec - tv_start.tv_sec) * 1000000LL +
                        (tv_stop.tv_usec - tv_start.tv_usec); // время в микросекундах
    }
    printf("Process_3 = %" PRId64 " us\n", elapsed_time / (M - 2));
    printf("\n");

    return rc;
}

/* Формирование случайного целочисленного массива */
void form_array(int *array, int *n)
{
    srand(time(NULL));
    for (int i = 0; i < *n; ++i)
        array[i] = rand() % 100 + 1;
}

/* Вычисление суммы последовательности.
   Массив обрабатывается с помощью индексации */
int process_1(int *array, int *n)
{
    long int sum = array[0], mult = array[0];

    if (array[0] <= 0)
        return sum;

    for (int i = 1; i < *n; ++i)
    {
        if (array[i] < 0)
        {
            mult *= array[i];
            sum += mult;
            break;
        }
        else
        {
            mult *= array[i];
            sum += mult;
        }
    }

    return sum;
}

/* Вычисление суммы последовательности.
   Массив обрабатывается с помощью выражения *(a + i) */
int process_2(int *pa, int *n)
{
    long int sum = *pa, mult = *pa;

    if (*pa <= 0)
        return sum;

    for (int i = 1; i < *n; ++i)
    {
        if (*(pa + i) < 0)
        {
            mult *= *(pa + i);
            sum += mult;
            break;
        }
        else
        {
            mult *= *(pa + i);
            sum += mult;
        }
    }

    return sum;
}

/* Вычисление суммы последовательности.
   Массив обрабатывается с помощью указателей */
int process_3(int *pa, int *pa_end)
{
    long int sum = *pa, mult = *pa;

    if (*pa <= 0)
        return sum;

    ++pa;
    while (pa != pa_end)
    {
        if (*pa < 0)
        {
            mult *= *pa;
            sum += mult;
            break;
        }
        else
        {
            mult *= *pa;
            sum += mult;
            ++pa;
        }
    }

    return sum;
}
