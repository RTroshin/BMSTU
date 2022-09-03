#include <stdio.h>

#include "const.h"
#include "input.h"
#include "output.h"
#include "functions.h"

int main(void)
{
    char str[MAX_LEN_STRING + 1] = "";

    char words_array[MAX_WORDS_COUNT][MAX_LEN_WORD];
    int word_count = 0;

    int rc = CORRECT;

    setbuf(stdout, NULL);

    printf("Input string:\n");
    rc = input_string(str);
    if (rc)
        return rc;

    word_count = strsplit(str, words_array);
    if (word_count < 0)
        return word_count;

    rc = print_words(words_array, word_count);

    return rc;
}
