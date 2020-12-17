# Программа "Database"
# Имитировать работу базы данных (БД), используя бинарный файл.
# Запись содержит 3-4 поля. Например, запись "книга" содержит поля "автор", 
# "наименование", "год издания".
#
# Необходимо сделать меню:
# 1. Создание БД.
# 2. Добавление записи в БД.
# 3. Вывод всей БД.
# 4. Поиск записей по одному полю.
# 5. Поиск записей по двум полям. 
# Для работы с текущей записью используется словарь.
#

import pickle as p
import os.path


# Проверка на существование файла

def checkFile(fn):
    check = os.path.exists(fn)
    if not check:
        print('Файла не существует!')
    else:
        return True


filename = 'Documents\Laboratory Work №11\Database.txt'
ch = 1
book = {'book': '1', 'author' : 'Tolkien',  'name': 'Lord of the ring', 'year': '1950'}

while True:
    print('\nМеню\n')
    print('1. Создание БД')
    print('2. Добавление записи в БД')
    print('3. Вывод всей БД')
    print('4. Поиск записей по одному полю')
    print('5. Поиск записей по двум полям')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()

    # Создание БД

    if userChoice == '1':
        f = open(filename, 'wb')
        print('\nБаза данных создана')
        f.close()

    # Добавление записи в БД

    elif userChoice == '2':
        f = open(filename, 'ab')
        uC = 'да'
        while uC.lower() != 'нет':
            # book['book'], book['author'], book['name'], book['year'] =\
            # input('Введите номер книги, автора, наименование, год выпуска: ').split()
            book['book'] = input('Введите номер книги: ')
            book['author'] = input('Введите автора: ')
            book['name'] = input('Введите наименование: ')
            book['year'] = input('Введите год выпуска: ')
            print()
            print('Ввести ещё одну книгу?')
            p.dump(book, f)
            while True:
                uC = input('(Да/Нет): ')
                if uC.lower() == 'да' or uC.lower() == 'нет':
                    break
        f.close()

    # Вывод всей БД

    elif userChoice == '3':
        checkFile = os.path.exists(filename)
        if not checkFile:
            print('Файла не существует!')
        else:
            f = open(filename, 'rb')
            try:
                while f != '\n':
                    book = p.load(f)
                    print(book['book'], book['author'], book['name'], book['year'])
            except EOFError:
                book = {}
            f.close()

    # Поиск записей по одному полю

    elif userChoice == '4':
        checkFile = os.path.exists(filename)
        if not checkFile:
            print('Файла не существует!')
        else:
            f = open(filename, 'rb')
            field = input('Введите поле, которое необходимо найти: ')
            print()
            find = False
            try:
                while f != '\n':
                    book = p.load(f)
                    for value in book.values():
                        if value.lower() == field.lower():
                            print(book['book'], book['author'], book['name'], book['year'])
                            find = True
                            break
            except EOFError:
                book = {}
            if not find:
                print('\nПоля не найдены')
            f.close()

    # Поиск записей по двум полям

    elif userChoice == '5':
        checkFile = os.path.exists(filename)
        if not checkFile:
            print('Файла не существует!')
        else:
            f = open(filename, 'rb')
            # field1, field2 = map(str, input('Введите два поля, которые необходимо найти: ').split())
            print('Введите два поля, которые необходимо найти')
            field1 = input('Введите первое поле: ')
            field2 = input('Введите второе поле: ')
            find = False
            try:
                while f != '\n':
                    book = p.load(f)
                    for value in book.values():
                        if value.lower() == field1.lower():
                            for value in book.values():
                                if value.lower() == field2.lower():
                                    print()
                                    print(book['book'], book['author'], book['name'], book['year'])
                                    find = True
                                    break
            except EOFError:
                book = {}
            if not find:
                print('\nПоля не найдены')
            f.close()

    # Выход из программы

    if userChoice.lower() == 'выход':
        exit()