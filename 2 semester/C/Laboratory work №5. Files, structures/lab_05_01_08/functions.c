#include <stdio.h>
#include <stdlib.h>
//#include <limits.h>

#include "constants.h"

// Поиск наименьшей дистанции между двумя локальными максимумами
int process(FILE *f)
{
//    int min_distance = INT_MAX;
    int min_distance = 10000;
    int number_1, number_2, number_3;
    int local_max_1 = 1000, local_max_2 = 1000;
//    int curr_distance = INT_MAX;
    int counter = 0;

    if (f == NULL)
        return NULL_POINTER_ERROR;
    else if (ferror(f))
        return FILE_ERROR;
    else if (fseek(f, 0, SEEK_SET))
        return SEEK_ERROR;

    if (fscanf(f, "%d", &number_1) != TRUE || fscanf(f, "%d", &number_2) != TRUE || fscanf(f, "%d", &number_3) != TRUE)
        return NULL_POINTER_ERROR;

    if (number_2 > number_1 && number_2 > number_3)
        local_max_2 = 2;

    counter = 3;

    while (TRUE)
    {
        number_1 = number_2;
        number_2 = number_3;

        if (fscanf(f, "%d", &number_3) != TRUE)
            break;

        if (number_2 > number_1 && number_2 > number_3)
        {
            local_max_1 = local_max_2;
            local_max_2 = counter;

            if (local_max_2 - local_max_1 < abs(min_distance))
                min_distance = local_max_2 - local_max_1;
        }

        ++counter;
    }

    if (local_max_1 == 1000 || local_max_2 == 1000)
        return NO_LOCAL_MAX;

    if (min_distance == 10000)
        return NO_LOCAL_MAX;

    printf("%d", min_distance);

    return SUCCESS;
}
