# Программа "English training"
# Реализованы следующие возможности:
# 1. Просмотр слов для тренировки. Вывод в виде таблицы.
#    Для этого необходимо ввести цифру "1" в главном меню
#    Если список пуст, то выводится соответствующиее сообщение
#
# 2. Добавление слова для тренировки
#    Для этого необходимо ввести цифру "2"  в главном меню, после
#    чего требуется ввести слово на иностранном языке и его перевод
#    Слова добавляются в конец списка (последняя строка таблицы)
#
# 3. Тренировка слов
#    Для этого необходимо ввести цифру "3"  в главном меню, после
#    чего требуется выбрать тип тренировки, набрав
#    соответствующую цифру и нажать Enter.
#
# 4. Выход из программы
#    Для этого необходимо набрать слово "Выход"  в главном меню, после
#    чего нажать "ОК" во всплывающем окне
#

import copy, random

print()
print('Вас приветствует программа "English Training"!')
EasyEnglishWords = ['food', 'bike', 'apple', 'do', 'mean']
EasyRussianWords = ['еда', 'велосипед', 'яблоко', 'делать', 'иметь в виду']
EasyEnglishWordsTraining = []
EasyRussianWordsTraining = []

while True:
    print('Меню\n')
    print('1. Просмотреть слова для тренировки')
    print('2. Добавить слово для тренировки')
    print('3. Начать тренировку')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')

    # Выход из программы

    if userChoice.lower() == 'выход':
        exit()

    # Вывод слов для тренировок на экран

    if (userChoice == '1'):
        print()
        if len(EasyEnglishWords) == 0:
            print('Ваш список слов пуст!\n')
        else:
            number = 1
            print('─' * 43)
            print('|  №  |      Слово      |     Перевод     |')
            print('─' * 43)
            for i in range(len(EasyEnglishWords)):
                print('|{:^5d}| {:<15} | {:<15} |'\
.format(number, EasyEnglishWords[i], EasyRussianWords[i]))
                print('─' * 43)
                number += 1

    # Добавить слова для тренировки

    if (userChoice == '2'):
        add = True
        print()
        print('Добавление слова для тренировки')
        enWord = input('Введите слово на английском языке: ')
        ruWord = input('Введите перевод слова на русском языке: ')
        print('-' * 43)
        for i in range(len(EasyEnglishWords)):
            if enWord.lower() == EasyEnglishWords[i]:
                print('\nТакое слово уже есть в Вашем списке!')
                add = False
                break
        if add == True:
            EasyEnglishWords.append(enWord.lower())
            EasyRussianWords.append(ruWord.lower())
            print('\nСлово "', enWord, '" добавлено!')
        print()

    if (userChoice == '3'):

        # Выбор типа тренировки

        while True:
            EnglishWordsTraining = copy.deepcopy(EasyEnglishWords)
            RussianWordsTraining = copy.deepcopy(EasyRussianWords)

            print()
            print('Выберите тип тренировки:')
            print('1. Слово-перевод')
            print('2. Перевод-слово')
            print('3. Правописание')
            print('4. Конструктор слов')
            print('\nДля того, чтобы вернуться в предыдущее меню, \
наберите "Назад""\n')
            userChoiceTraining = input('Выберите пункт меню: ')

            # Возврат к предыдущему меню

            if userChoiceTraining.lower() == 'назад':
                break

            # Тренировка на знание перевода (с английского на русский)

            if (userChoiceTraining == '1'):
                print()
                print('\nТренировка "Слово-перевод"\nВыберите верный \
перевод из списка\n')
                trueAmount = 0
                while True:
                    trueTranslate = random.randint(0,\
                                    len(EnglishWordsTraining) - 1)
                    if EnglishWordsTraining[trueTranslate] == 'None':
                        while EnglishWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(EnglishWordsTraining) - 1)
                    print('Выберите верный перевод: ',\
                          EnglishWordsTraining[trueTranslate])
                    for i in range(len(EasyRussianWords)):
                        print(str(i + 1), ') ', EasyRussianWords[i])
                    userAnswer = input('\nВаш ответ: ')
                    if userAnswer == str(trueTranslate + 1):
                        EnglishWordsTraining.\
                        remove(EnglishWordsTraining[trueTranslate])
                        EnglishWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(EnglishWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break

            # Тренировка на знание перевода (с русского на английский)

            if (userChoiceTraining == '2'):
                print()
                print('\nТренировка "Перевод-слово"\n\
Выберите верный перевод из списка\n')
                trueAmount = 0
                while True:
                    trueTranslate = random.randint(0,\
                                    len(RussianWordsTraining) - 1)
                    if RussianWordsTraining[trueTranslate] == 'None':
                        while RussianWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(RussianWordsTraining) - 1)
                    print('Выберите верный перевод: ',\
                          RussianWordsTraining[trueTranslate])
                    for i in range(len(EasyEnglishWords)):
                        print(str(i + 1), ') ', EasyEnglishWords[i])
                    userAnswer = input('\nВаш ответ: ')
                    if userAnswer == str(trueTranslate + 1):
                        RussianWordsTraining.\
                        remove(RussianWordsTraining[trueTranslate])
                        RussianWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(RussianWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break

            # Тренировка на правописание

            if (userChoiceTraining == '3'):
                print()
                print('\nТренировка "Правописание"\n\
Введите верный перевод из списка\n')
                trueAmount = 0
                while True:
                    trueTranslate = random.randint(0,\
                                    len(RussianWordsTraining) - 1)
                    if RussianWordsTraining[trueTranslate] == 'None':
                        while RussianWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(RussianWordsTraining) - 1)
                    print('Введите верный перевод: ',\
                          RussianWordsTraining[trueTranslate])
                    userAnswer = input('\nВаш ответ: ')
                    if userAnswer.lower() == EnglishWordsTraining[trueTranslate]:
                        RussianWordsTraining.\
                        remove(RussianWordsTraining[trueTranslate])
                        RussianWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(RussianWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break

            # Конструктор слов

            if (userChoiceTraining == '4'):
                print()
                print('\nТренировка "Конструктор слов"\n')
                trueAmount = 0
                while True:
                    word = []
                    trueTranslate = random.randint(0,\
                                    len(RussianWordsTraining) - 1)
                    if RussianWordsTraining[trueTranslate] == 'None':
                        while RussianWordsTraining[trueTranslate] == 'None':
                            trueTranslate = random.randint(0,\
                                            len(RussianWordsTraining) - 1)
                    print('Соберите перевод слова из букв: ',\
                          RussianWordsTraining[trueTranslate])
                    print()
                    for letter in EnglishWordsTraining[trueTranslate]:
                        word.append(letter)
                    random.shuffle(word)
                    if word == list(EnglishWordsTraining[trueTranslate]):
                        while word == list(EnglishWordsTraining[trueTranslate]):
                            random.shuffle(word)
                    for letter in word:
                        print(letter, end = ' ')
                    print()

                    userAnswer = input('\nВаш ответ: ')

                    if userAnswer.lower() == EnglishWordsTraining[trueTranslate]:
                        RussianWordsTraining.\
                        remove(RussianWordsTraining[trueTranslate])
                        RussianWordsTraining.insert(trueTranslate, 'None')
                        print('\nВерно!\n')
                        trueAmount += 1
                    else:
                        print('\nНеверно!\nПопробуйте ещё раз!\n')
                    if len(RussianWordsTraining) == trueAmount:
                        print('Поздравляю!\nВы изучили все слова!\n')
                        break

    HardEnglishWords = ['chainsaw', 'squirrel', 'castle',\
                        'homeland', 'sewerage', 'bottom']
    HardRussianWords = ['бензопила', 'белка', 'замок',\
                        'родина', 'канализация', 'дно']
    print()