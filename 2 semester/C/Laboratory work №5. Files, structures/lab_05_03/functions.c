#include <stdio.h>

#include "constants.h"

// Получение числа по его позиции
int get_number_by_pos(FILE *f, int pos)
{
    int res;

    fseek(f, pos * sizeof(int), SEEK_SET);
    fread(&res, sizeof(int), 1, f);

    return res;
}

// Вставка числа на позицию
int put_number_by_pos(FILE *f, int pos, int number)
{
    fseek(f, pos * sizeof(int), SEEK_SET);
    fwrite(&number, sizeof(int), 1, f);

    return SUCCESS;
}

// Сортировка чисел в файле
int sort(char *file_name)
{
    FILE *f;

    if ((f = fopen(file_name, "rb+")) == NULL)
        return FILE_DOESNT_EXIST;

    int len = 0, temp;
    int number_1, number_2;

    while (fread(&temp, sizeof(int), 1, f) == 1)
        ++len;

    if (len == 0)
        return EMPTY_FILE;

    for (int i = 0; i < len - 1; ++i)
        for (int j = 0; j < len - i - 1; ++j)
            if ((number_1 = get_number_by_pos(f, j)) > (number_2 = get_number_by_pos(f, j + 1)))
            {
                put_number_by_pos(f, j, number_2);
                put_number_by_pos(f, j + 1, number_1);
            }

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}
