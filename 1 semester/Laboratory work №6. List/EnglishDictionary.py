# Программа "English dictionary"
# Реализованы следующие возможности:
# 1. Просмотр слов в словаре. Вывод в виде таблицы.
#    Для этого необходимо ввести цифру "1" в главном меню
#    Если словарь пуст, то выводится соответствующиее сообщение
#
# 2. Добавление слова в словарь
#    Для этого необходимо ввести цифру "2"  в главном меню, после
#    чего требуется ввести слово на иностранном языке и его перевод
#    Слова добавляются в конец списка (последняя строка таблицы) и
#    после сортируются по алфавиту
#
# 3. Редактирование слова
#    Для этого необходимо ввести цифру "3"  в главном меню, после
#    чего требуется выбрать слово из таблицы, набрав
#    соответствующую цифру и нажать Enter. После этого
#    требуется ввести исправление слова на иностранном языке и его перевод
#
# 4. Удаление слова из словаря
#    Для этого необходимо ввести цифру "4"  в главном меню, после
#    чего требуется выбрать слово из таблицы, набрав
#    соответствующую цифру и нажать Enter. Если выполнить команду
#    "Просмотреть словарь", то можно увидеть, что слово удалено
#    из таблицы
#
# 5. Выход из программы
#    Для этого необходимо набрать слово "Выход"  в главном меню, после
#    чего нажать "ОК" во всплывающем окне
#

print()
print('Вас приветствует программа "English dictionary"!')
englishWords = ['cat', 'apple', 'car', 'water']
russianWords = ['кошка', 'яблоко', 'автомобиль', 'вода']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',\
            'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r',\
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numberWord = [3, 1, 3, 23]

while True:
    print('Меню\n')
    print('1. Просмотреть словарь')
    print('2. Добавить слово в словарь')
    print('3. Редактировать слово')
    print('4. Удалить слово из словаря\n')
    print('Для выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')

    # Выход из программы

    if userChoice.lower() == 'выход':
        exit()

    while True:
        if (userChoice == '1') or (userChoice == '2') or\
          (userChoice == '3') or (userChoice == '4'):
            break
        else:
            userChoice = input('Выберите пункт меню: ')
            if userChoice.lower() == 'выход':
                exit()
    print()

    # Вывод словаря на экран

    if userChoice == '1':
        if len(englishWords) == 0:
            print('Ваш словарь пуст!\n')
        else:
            number = 1
            print('┌', '─' * 5, '┬', '─' * 17, '┬', '─' * 17, '┐', sep = '')
            print('│  №  │      Слово      │     Перевод     │')
            print('├', '─' * 5, '┼', '─' * 17, '┼', '─' * 17, '┤', sep = '')
            for i in range(len(englishWords)):
                print('│{:^5d}│ {:<15} │ {:<15} │'\
                      .format(number, englishWords[i], russianWords[i]))
                if number != len(englishWords):
                    print('├', '─' * 5, '┼', '─' * 17, '┼', '─' * 17, '┤', sep = '')
                else:
                    print('└', '─' * 5, '┴', '─' * 17, '┴', '─' * 17, '┘', sep = '')                    
                number += 1
        print()

    # Добавление слова в словарь

    if userChoice == '2':
        add = True
        print('Добавление слова в словарь')
        enWord = input('Введите слово на английском языке: ')
        ruWord = input('Введите перевод слова на русском языке: ')
        print('-' * 43)
        for i in range(len(englishWords)):
            if enWord.lower() == englishWords[i]:
                print('\nТакое слово уже есть в Вашем словаре!')
                add = False
                break
        if add == True:
            englishWords.append(enWord.lower())
            russianWords.append(ruWord.lower())
            print('\nСлово "', enWord, '" добавлено!')
        print()

    # Редактировать слово

    if userChoice == '3':
        if len(englishWords) == 0:
            print('Ваш словарь пуст!\n')
        else:
            cor = True

            listNumber = int(input('Редактирование слова\n\
Выберите номер слова из списка: '))
            print('-' * 43)
            while (listNumber <= 0) or (listNumber > len(englishWords)):
                print('Номер в списке не найден!\nПопробуйте ещё раз!\n')
                listNumber = int(input('Выберите номер слова из списка: '))
            OldEnWord = englishWords[listNumber - 1]
            OldRoWord = russianWords[listNumber - 1]
            NewEnWord = input('\nРедактируйте слово: ')
            NewRuWord = input('Редактируйте перевод слова: ')
            for i in range(len(englishWords)):
                if NewEnWord.lower() == englishWords[i]:
                    print('\nТакое слово уже есть в Вашем словаре!')
                    cor = False
                    break
            if cor == True:
                englishWords.remove(englishWords[listNumber - 1])
                russianWords.remove(russianWords[listNumber - 1])
                englishWords.insert(listNumber - 1, NewEnWord.lower())
                russianWords.insert(listNumber - 1, NewRuWord.lower())
                print('\nСлово ', OldEnWord, ' (', OldRoWord,')\
 отредактировано на ', NewEnWord, ' (', NewRuWord,')')
        print()

    # Удаление слова из словаря

    if userChoice == '4':
        if len(englishWords) == 0:
            print('Ваш словарь пуст!\n')
        else:
            listNumber = int(input('Удаление слова из словаря\n\
Выберите номер слова из списка: '))
            print('-' * 43)
            while (listNumber <= 0) or listNumber > len(englishWords):
                print('Номер в списке не найден!\nПопробуйте ещё раз!\n')
                listNumber = int(input('Выберите номер слова из списка: '))
            englishWords.remove(englishWords[listNumber - 1])
            russianWords.remove(russianWords[listNumber - 1])
            numberWord.remove(numberWord[listNumber - 1])
        print()

    # Сортировка массива по алфавиту

    numberWord = []
    word = []
    for i in range(len(englishWords)):
        word = englishWords[i]
        for c in range(len(alphabet)):
            if (word[0] == alphabet[c]):
                if len(numberWord) < len(englishWords): 
                    numberWord.append(c + 1)

    swapped = True
    while swapped != False:
        swapped = False
        for i in range(len(numberWord) - 1):
            if numberWord[i + 1] < numberWord[i]:
                numberWord[i], numberWord[i + 1] =\
                numberWord[i + 1], numberWord[i]
                englishWords[i], englishWords[i + 1] =\
                englishWords[i + 1], englishWords[i]
                russianWords[i], russianWords[i + 1] =\
                russianWords[i + 1], russianWords[i]
                swapped = True

    # Проверка

    # print()
    # print(englishWords)
    # print(russianWords)
    # print(numberWord)
    # print()
