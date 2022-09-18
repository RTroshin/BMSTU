#include "constants.h"

// Сортировка товаров по убыванию цены за единицу товара
int sort(char *file_in, char *file_out)
{
    struct products product[100], temp;
    FILE *f_out;
    int i = 0, rc;
    rc = read_file(file_in, product);

    if (rc == FILE_DOESNT_EXIST)
    {
        return FILE_DOESNT_EXIST;
    }
    else if (rc == FILE_READING_ERROR)
        return FILE_READING_ERROR;
    else if (rc == 0)
        return FILE_DATA_ERROR;
    else if (rc == WRONG_ARG)
        return WRONG_ARG;

    i = rc;

    for (int j = 0; j < i; ++j)
        for (int k = j; k < i; k++)
        {
            if (product[j].price < product[k].price)
            {
                temp = product[k];
                product[k] = product[j];
                product[j] = temp;
            }
            if ((product[j].price == product[k].price) && (product[j].amount < product[k].amount))
            {
                temp = product[k];
                product[k] = product[j];
                product[j] = temp;
            }
        }

    f_out = fopen(file_out, "w");

    for (int j = 0; j < i; ++j)
        fprintf(f_out, "%s\n%s\n%u\n%u\n", product[j].name, product[j].brand, product[j].price, product[j].amount);

    if (fclose(f_out) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}
