#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "const.h"

/* Проверка коррекности номера абонента */
int check_subscriber_number(int *start, char *str)
{
    int i;

    if (str[*start] == ')' && str[++(*start)] == '-')
    {
        for (i = *start + 1; i < 4 + *start; ++i)
            if (!isdigit(str[i]))
                return INCORRECT;

        *start = i;
        if (str[i] == '-')
        {
            for (i = *start + 1; i < 3 + *start; ++i)
                if (!isdigit(str[i]))
                    return INCORRECT;
        }
        else
            return INCORRECT;

        *start = i;
        if (str[i] == '-')
        {
            for (i = *start + 1; i < 3 + *start; ++i)
                if (!isdigit(str[i]))
                    return INCORRECT;
        }
        else
            return INCORRECT;
    }
    else
        return INCORRECT;

    *start = i;

    return CORRECT;
}

/* Проверка коррекности номера оператора связи */
int check_operator_code(int *start, char *str)
{
    int i;

    if (str[*start] == '(')
    {
        for (i = *start + 1; i < 4 + *start; ++i)
            if (!isdigit(str[i]))
                return INCORRECT;
        *start = i;
    }
    else
        return INCORRECT;

    return CORRECT;
}

/* Проверка коррекности кода страны */
int check_country_code(int *start, char *str)
{
    int i;

    if (str[*start] == '(')
        return CORRECT;

    if (str[*start] == '+' && str[*start + 1] != '(')
    {
        for (i = *start + 1; ; ++i)
            if (str[i] == '(')
                break;
            else if (!isdigit(str[i]))
                return INCORRECT;
        *start = i;
    }
    else
        return INCORRECT;

    return CORRECT;
}

/* Проверка строки на пробельные символы */
int check_space(int *start, char *str)
{
    for (int i = *start; str[i]; ++i)
    {
        if (!(*start))
        {
            if (!isspace(str[i]) || str[i] == '+' || str[i] == '(')
            {
                *start = i;
                return CORRECT;
            }
        }
        else
        {
            if (!isspace(str[i]))
                return INCORRECT;
        }
    }

    return CORRECT;
}

/* Проверка коррекности записи телефонного номера */
int check_phone_number(char *str)
{
    int start = 0;
    int rc;

    rc = check_space(&start, str);
    if (rc)
        return INCORRECT;
    rc = check_country_code(&start, str);
    if (rc)
        return INCORRECT;
    rc = check_operator_code(&start, str);
    if (rc)
        return INCORRECT;
    rc = check_subscriber_number(&start, str);
    if (rc)
        return INCORRECT;
    rc = check_space(&start, str);
    if (rc)
        return INCORRECT;

    return CORRECT;
}
