#include <stdio.h>
#include <math.h>

int point_position(double, double, double, \
double, double, double);

int main(void)
{
    double xq, yq, xr, yr, xp, yp;
    int answer;
    int rc;

    printf("Enter coordinates for first point (xq, yq):\n");
    rc = scanf("%lf%lf", &xq, &yq);
    if (rc != 2)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }
    printf("Enter coordinates for second point (xr, yr):\n");
    rc = scanf("%lf%lf", &xr, &yr);
    if (rc != 2)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }
    printf("Enter coordinates for arbitrary point (xp, yp):\n");
    rc = scanf("%lf%lf", &xp, &yp);
    if (rc != 2)
    {
        printf("Error: Incorrect enter\n");
        return 1;
    }

    answer = point_position(xq, yq, xr, yr, xp, yp);
    if (answer == 3 || answer == 4)
        return answer;

    printf("\nAnswer is %d\n", answer);

    return 0;
}

/* Проверка с помощью псевдоскалярного произведения, лежит ли точка
   выше прямой, на прямой или ниже прямой */
int point_position(double xq, double yq, double xr, \
double yr, double xp, double yp)
{
    int result = 5;
    double eps = 1e-8;
    double expression_1 = (xq - xr) * (yq - yp);
    double expression_2 = (xq - xp) * (yq - yr);

/* Проверка на вырожденность прямой (начальная и конечная точка равны) */
    if (fabs(xq - xr) < eps && fabs(yq - yr) < eps)
    {
        printf("The straight line is not exist\n");
        result = 3;
    }
/* Проверка на вертикальное расположение прямой */
    else if (fabs(xq - xr) < eps && !(fabs(expression_1 - expression_2) < eps))
    {
        printf("\nThe straight line is vertical\n");
        result = 4;
    }
/* Точка находится на прямой */
    else if (fabs((xq - xr) * (yq - yp) - (yq - yr) * (xq - xp)) < eps)
        result = 1;
/* Точка находится выше прямой */
    else if ((xq - xr) * (yq - yp) - (yq - yr) * (xq - xp) > 0)
        result = 0;
/* Точка находится под прямой */
    else if ((xq - xr) * (yq - yp) - (yq - yr) * (xq - xp) < 0)
        result = 2;
    return result;
}
