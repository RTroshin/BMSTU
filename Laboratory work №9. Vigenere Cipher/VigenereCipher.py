# Программа "Шифр Виженера"
# Написать программу, реализующую меню:
# 1. Ввод строки.
# 2. Настройка шифрующего алгоритма.
# 3. Шифрование строки. используя шифр Виженера.
# 4. Расшифрование строки.
#

# По-умолчанию
plaintext = 'PYTHON' 
key = 'SPAM'

def main():
    while True:
        userChoice = menu()
        # Добавить проверку для ключа, все ли буквы ключа являются символами алфавита
        # Функция isalpha
        # if userChoice == '1':
        #     plaintext = input("Введите строку: ")
            # plaintext = 'PYTHON'       
        # elif userChoice == '2':
            # key = input("Введите ключевое слово: ")
            # key = 'SPAM' 
        if userChoice == '3':
            print(encryptVigenere(plaintext, key))
        elif userChoice == '4':
            print(decryptVigenere(plaintext, key))

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

def encryptVigenere(plaintext, key):
    result = ''
    for letter in plaintext:
        encodedSymbol = ord('A') + (ord(letter) - ord('A') + ord(key) - ord('A') + 1) % 26
        result += chr(encodedSymbol)
    return result

# def decryptVigenere(plaintext, key):
#     result = ''
#     for letter in plaintext:
#         result += 
#     return result


if __name__ == "__main__":
    main()