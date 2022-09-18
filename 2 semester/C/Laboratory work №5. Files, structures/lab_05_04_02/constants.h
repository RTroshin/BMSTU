#ifndef CONSTANTS_H

#define CONSTANTS_H

#include <stdio.h>
#include <string.h>
//#include <stdint.h>
//#include <inttypes.h>

#include "a_task.h"            // Функции для сортировки полей структуры
#include "b_task.h"            // Функции для вывода продуктов в указанный файл
#include "struct.h"            // Структура
#include "io.h"                // Функции ввода/вывода и проверки файла

#define SUCCESS 0
#define FILE_READING_ERROR 1   // Ошибка чтения файла
#define FILE_DATA_ERROR 2      // Ошибка данных в файле
#define FILE_CLOSE_ERROR 3     // Ошибка закрытия файла
#define FILE_CREATION_ERROR 4  // Ошибка создания файла
#define FILE_DOESNT_EXIST 5    // Ошибка, файл не существует
#define EMPTY_FILE 6           // Ошибка, файл пустой

#define INCORRECT_INPUT -1     // Некорректный ввод
#define NAME_OVERFLOW -2       // Переполнение наименования
#define BRAND_NAME_OVERFLOW -3 // Переполнение наименования изготовителя
#define PRICE_ERROR -4         // Ошибка, неверно задана цена продукта
#define AMOUNT_ERROR -5        // Ошибка, неверное количество продуктов
#define EMPTY_STRING -6        // Пустая строка
#define NO_FIT_PRODUCTS -7     // Нет подходящих продуктов

#define NO_KEYS 1              // Ошибка, ключи отсутствуют
#define WRONG_ARG 2            // Ошибка количества аргументов командной строки
#define MAX_BUFFER 256
#define KEY_ERROR 53           // Ошибка ключа

#define WRONG_ELEMENT 3        // Ошибка неверного заданного элемента

#define TRUE 1
#define FALSE 0

#endif // CONSTANTS_H
