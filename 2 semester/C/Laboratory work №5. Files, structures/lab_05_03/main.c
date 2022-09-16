#include <stdio.h>
#include <string.h>

#include "constants.h"
#include "functions.h"
#include "io.h"

int main(int argc, char **argv)
{
    int rc;

    if (argc == 4)
    {
        if (strcmp(argv[1], "c") == 0)
        {
            if ((rc = create_file(argv[3], RANDOM, argv[2])) != 0)
                return rc;
        }
        else
            return KEY_ERROR;
    }
    else if (argc != 3)
        return NO_KEYS;
    else if (strcmp(argv[1], "p") == 0)
    {
        if ((rc = read_file(argv[argc - 1])) != 0)
            return rc;
    }
    else if (strcmp(argv[1], "s") == 0)
    {
        if ((rc = sort(argv[argc - 1])) != 0)
            return rc;
    }
    else
        return KEY_ERROR;

    return SUCCESS;
}

