#include <stdio.h>
#include <math.h>

double function(float);
double approximate_sum(float, float, float);

int main(void)
{
    float x, x2;
    float eps;
    int rc;
    double f, sum;

    printf("Enter value of x:\n");
    rc = scanf("%f", &x);
    if (rc != 1 || fabs(x) > 1)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    printf("Enter value of eps:\n");
    rc = scanf("%f", &eps);
    if (rc != 1 || eps <= 0 || eps > 1)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    f = function(x);
    x2 = x * x;
    sum = approximate_sum(x, x2, eps);

    printf("\nValue of function s(x): %.6f\n\
Approximate value f(x): %.6f\n\
Absolute error:         %.6f\n\
Observational error:    %.6f\n", \
    sum, f, fabs(f - sum), fabs(f - sum) / fabs(f));

    return 0;
}

double function(float x)
{
    return atan(x);
}

double approximate_sum(float x, float x2, float eps)
{
    int i = 1;
    double value = x;
    double sum = x;

    while (fabs(value) >= eps)
    {
        i += 2;
        value *= (-1) * x2 * (i - 2) / i;
        sum += value;
    }
    return sum;
}
