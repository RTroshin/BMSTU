#include <stdio.h>
#include <string.h>

#include "const.h"
#include "functions.h"

/* Вывод массива слов */
int print_words(char words_array[][MAX_LEN_WORD], int word_count)
{
    char new_str[MAX_LEN_STRING] = "";

    int str_len = 0;
    for (int i = word_count; i >= 0; i--)
        if (strcmp(words_array[word_count - 1], words_array[i]))
        {
            form_word(words_array[i]);
            form_new_str(new_str, &str_len, words_array[i]);
        }

    if (new_str[0] && word_count)
    {
        new_str[str_len - 1] = '\0';
        printf("Result: %s\n", new_str);
        return CORRECT;
    }
    else
        return INCORRECT_ENTER;
}

