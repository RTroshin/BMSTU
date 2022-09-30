#include "constants.h"
#include "io.h"

int main(int argc, char *argv[])
{
    setbuf(stdout, NULL);

    struct products product[15];
    int product_number;

    int rc = test_file(argc, argv);
    if (rc != SUCCESS)
        return rc;

    rc = read_file(argv, product, &product_number);
    if (rc != SUCCESS)
        return rc;

    print_products(product, &product_number, argv);

    return SUCCESS;
}
