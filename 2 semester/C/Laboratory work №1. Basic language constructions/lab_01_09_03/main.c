#include <stdio.h>
#include <math.h>

float computing_g(int, float);

int main(void)
{
    float x;
    float g = 1.0;
    int n = 1;
    int rc;

    printf("Enter sequance numbers where xn >= zero:\n");
    rc = scanf("%f", &x);
    if (rc != 1)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    if (x < 0)
    {
        printf("Empty enum\n");
        return 1;
    }

    while (x >= 0)
    {
        g *= computing_g(n, x);
        ++n;

        rc = scanf("%f", &x);
        if (rc != 1)
        {
            printf("Error: Incorrect enter\n");
            return 1;
        }
    }

    printf("Value of g: %.6f\n", expf(g));

    return 0;
}

float computing_g(int n, float x)
{
    return 1 / (x + n);
}