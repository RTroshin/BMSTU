# Тесты для задачи lab_04_03_01

## Входные данные
Строка: str

## Выходные данные
Строка: new_str

## Позитивные тесты
- 01 - обычный тест;
- 02 - в str введена строка, в которой только одно слово совпадает с последним;
- 03 - в str введена строка, в которой только одно слово не совпадает с последним;
- 04 - в str введена строка, в которой только неповторяющиеся слова;
- 05 - в str введена строка, в которой есть слова, состоящие из одной буквы;
- 06 - в str введена строка, в которой есть слова, состоящие только из одной повторяющейся буквы;

- 07 - в str введена строка, в которой слова содержат цифры;
- 08 - в str введена строка, в которой слова состоят только из цифр;
- 09 - в str введена строка, в которой есть слова состоящие только из букв и только из цифр;

- 10 - в str введена строка, в которой слова содержат символы " ,;:-.!?";
- 11 - в str введена строка, в которой слова разделены большим количеством символов " ,;:-.!?";
- 12 - в str введена строка, начинающияся с символов " ,;:-.!?";
- 13 - в str введена строка, заканчивающияся символами " ,;:-.!?";
- 14 - в str введена строка, начинающияся и заканчивающиеся символами " ,;:-.!?";
- 15 - в str введена строка, начинающияся и заканчивающиеся символами " ,;:-.!?"
       и в которой слова разделены большим количеством символов " ,;:-.!?";.

## Негативные тесты
- 01 - в str введена пустая строка;
- 02 - в str введена строка размером больше 256 символов;
- 03 - в str введено слово размером больше 16 символов;
- 04 - в str введена, состоящая только из символов " ,;:-.!?";
- 05 - в str введена, состоящая одного слова;
- 06 - в str введена, состоящая только из повторяющихся слов.