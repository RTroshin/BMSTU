#include <stdlib.h>

#include "constants.h"

// Проверка файла на корректность
int test_file(int argc, char **argv)
{
    if (argc != 3)
        return WRONG_ARG;

    if (!atoi(argv[2]))
        return WRONG_ARG;

    FILE *f = fopen(argv[1], "r");

    if (f == NULL)
        return FILE_READING_ERROR;

    if (ferror(f) != 0)
        return FILE_DATA_ERROR;

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}

// Чтение полей структуры из файла и составления массива структур
int read_file(char **argv, struct products *product, int *product_number)
{
    FILE *f = fopen(argv[1], "r");
    int structs_amount;
    int rc;
    int i = 0;

    rc = fscanf(f, "%d", &structs_amount);
    if (rc != 1)
    {
        fclose(f);
        return INCORRECT_INPUT;
    }
    else if (structs_amount <= 0 || structs_amount > 15)
    {
        fclose(f);
        return STRUCT_ERROR;
    }

    rc = 2;
    while (rc == 2)
    {
        rc = fscanf(f, "%s%d", product[i].name, &product[i].price);
        if (rc != 2)
            continue;

        if (strlen(product[i].name) > NAME_LENGTH)
        {
            fclose(f);
            return NAME_OVERFLOW;
        }

        if (product[i].price <= 0)
        {
            fclose(f);
            return PRICE_ERROR;
        }

        ++i;
    }

    *product_number = i;

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return structs_amount == *product_number ? SUCCESS : STRUCT_ERROR;
}

// Вывод массива структур
void print_products(struct products *product, int *product_number, char **argv)
{
    for (int i = 0; i < *product_number; ++i)
        if ((double) product[i].price - atof(argv[2]) < 0.0)
            printf("%s\n%u\n", product[i].name, product[i].price);
}
