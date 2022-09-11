#include <stdio.h>

#include "my_strrchr.h"

/* Возвращает адрес символа c в строке s, начиная с хвоста, или NULL, если
 * строка s не содержит символ c */
char *my_strrchr(const char *str, const char c)
{
    int str_size = 0;
    int i;

    for (i = 0; str[i]; ++i)
        ++str_size;

    for (i = str_size; str[i] != str[0]; --i)
        if (str[i] == c)
            return (char*) str + i;

    if (str[i] == c)
        return (char*) str + i;

    return NULL;
}
