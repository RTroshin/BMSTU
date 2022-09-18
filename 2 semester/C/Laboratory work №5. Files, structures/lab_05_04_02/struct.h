#ifndef STRUCT_H

#define STRUCT_H

#define NAME_LENGTH 31             // Максимальная длина наименования продукта
#define BRAND_NAME_LENGTH 16       // Максимальная длина наименования изготовителя
#define MAX_PRODUCTS 100

struct products
{
    char name[NAME_LENGTH];
    char brand[BRAND_NAME_LENGTH];
    unsigned int price, amount;
};

#endif // STRUCT_H
