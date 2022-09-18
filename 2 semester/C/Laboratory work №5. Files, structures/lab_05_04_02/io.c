#include "constants.h"

// Проверка файла на корректность
int test_file(int argc, char **argv)
{
    FILE *f = fopen(argv[2], "r");

    if (argc != 4)
        return KEY_ERROR;

    if (f == NULL)
        return FILE_READING_ERROR;

    if (ferror(f) != 0)
        return FILE_DATA_ERROR;

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}

// Чтение полей структуры из файла и составления массива структур
//int read_file(char **argv, struct products *product, int *product_number)
//{
//    FILE *f = fopen(argv[2], "r");
//    int rc = 4;
//    int i = 0;

//    while (rc == 4)
//    {
//        rc = fscanf(f, "%s%s%u%u", product[i].name, product[i].brand, &product[i].price, &product[i].amount);
//        if (rc != 4)
//            continue;

//        if (strlen(product[i].name) > NAME_LENGTH)
//        {
//            fclose(f);
//            return NAME_OVERFLOW;
//        }

//        if (strlen(product[i].brand) > BRAND_NAME_LENGTH)
//        {
//            fclose(f);
//            return BRAND_NAME_OVERFLOW;
//        }

//        ++(*product_number);
//        ++i;
//    }

//    if (fclose(f) == EOF)
//        return FILE_CLOSE_ERROR;

//    return *product_number ? SUCCESS : INCORRECT_INPUT;
//}

//char *str_del_end(char *str)
//{
//    size_t end = strlen(str);

//    if (end && str[end - 1] == '\n')
//        str[end - 1] = '\0';

//    return str;
//}

int read_file(char *file, struct products product[])
{
    FILE *f;
    f = fopen(file, "r");

    int count = 0;
    char *p_end;
    char buffer[MAX_BUFFER];
    long num;

    if (!f)
    {
        return FILE_DOESNT_EXIST;
    }
    for (; count < MAX_PRODUCTS; count++)
    {
        if (fgets(buffer, MAX_BUFFER, f) == NULL)
        {
            fclose(f);
            return count;
        }
        str_del_end(buffer);
        if (strlen(buffer) == 0 || strlen(buffer) > NAME_LENGTH)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        strcpy(product[count].name, buffer);
        if (fgets(buffer, MAX_BUFFER, f) == NULL)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        str_del_end(buffer);
        if (strlen(buffer) == 0 || strlen(buffer) > MAX_PRODUCTS)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        strcpy(product[count].brand, buffer);
        if (fgets(buffer, MAX_BUFFER, f) == NULL)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        str_del_end(buffer);
        if (strlen(buffer) == 0)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        num = strtol(buffer, &p_end, 10);
        if (p_end == NULL)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        if (num < 0)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        product[count].price = (unsigned int) num;
        if (fgets(buffer, MAX_BUFFER, f) == NULL)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        str_del_end(buffer);
        if (strlen(buffer) == 0)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        num = strtol(buffer, &p_end, 10);
        if (p_end == NULL)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        if (num < 0)
        {
            fclose(f);
            return FILE_READING_ERROR;
        }
        product[count].amount = (unsigned int) num;
    }

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    if (count == MAX_PRODUCTS)
        return WRONG_ARG;

    return SUCCESS;
}

void insert_item(struct products product[], struct products product, int i, int n)
{
    for (int j = n - 1; j >= i; j--)
        product[j + 1] = product[j];

    product[i] = product;
}

int append_product(char *file, struct products product)
{
    FILE *f;
    int rc, i = 0, j;
    struct product product[100];
    rc = read_file(file, product);
    if (rc == FILE_READING_ERROR)
    {
        return FILE_READING_ERROR;
    }
    else if (rc == WRONG_ARG)
    {
        return WRONG_ARG;
    }
    if ((rc == 0) || (rc == FILE_DOESNT_EXIST))
    {
        product[0] = product;
        i++;
    }
    else
    {
        i = rc;
        for (j = 0; j < i; j++)
        {
            if (product.price > product[j].price)
            {
                insert_item(product, product, j, i);
                break;
            }
            else if ((product.price == product[j].price) && (product.amount > product[j].amount))
            {
                insert_item(product, product, j, i);
                break;
            }
        }
        if (j == i)
        {
            product[j] = product;
        }
        i++;
    }
    f = fopen(file, "w");
    for (j = 0; j < i; j++)
    {
        fprintf(f, "%s\n%s\n%u\n%u\n", product[j].name, product[j].producer, product[j].price, product[j].quantity);
    }
    fclose(f);
    return SUCCESS;
}

// Создание и заполнение файла или вывод массива структур
void write_to_file(FILE *f, struct products *product, int product_number)
{
    for (int i = 0; i < product_number; ++i)
    {
        fprintf(f, "%s\n%s\n", product[i].name, product[i].brand);
        fprintf(f, "%u\n%u\n", product[i].price, product[i].amount);
    }
}

// Вывод массива структур
//void print_products(struct products *product, int *product_number)
//{
//    for (int i = 0; i < *product_number; ++i)
//    {
//        printf("%s\n%s\n", product[i].name, product[i].brand);
//        printf("%"PRIu32"\n%"PRIu32"\n", product[i].price, product[i].amount);
//    }
//}
