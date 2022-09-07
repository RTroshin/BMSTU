#include <stdio.h>
#include <string.h>

#include "my_strpbrk.h"
#include "my_strspn.h"
#include "my_strcspn.h"
#include "my_strchr.h"
#include "my_strrchr.h"

#define CORRECT 0
#define INCORRECT_ENTER 1

int main(void)
{
    int test_1, test_2;
    char *pc_test_1, *pc_test_2;

    int result = 1;
    int rc = CORRECT;

    /* Тест strpbrk и my_strpbrk */

    pc_test_1 = strpbrk("Hello world!", "abcde");
    pc_test_2 = my_strpbrk("Hello world!", "abcde");
    result &= pc_test_1 == pc_test_2;

    printf("strpbrk:\n%s\n", pc_test_1); // "ello world!"
    printf("my_strpbrk:\n%s\n", pc_test_2); // "ello world!"
    printf("\n");

    if (!strpbrk("Hello world!", "xyz"))
        printf("Error! strpbrk returned NULL\n");
    if (!my_strpbrk("Hello world!", "xyz"))
        printf("Error! my_strpbrk returned NULL\n");
    printf("\n");

    if (!strpbrk("", "xyz"))
        printf("Error! strpbrk returned NULL\n");
    if (!my_strpbrk("", "xyz"))
        printf("Error! my_strpbrk returned NULL\n");
    printf("\n");

    /* Тест strspn и my_strspn */

    test_1 = strspn("Hello world!", "olleH");
    test_2 = my_strspn("Hello world!", "olleH");
    result &= test_1 == test_2;

    printf("strspn:\n%d\n", test_1); // 4
    printf("my_strspn:\n%d\n", test_2); // 4
    printf("\n");

    test_1 = strspn("Hello world!", "zyx");
    test_2 = my_strspn("Hello world!", "zyx");
    result &= test_1 == test_2;

    printf("strspn:\n%d\n", test_1); // 0
    printf("my_strspn:\n%d\n", test_2); // 0
    printf("\n");

    test_1 = strspn("", "zyx");
    test_2 = my_strspn("", "zyx");
    result &= test_1 == test_2;

    printf("strspn:\n%d\n", test_1); // 0
    printf("my_strspn:\n%d\n", test_2); // 0
    printf("\n");

    /* Тест strcspn и my_strcspn */

    test_1 = strcspn("Hello world!", "wrd!");
    test_2 = my_strcspn("Hello world!", "wrd!");
    result &= test_1 == test_2;

    printf("strcspn:\n%d\n", test_1); // 6
    printf("my_strcspn:\n%d\n", test_2); // 6
    printf("\n");

    test_1 = strcspn("Hello world!", "xyz?");
    test_2 = my_strcspn("Hello world!", "xyz?");
    result &= test_1 == test_2;

    printf("strcspn:\n%d\n", test_1); // 0
    printf("my_strcspn:\n%d\n", test_2); // 0
    printf("\n");

    test_1 = strcspn("", "xyz?");
    test_2 = my_strcspn("", "xyz?");
    result &= test_1 == test_2;

    printf("strcspn:\n%d\n", test_1); // 0
    printf("my_strcspn:\n%d\n", test_2); // 0
    printf("\n");

    test_1 = strcspn("Hello world!", "");
    test_2 = my_strcspn("Hello world!", "");
    result &= test_1 == test_2;

    printf("strcspn:\n%d\n", test_1); // 0
    printf("my_strcspn:\n%d\n", test_2); // 0
    printf("\n");

    test_1 = strcspn("", "");
    test_2 = my_strcspn("", "");
    result &= test_1 == test_2;

    printf("strcspn:\n%d\n", test_1); // 0
    printf("my_strcspn:\n%d\n", test_2); // 0
    printf("\n");

    /* Тест strchr и my_strchr */

    pc_test_1 = strchr("Hello world!", 'l');
    pc_test_2 = my_strchr("Hello world!", 'l');
    result &= pc_test_1 == pc_test_2;

    printf("strchr:\n%s\n", pc_test_1); // "llo world!"
    printf("my_strchr:\n%s\n", pc_test_2); // "llo world!"
    printf("\n");

    if (!strchr("Hello world!", 'x'))
        printf("Error! strchr returned NULL\n");
    if (!my_strchr("Hello world!", 'x'))
        printf("Error! my_strchr returned NULL\n");
    printf("\n");

    if (!strchr("", 'x'))
        printf("Error! strchr returned NULL\n");
    if (!my_strchr("", 'x'))
        printf("Error! my_strchr returned NULL\n");
    printf("\n");

    if (strchr("", '\0'))
        printf("Error! strchr returned NULL\n");
    if (my_strchr("", '\0'))
        printf("Error! my_strchr returned NULL\n");
    printf("\n");

    /* Тест strrchr и my_strrchr */

    pc_test_1 = strrchr("Hello world!", 'l');
    pc_test_2 = my_strrchr("Hello world!", 'l');
    result &= pc_test_1 == pc_test_2;

    printf("strrchr:\n%s\n", pc_test_1); // "ld!"
    printf("my_strrchr:\n%s\n", pc_test_2); // "ld!"
    printf("\n");

    if (!strrchr("Hello world!", 'x'))
        printf("Error! strrchr returned NULL\n");
    if (!my_strrchr("Hello world!", 'x'))
        printf("Error! my_strrchr returned NULL\n");
    printf("\n");

    if (!strrchr("", 'x'))
        printf("Error! strrchr returned NULL\n");
    if (!my_strrchr("", 'x'))
        printf("Error! my_strrchr returned NULL\n");
    printf("\n");

    if (strrchr("", '\0'))
        printf("Error! strchr returned NULL\n");
    if (my_strrchr("", '\0'))
        printf("Error! my_strchr returned NULL\n");
    printf("\n");

    printf("\nResult: %d\n", result); // 1

    return rc;
}
