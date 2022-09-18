#ifndef IO_H

#define IO_H

#include "constants.h"

int test_file(int, char**);
int read_file(char*, struct products*);
char *str_del_end(char*);
void write_to_file(FILE*, struct products*, int);
void print_products(struct products*, int*);

#endif // IO_H
