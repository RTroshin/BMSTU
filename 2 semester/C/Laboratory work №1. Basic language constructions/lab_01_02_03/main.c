#include <stdio.h>
#include <math.h>

#define PI 3.141592 // Число Пи

int main(void)
{
    float a, b;
    float angle;
    double s;

    printf("Enter sides a, b and angle between them:\n");
    scanf("%f%f%f", &a, &b, &angle);

    s = 0.5 * a * b * sin(angle * PI / 180);

    printf("Square triangle is %.6f\n", s);

    return 0;
}
