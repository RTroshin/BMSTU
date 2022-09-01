#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "const.h"

/* Поиск неповторяющихся слов в массивах */
int search_duplicate(int i, char words_array_1[][MAX_LEN_WORD], int word_count_1,
char words_array_2[][MAX_LEN_WORD], int word_count_2)
{
    int flag = TRUE;
    for (int j = 0; j < word_count_1; ++j)
        if (!strcmp(words_array_1[i], words_array_1[j]) && i != j)
        {
            flag = FALSE;
            break;
        }

    for (int j = 0; j < word_count_2; ++j)
        if (!strcmp(words_array_1[i], words_array_2[j]))
        {
            flag = FALSE;
            break;
        }

    return flag;
}

/* Разбиение строки на слова */
int strsplit(char *str, char words_array[][MAX_LEN_WORD])
{
    int word_count = 0;
    int start = 0;

    for (int i = 0, j = 0, k = 0; str[j] ; ++i, ++word_count)
    {
        int word_len = 0;

        while (!isalpha(str[start]) && !isdigit(str[start]) && str[start])
            ++start;

        for (j = start, k = 0; str[j]; ++j, ++k)
            if (isalpha(str[j]) || isdigit(str[j]))
            {
                words_array[i][k] = str[j];
                ++word_len;
                ++start;
            }
            else
                break;

        if (word_len > MAX_LEN_WORD)
            return WORD_OVERFLOW;

        if (!str[start])
            break;
        else
            words_array[i][k] = '\0';
    }

    if (word_count == 0)
        return EMPTY_STRING;

    return word_count;
}
