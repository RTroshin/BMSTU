# Программа "Text formatting"
# 

from math import e, pi, sqrt


# Главная функция
def main():
    while True:
        userChoice = menu()

# Меню программы
def menu():
    print('\nМеню')
    print('1. Выравнивание по левому краю')
    print('2. Выравнивание по правому краю')
    print('3. Выравнивание по ширине')
    print('4. Удаление заданного слова')
    print('5. Замена заданного слова')
    print('6. Вычисление арифметического выражения')
    print('7. Найти предложение, в котором максимальное количество слов, '
        + 'в которых каждая буква входит не менее двух раз')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()
    return userChoice


if __name__ == "__main__":
    main()