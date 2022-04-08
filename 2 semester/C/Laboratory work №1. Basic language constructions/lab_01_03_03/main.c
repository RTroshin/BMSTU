#include <stdio.h>

int main(void)
{
    float v0, a, t;
    double s;

    printf("Enter speed, acceleration and time:\n");
    scanf("%f%f%f", &v0, &a, &t);

    s = v0 * t + a * t * t / 2;

    printf("Distance is %.6f\n", s);

    return 0;
}
