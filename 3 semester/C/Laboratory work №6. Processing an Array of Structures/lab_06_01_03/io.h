#ifndef IO_H

#define IO_H

#include "constants.h"

int test_file(int, char**);
int read_file(char**, struct products*, int*);
void print_products(struct products*, int*, char**);

#endif // IO_H
