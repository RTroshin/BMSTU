#include "my_strcspn.h"

/* Определяет максимальную длину начальной подстроки, состоящей исключительно
 * из байтов, не перечисленных в reject */
int my_strcspn(const char *str, const char *reject)
{
    int i = 0;

    for (i = 0; str[i]; ++i)
        for (int j = 0; reject[j]; ++j)
            if (str[i] == reject[j])
                return i;

    return i;
}
