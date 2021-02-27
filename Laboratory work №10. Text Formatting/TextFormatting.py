# Программа "Text formatting"
# 

# Задан текст массивом строк. Текст - фрагмент литературного произведения
# (5-7 предложений). Ни одна строка не оканчивается точкий кроме последней.
# Текст задаётся в программе, пользовательский ввод не требуется.
# Необходимо создать меню, выполняющее следующие действия:

# 1. Выравнивание текста по левому краю.
# 2. Выравнивание текста по правому краю.
# 3. Выравнивание текста по ширине.
# 4. Удаление заданного слова.
# 5. Замена одного слова другим во всем тексте.
# 6. Вычисление арифметического выражения.
# 7. Индивидуальное задание.

# Варианты индивидуальных заданий:

# 1. Найти предложение с максимальным количеством слов, в которых гласные
# чередуются с согласными.
# 2. Найти предложение, в котором слово с максимальным количеством
# согласных букв.
# 3. Найти предложение с максимальным количеством слов, начинающихся на
# заданную букву.
# 4. Определить сколько имеется слов из 2,3,4 букв в каждом предложении.
# 5. Удалить самое длинное слово в самом коротком по числу слов предложении.
# 6. Отсортировать слова в лексикографическом пор€дке в самом длинном по
# количеству символов предложении.
# 7. В каждом четном предложении определить самый часто встречающийся
# символ.
# 8. Удалить самое короткое слово в самом длинном по числу слов предложении.
# 9. Найти предложение, в котором максимальное количество слов, в которых
# каждая буква входит не менее двух раз.
# 10. Найти наиболее часто встречающееся слово в каждом предложении.
# 11. Найти и напечатать предложения, в которых количество слов совпадает.
# 
# Номер по номер журналу варианта
# 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10
# Номер по номер журналу варианта
# 11 11 12 1 13 2 14 3 15 4 16 5 17 6 18 7 19 8 20 9
# Номер по номер журналу варианта
# 21 10 22 11 23 1 24 2 25 3 26 4 27 5 28 6 29 7 30 8
# 

from math import e, pi, sqrt


# Главная функция
def main():

    longest_line_len = 0

    text = ['Текст']

    for line in text:
        line_len = len(line)
        if longest_line_len < line_len:
            longest_line_len = line_len

    print(*text, sep = '\n')

    while True:
        userChoice = menu()
        if userChoice == '1':
            for line in text:
                print(line.ljust(longest_line_len)) 
        elif userChoice == '2':
            for line in text:
                print(line.rjust(longest_line_len))
        elif userChoice == '3':
            for line in text:
                line_len = len(line)
                words = line.split()
                words_len = len(words)
                if words_len < 2 or line_len == longest_line_len:
                    print(line)
                else:
                    space_width = (longest_line_len - line_len + words_len) // (
                            words_len - 1)
                    print(*words[:-1], sep = ' ' * space_width, end = '')
                    print(
                        words[-1].rjust(
                            longest_line_len - line_len +
                            len(words[-1]) + words_len - 1 -
                            space_width * (words_len - 2)
                        )
                    )
        elif userChoice == '4':
            word = input('Введите слово для удаления: ')
            deleteWord = ''

            # for string in text:
            #     # if string.find(word):
            #     string = string.replace(word.strip(), deleteWord.strip())
            
            lenText = len(text) - 1
            for i in range(lenText):
                text[i] = text[i].replace(word +  ' ', deleteWord) # НЕМНОГО УЛУЧШИЛ!

            # text = [string.replace(word.strip(), deleteWord.strip()) for string in text] ИСПОЛЬЗОВАТЬ! ЭТО ГЕНЕРАТОР!

            for string in text: # ЗАМЕНИТЬ ФУНКЦИЕЙ!
                print(string)
            # [print(string) for string in text] НОВЫЙ СПОСОБ ВЫВОДА!

        elif userChoice == '5':
            word = input('Введите слово для замены: ')
            newWord = input('Введите слово, на которое хотите заменить: ')

            # for string in text:
            #     string.replace(word.strip(), newWord.strip())

            lenText = len(text) - 1
            for i in range(lenText):
                text[i] = text[i].replace(word, newWord) # НЕМНОГО УЛУЧШИЛ!

            # text = [string.replace(word.strip(), newWord.strip()) for string in text] ИСПОЛЬЗОВАТЬ! ЭТО ГЕНЕРАТОР!

            for string in text: # ЗАМЕНИТЬ ФУНКЦИЕЙ!
                print(string)
            # [print(string) for string in text] НОВЫЙ СПОСОБ ВЫВОДА!

        # elif userChoice == '6':

        # elif userChoice == '7':

        # Выход из программы
        elif userChoice.lower() == 'выход':
            exit()
        else:
            print('Такого пункта нет в меню!')

# Меню программы
def menu():
    print('\nМеню')
    print('1. Выравнивание текста по левому краю')
    print('2. Выравнивание текста по правому краю')
    print('3. Выравнивание текста по ширине')
    print('4. Удаление заданного слова')
    print('5. Замена одного слова другим во всём тексте')
    print('6. Вычисление арифметического выражения')
    print('7. Найти предложение, в котором максимальное количество слов, '
        + 'в которых каждая буква входит не менее двух раз')
    print('7. Удалить самое короткое слово в самом длинном по числу слов предложении')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()
    return userChoice


if __name__ == "__main__":
    main()