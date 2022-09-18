#include "constants.h"

// Поиск продуктов, содержащих заданную подстроку
int find_substr(struct products *product, int *product_number, struct products *new_product, int *new_product_number, char *str)
{
    int len = strlen(str);
    int len_name;
    char name[NAME_LENGTH];

    for (int i = 0; i < *product_number; ++i)
    {
        len_name = strlen(product[i].name);
        for (int j = 0; j < len + 1; ++j)
            name[len - j] = product[i].name[len_name - j];

        if (strncmp(name, str, len) == 0)
            new_product[(*new_product_number)++] = product[i];
    }

    return *new_product_number ? SUCCESS : NO_FIT_PRODUCTS;
}
