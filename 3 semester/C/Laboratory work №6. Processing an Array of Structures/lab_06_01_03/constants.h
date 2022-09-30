#ifndef CONSTANTS_H

#define CONSTANTS_H

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "struct.h"           // Структура
#include "io.h"               // Функции ввода/вывода и проверки файла

#define SUCCESS 0
#define FILE_READING_ERROR 1  // Ошибка чтения файла
#define FILE_DATA_ERROR 2     // Ошибка данных в файле
#define FILE_CLOSE_ERROR 3    // Ошибка закрытия файла
#define WRONG_ARG 4           // Ошибка количества аргументов строки

#define INCORRECT_INPUT -1    // Некорректный ввод
#define NAME_OVERFLOW -2      // Переполнение наименования
#define NAME_ERROR -3         // Ошибка, пробельный символ в названии продукта
#define PRICE_ERROR -4        // Ошибка, неверно задана цена продукта
#define STRUCT_ERROR -5       // Ошибка, неверное количество структур

#endif // CONSTANTS_H
