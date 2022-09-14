#include "constants.h"
#include "functions.h"

int main(int argc, char **argv)
{
    int rc = test_file(argc, argv);
    if (rc != 0)
        return rc;

    FILE *f;

    int imin = 0, imax = 0;
    double average_sum;

    f = fopen(argv[1], "r");
    find_min_num(f, &imin);
    rewind(f);
    find_max_num(f, &imax);
    rewind(f);
    rc = find_average_sum(f, &imin, &imax, &average_sum);
    if (rc != 0)
        return rc;

    printf("%lf\n", average_sum);

    if (fclose(f) == EOF)
        return FILE_CLOSE_ERROR;

    return SUCCESS;
}
