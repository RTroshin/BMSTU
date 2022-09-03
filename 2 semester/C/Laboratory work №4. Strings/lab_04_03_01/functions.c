#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "const.h"

/* Удаление в слове всех вхождений каждой буквы, кроме первых */
void delete_letter(int *index, int start, char *word)
{
    for (int i = start; word[i - 1]; ++i)
        word[i] = word[i + 1];
    --(*index);
}

/* Удаление в слове первых вхождений каждой буквы */
void form_word(char *word)
{
    for (int i = 0; i < word[i]; ++i)
        for (int j = 0; word[j]; ++j)
            if ((word[i] == word[j]) && i != j)
                delete_letter(&i, j, word);
}

/* Создание строки из массива слов */
void form_new_str(char *new_str, int *str_len, char *words_array)
{
    for (int i = 0; i < (int) strlen(words_array) + 1; ++i)
    {
        if (isalnum(words_array[i]))
            new_str[(*str_len)++] = words_array[i];
        else if (*str_len)
            new_str[(*str_len)++] = ' ';
    }
}

/* Разбиение строки на слова с помощью strtok */
int strsplit(char *str, char words_array[][MAX_LEN_WORD])
{
    int word_count = 0;
    char *temp = str;
    char *sep = " ,;:-.!?\n";

    temp = strtok(str, sep);

    for (int i = 0; temp; ++i)
    {
        if (strlen(temp) > MAX_LEN_WORD)
            return WORD_OVERFLOW;

        ++word_count;
        strncpy(words_array[i], temp, MAX_LEN_WORD + 1);
        temp = strtok(NULL, sep);
    }

    return word_count;
}
