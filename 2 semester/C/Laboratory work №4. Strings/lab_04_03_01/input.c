#include <stdio.h>

#include "const.h"

/* Вычисление длины строки */
int my_strlen(char *str)
{
    int str_size = 0;

    for (int i = 0; str[i]; ++i)
        ++str_size;

    return str_size;
}

/* Ввод строки */
char input_string(char *str)
{
    if (fgets(str, MAX_LEN_STRING + 1, stdin) == NULL)
        return INCORRECT_ENTER;
    else if (my_strlen(str) > MAX_LEN_STRING - 1)
        return STRING_OVERFLOW;
    else if (str[0] == '\n' || str[0] == '\0')
        return EMPTY_STRING;
    return CORRECT;
}
