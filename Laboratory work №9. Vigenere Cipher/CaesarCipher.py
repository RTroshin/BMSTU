# Программа "Caesar cipher"
#

def main():
    cyrillicAlphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # LatinAlphabetLat = 'abcdifghijklmnopqrstuvwxyz'
    # message = input('Введите строку: ').lower()
    # key = int(input('Введите ключ: '))
    message = 'чу, я слышу пушек гром'
    key = 3

    print('Зашифрованное сообщение:', encryptCaesar(cyrillicAlphabet, message, key))
    result = encryptCaesar(cyrillicAlphabet, message, key)
    print('Расшифрованное сообщение:', decryptCaesar(cyrillicAlphabet, result, key))

def encryptCaesar(alphabet, message, key):
    encrypted = ''
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            newKey = (t + key) % len(alphabet)
            encrypted += alphabet[newKey]
        else:
            encrypted += letter
    return encrypted

def decryptCaesar(alphabet, message, key):
    decrypted = ''
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            newKey = (t - key) % len(alphabet)
            decrypted += alphabet[newKey]
        else:
            decrypted += letter
    return decrypted


if __name__ == "__main__":
    main()