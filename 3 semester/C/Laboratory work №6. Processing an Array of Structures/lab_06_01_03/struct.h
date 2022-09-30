#ifndef STRUCT_H

#define STRUCT_H

#define NAME_LENGTH 25      // Максимальная длина наименования продукта

struct products
{
    char name[NAME_LENGTH];
    int price;
};

#endif // STRUCT_H
