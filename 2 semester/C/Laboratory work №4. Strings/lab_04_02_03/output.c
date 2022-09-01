#include <stdio.h>

#include "const.h"
#include "functions.h"

/* Вывод неповторяющихся слов из двух массивов */
int print_words(char words_array_1[][MAX_LEN_WORD], int word_count_1,
char words_array_2[][MAX_LEN_WORD], int word_count_2)
{
    int flag = FALSE;
    for (int i = 0; i < word_count_1; ++i)
        if (search_duplicate(i, words_array_1, word_count_1, words_array_2, word_count_2))
        {
            if (!flag)
            {
                printf("Result: %s", words_array_1[i]);
                flag = 1;
            }
            else
                printf(" %s", words_array_1[i]);
        }

    for (int i = 0; i < word_count_2; ++i)
        if (search_duplicate(i, words_array_2, word_count_2, words_array_1, word_count_1))
        {
            if (!flag)
            {
                printf("Result: %s", words_array_2[i]);
                flag = 1;
            }
            else
                printf(" %s", words_array_2[i]);
        }

    if (flag)
        return CORRECT;
    else
        return INCORRECT_ENTER;
}
