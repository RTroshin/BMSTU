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

# Исключения
# 1. AttributeError
# 2. EOFError
# 3. ImportError
# 4. IndexError
# 5. pickle.UnpicklingError
# 6. pickle.PicklingError
# 7. pickle.PickleError
# 8. OSError: [Errno 28] No space left on device

import pickle as p
import os.path


# Главная функция
def main():
    filename = 'C:/Users/Engine/Desktop/Database.txt'
    book = {'book': 'numberBook', 'author' : 'authorName',\
            'name': 'bookName', 'year': 'numberYear'}
    while True:
        userChoice = menu()
        if userChoice == '1':
            createDatabase(filename)
        elif userChoice == '2':
            addBook(filename, book)
        elif userChoice == '3':
            printDatabase(filename, book)
        elif userChoice == '4':
            searchOneField(filename, book)       
        elif userChoice == '5':
            searchTwoFields(filename, book)

        # Выход из программы
        if userChoice.lower() == 'выход':
            exit()

# Меню программы
def menu():
    print('\nМеню')
    print('1. Создание БД')
    print('2. Добавление записи в БД')
    print('3. Вывод всей БД')
    print('4. Поиск записей по одному полю')
    print('5. Поиск записей по двум полям')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()
    return userChoice

# Создание БД
def createDatabase(filename):
    # Добавить исключение!
    f = open(filename, 'wb')
    print('\nБаза данных создана')
    f.close()

# Добавление записи в БД
def addBook(filename, book):
    # Добавить исключение!
    f = open(filename, 'ab')
    uC = 'да'
    while uC.lower() != 'нет':
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
def printDatabase(filename, book):
    if checkFile(filename):
        # Добавить исключение!
        with open(filename, 'rb') as f:
            book = p.load(f)
            print('┌', '─' * 4, '┬', '─' * 21, '┬',\
                '─' * 41, '┬', '─' * 6, '┐', sep = '')
            print('│ {:^3}│ {:^20}│ {:^40}│ {:^5}│'\
                .format('№', 'Автор', 'Название книги', 'Год'))
            print('├', '─' * 4, '┼', '─' * 21,\
                    '┼', '─' * 41, '┼', '─' * 6, '┤', sep = '')
            print('│ {:^3}│ {:20}│ {:40}│ {:5}│'\
            .format(book['book'], book['author'],\
                    book['name'], book['year']))
            print('└', '─' * 4, '┴', '─' * 21, '┴',\
                '─' * 41, '┴', '─' * 6, '┘', sep = '')

# Поиск записей по одному полю
def searchOneField(filename, book):
    if checkFile(filename):
        # Добавить исключение!
        with open(filename, 'rb') as f:
            book = p.load(f)
            field = input('Введите поле, которое необходимо найти: ')
            print()
            search = False
            print('┌', '─' * 4, '┬', '─' * 21, '┬',\
                '─' * 41, '┬', '─' * 6, '┐', sep = '')
            print('│ {:^3}│ {:^20}│ {:^40}│ {:^5}│'\
                .format('№', 'Автор', 'Название книги', 'Год'))
            for value in book.values():
                if value.lower() == field.lower():
                    print('├', '─' * 4, '┼', '─' * 21,\
                            '┼', '─' * 41, '┼', '─' * 6, '┤', sep = '')
                    print('│ {:^3}│ {:20}│ {:40}│ {:5}│'\
                    .format(book['book'], book['author'],\
                            book['name'], book['year']))
                    search = True
                    break
            if not search:
                print('\nПоля не найдены')
            print('└', '─' * 4, '┴', '─' * 21,\
                '┴', '─' * 41, '┴', '─' * 6, '┘', sep = '')

# Поиск записей по двум полям
def searchTwoFields(filename, book):
    if checkFile(filename):
        # Добавить исключение!
        with open(filename, 'rb') as f:
            book = p.load(f)
            print('Введите два поля, которые необходимо найти')
            field1 = input('Введите первое поле: ')
            field2 = input('Введите второе поле: ')
            search = False
            print('┌', '─' * 4, '┬', '─' * 21, '┬',\
                '─' * 41, '┬', '─' * 6, '┐', sep = '')
            print('│ {:^3}│ {:^20}│ {:^40}│ {:^5}│'\
                .format('№', 'Автор', 'Название книги', 'Год'))
            for value in book.values():
                if value.lower() == field1.lower():
                    for value in book.values():
                        if value.lower() == field2.lower():
                            print('├', '─' * 4, '┼', '─' * 21,\
                                    '┼', '─' * 41, '┼', '─' * 6, '┤', sep = '')
                            print('│ {:^3}│ {:20}│ {:40}│ {:5}│'\
                            .format(book['book'], book['author'],\
                                    book['name'], book['year']))
                            search = True
                            break
            if not search:
                print('\nПоля не найдены')
            print('└', '─' * 4, '┴', '─' * 21,\
                '┴', '─' * 41, '┴', '─' * 6, '┘', sep = '')

# Проверка на существование файла
def checkFile(filename):
    check = os.path.exists(filename)
    if not check:
        print('Файла не существует!')
    else:
        return True


if __name__ == "__main__":
    main()