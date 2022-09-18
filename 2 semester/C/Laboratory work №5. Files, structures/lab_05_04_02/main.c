#include "constants.h"

int main(int argc, char **argv)
{
    setbuf(stdout, NULL);

    struct products product;
    char buffer[MAX_BUFFER];
    long num;
    char *p_end;

    setbuf(stdout, NULL);

    int rc = test_file(argc, argv);
    if (rc != SUCCESS)
        return rc;

    if (argc == 4 && strcmp(argv[1], "st") == 0)
    {
        rc = sort(argv[2], argv[3]);
        if (rc != SUCCESS)
            return rc;

        FILE *f = fopen(argv[3], "w");

        if (f == NULL)
            return FILE_DOESNT_EXIST;

        if (rc == FILE_DOESNT_EXIST)
            return FILE_DOESNT_EXIST;
        else if (rc == FILE_DATA_ERROR)
            return FILE_DATA_ERROR;
        else if (rc == FILE_READING_ERROR)
            return FILE_READING_ERROR;
        else if (rc == WRONG_ARG)
            return WRONG_ARG;
    }

    else if ((argc == 3) && strcmp(argv[1], "at") == 0)
    {
        if (fgets(buffer, MAX_BUFFER, stdin) == NULL)
            return INCORRECT_INPUT;

        str_del_end(buffer);

        if (strlen(buffer) == 0 || strlen(buffer) > NAME_LENGTH)
            return INCORRECT_INPUT;

        strcpy(product.name, buffer);

        if (fgets(buffer, MAX_BUFFER, stdin) == NULL)
            return INCORRECT_INPUT;

        str_del_end(buffer);

        if (strlen(buffer) == 0 || strlen(buffer) > BRAND_NAME_LENGTH)
            return INCORRECT_INPUT;

        strcpy(product.brand, buffer);

        if (fgets(buffer, MAX_BUFFER, stdin) == NULL)
            return INCORRECT_INPUT;

        str_del_end(buffer);

        if (strlen(buffer) == 0)
            return INCORRECT_INPUT;

        num = strtol(buffer, &p_end, 10);

        if (p_end == NULL)
            return INCORRECT_INPUT;

        if (num < 0)
            return INCORRECT_INPUT;
        product.price = (unsigned int) num;

        if (fgets(buffer, MAX_BUFFER, stdin) == NULL)
            return INCORRECT_INPUT;

        str_del_end(buffer);

        if (strlen(buffer) == 0)
            return INCORRECT_INPUT;

        num = strtol(buffer, &p_end, 10);

        if (p_end == NULL)
            return INCORRECT_INPUT;

        if (num < 0)
            return INCORRECT_INPUT;

        product.amount = (unsigned int) num;
        rc = append_product(argv[2], product);

        if (rc == FILE_READING_ERROR)
            return FILE_READING_ERROR;

        if (rc == WRONG_ARG)
            return WRONG_ARG;
    }
//    else if (argc == 4 && strcmp(argv[1], "ft") == 0)
//    {
//        struct products new_product[100];
//        int new_product_number = 0;

//        rc = find_substr(product, &product_number, new_product, &new_product_number, argv[3]);
//        if (rc != SUCCESS)
//            return rc;

//        write_to_file(stdout, new_product, new_product_number);
////        write_to_file(f, new_product, new_product_number);
//    }
    else
        return KEY_ERROR;

    return SUCCESS;
}

