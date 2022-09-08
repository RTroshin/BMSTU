#include "my_strspn.h"

/* Булевы константы */
#define TRUE 1
#define FALSE 0

/* Определяет максимальную длину начальной подстроки, состоящей исключительно
 * из байтов, перечисленных в accept */
int my_strspn(const char *str, const char *accept)
{
    int result = 0;
    int bool;

    for (int i = 0; str[i]; ++i)
    {
        bool = FALSE;
        for (int j = 0; accept[j]; ++j)
            if (str[i] == accept[j])
            {
                bool = TRUE;
                result = i + 1;
            }
        if (!bool)
            break;
    }
    return result;
}
