#include <stdio.h>

#include "my_strchr.h"

/* Возвращает адрес символа c в строке s, начиная с головы, или NULL, если
 * строка s не содержит символ c */
char *my_strchr(const char *str, const char c)
{
    int i;
    for (i = 0; str[i]; ++i)
        if (str[i] == c)
            return (char*) str + i;

    if (str[i] == c)
        return (char*) str + i;

    return NULL;
}
