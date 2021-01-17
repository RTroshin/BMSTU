# Программа "Шифр Цезаря"
#

def main():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    # message = input('Введите строку: ').lower()
    # key = int(input('Введите ключ: '))
    message = 'чу, я слышу пушек гром'
    key = 3

    print('Зашифрованное сообщение:', encryptCaesar(alphabet, message, key))

    result = encryptCaesar(alphabet, message, key)

    print('Расшифрованное сообщение:', decryptCaesar(alphabet, result, key))

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