# Программа "Caesar cipher"
#

def main():
    cyrillicAlphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latinAlphabetLat = 'abcdifghijklmnopqrstuvwxyz'

    while True:
        print('Введите Ш чтобы зашифровать сообщение, Р чтобы расшифровать и В чтобы выйти')
        menu = input('>>> ').lower()
        if menu == 'в':
            break
        elif not (menu == 'ш' or menu == 'р'):
            continue
        output = ''
        # message = input('Введите строку: ').lower()
        # key = int(input('Введите ключ: '))
        # message = 'чу, я слышу пушек гром'
        message = 'ъц, в фоюыц тцызн ёусп'
        key = 3
        if menu == 'р':
            key *= -1
        for letter in message:
            if letter in cyrillicAlphabet:
                t = cyrillicAlphabet.find(letter)
                newKey = (t + key) % len(cyrillicAlphabet)
                output += cyrillicAlphabet[newKey]
            # if letter in latinAlphabetLat:
            #     t = latinAlphabetLat.find(letter)
            #     newKey = (t + key) % len(latinAlphabetLat)
            #     output += latinAlphabetLat[newKey]
            else:
                output += letter
        print('Результат: ' + output)

    # print('Зашифрованное сообщение:', encryptCaesar(alphabet, message, key))
    # result = encryptCaesar(alphabet, message, key)
    # print('Расшифрованное сообщение:', decryptCaesar(alphabet, result, key))

# def encryptCaesar(alphabet, message, key):
#     encrypted = ''
#     for letter in message:
#         if letter in alphabet:
#             t = alphabet.find(letter)
#             newKey = (t + key) % len(alphabet)
#             encrypted += alphabet[newKey]
#         else:
#             encrypted += letter
#     return encrypted

# def decryptCaesar(alphabet, message, key):
#     decrypted = ''
#     for letter in message:
#         if letter in alphabet:
#             t = alphabet.find(letter)
#             newKey = (t - key) % len(alphabet)
#             decrypted += alphabet[newKey]
#         else:
#             decrypted += letter
#     return decrypted


if __name__ == "__main__":
    main()