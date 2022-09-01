#include <stdio.h>

#include "const.h"
#include "input.h"
#include "output.h"
#include "functions.h"

int main(void)
{
    char str_1[MAX_LEN_STRING + 1] = "";
    char str_2[MAX_LEN_STRING + 1] = "";

    char words_array_1[MAX_WORDS_COUNT][MAX_LEN_WORD];
    words_array_1[0][0] = ' ';
    char words_array_2[MAX_WORDS_COUNT][MAX_LEN_WORD];
    words_array_2[0][0] = ' ';
    int word_count_1 = 0, word_count_2 = 0;

    int rc = CORRECT;

    setbuf(stdout, NULL);

    printf("Input first string:\n");
    rc = input_string(str_1);
    if (rc)
        return rc;

    word_count_1 = strsplit(str_1, words_array_1);
    if (word_count_1 < 0)
        return word_count_1;

    printf("Input second string:\n");
    rc = input_string(str_2);
    if (rc)
        return rc;

    word_count_2 = strsplit(str_2, words_array_2);
    if (word_count_2 < 0)
        return word_count_2;

    rc = print_words(words_array_1, word_count_1, words_array_2, word_count_2);

    return rc;
}
