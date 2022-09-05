#include <stdio.h>

#include "const.h"
#include "input.h"
#include "functions.h"

int main(void)
{
    char str[MAX_LEN_STRING + 1] = "";
    int rc = CORRECT;

    setbuf(stdout, NULL);

    rc = input_string(str);
    if (rc == INCORRECT_ENTER || rc == STRING_OVERFLOW)
        return rc;

    if (!rc)
        rc = check_phone_number(str);

    if (!rc)
        printf("YES");
    else
        printf("NO");

    return CORRECT;
}
