#include <stdio.h>
#include <stdlib.h>

#include "constants.h"

// Создание файла
int create_file(char *file_name, int random, char *argv)
{
    int amount_argv = atoi(argv);

    if (amount_argv == 0)
        return WRONG_ARG;

    FILE *f;
    int a;

    if ((f = fopen(file_name, "wb")) == NULL)
        return FILE_CREATION_ERROR;

    for (int i = 0; i < amount_argv; ++i)
    {
        a = rand() % (random * 2) - random;
        fwrite(&a, sizeof(int), 1, f);
    }

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}

// Чтение файла
int read_file(char *file_name)
{
    int temp = 0, i = 0;
    FILE *f;

    if ((f = fopen(file_name, "rb")) == NULL)
        return FILE_DOESNT_EXIST;

    fseek(f, 0, SEEK_SET);
    while (!feof(f))
        if (fread(&temp, sizeof(int), 1, f) == 1)
        {
            fprintf(stdout, "%d ", temp);
            ++i;
        }

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    if (i == 0)
        return EMPTY_FILE;

    return SUCCESS;
}
