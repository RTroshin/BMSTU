# Программа "Vigenere cipher"
# Написать программу, реализующую меню:
# 1. Ввод строки.
# 2. Настройка шифрующего алгоритма.
# 3. Шифрование строки. используя шифр Виженера.
# 4. Расшифрование строки.
#

#TO DO Вставить букву ё

# Главная функция
def main():

    # Настройки по-умолчанию
    plaintext = 'how can i get to the library?'
    # plaintext = 'swx tae g rmu ko kfp tjsrrpj?'
    key = 'library'
    latinAlphabet = True
    cyrillicAlphabet = False

    while True:
        userChoice = menu()
        if userChoice == '1':
            plaintext = input("Введите строку: ").lower()      
        elif userChoice == '2':
            while True:
                check = True
                key = input("Введите ключевое слово: ").lower()
                for k in key:
                    if not k.isalpha():
                        check = False
                if not check:
                    print('Ключевое слово должно ' +\
                          'состоять из букв алфавита!')
                else:
                    break

        elif userChoice == '3':
            print('Результат: ', encryptVigenere(plaintext, key, latinAlphabet, cyrillicAlphabet))
        elif userChoice == '4':
            print('Результат: ', decryptVigenere(plaintext, key, latinAlphabet, cyrillicAlphabet))
        elif userChoice == '5':
            while True:
                alphabetChoice = input('Выберите используемый алфавит'
                                     + '\n1. Латиница\n2. Кириллица\nВыбор: ')
                if alphabetChoice == '1':
                    latinAlphabet = True
                    cyrillicAlphabet = False
                    break
                elif alphabetChoice == '2':
                    cyrillicAlphabet = True
                    latinAlphabet = False
                    break
                else:
                    print('Такого пункта нет в меню!')            

        # Выход из программы
        elif userChoice.lower() == 'выход':
            exit()
        else:
            print('Такого пункта нет в меню!')

# Меню программы
def menu():
    print()
    print('1. Ввод строки')
    print('2. Настройка шифрующего алгоритма')
    print('3. Шифрование строки, используя шифр Виженера')
    print('4. Расшифровывание строки')
    print('5. Настройка используемоего алфавита')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()
    return userChoice

# 3. Шифрование строки, используя шифр Виженера
def encryptVigenere(plaintext, key, latinAlphabet, cyrillicAlphabet):
    result = ''
    i = 0
    lenKey = len(key) - 1
    for letter in plaintext:
        if letter.isalpha():
            if latinAlphabet:
                result += chr(ord('a') + (ord(letter) - ord('a')\
                        + ord(key[i]) - ord('a')) % 26)
            elif cyrillicAlphabet:
                result += chr(ord('а') + (ord(letter) - ord('а')\
                        + ord(key[i]) - ord('а')) % 33)
            i = 0 if i == lenKey else i + 1
        else:
            result += letter
    return result

# 4. Расшифровывание строки
def decryptVigenere(plaintext, key, latinAlphabet, cyrillicAlphabet):
    result = ''
    i = 0
    lenKey = len(key) - 1
    for letter in plaintext:
        if letter.isalpha():
            if latinAlphabet:
                result += chr(ord('а') + ((ord(letter) - ord('а')) + 26\
                        - (ord(key[i]) - ord('а'))) % 26)
            elif cyrillicAlphabet:
                result += chr(ord('а') + ((ord(letter) - ord('а')) + 33\
                        - (ord(key[i]) - ord('а'))) % 33)
            i = 0 if i == lenKey else i + 1
        else:
            result += letter
    return result


if __name__ == "__main__":
    main()