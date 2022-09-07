#include <stdio.h>

#include "my_strpbrk.h"

/* Находит первое вхождение любого симмвола, перечисленного в accept */
char *my_strpbrk(const char *str, const char *accept)
{
    for (int i = 0; str[i]; ++i)
        for (int j = 0; accept[j]; ++j)
            if (str[i] == accept[j])
                return (char*) str + i;

    return NULL;
}
