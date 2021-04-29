# Программа "Text formatting"
# Задан текст массивом строк. Текст - фрагмент литературного произведения
# (5-7 предложений). Ни одна строка не оканчивается точкий кроме последней.
# Текст задаётся в программе, пользовательский ввод не требуется.
# Необходимо создать меню, выполняющее следующие действия:
# 1. Выравнивание текста по левому краю.
# 2. Выравнивание текста по правому краю.
# 3. Выравнивание текста по ширине.
# 4. Удаление заданного слова.
# 5. Замена одного слова другим во всем тексте.
# 6. Вычисление арифметического выражения.
# 7. Индивидуальное задание.
# 
# Варианты индивидуальных заданий:
# 
# 8. Удалить самое короткое слово в самом длинном по числу слов предложении.
#

from string import *


pointing = ['', '.', ',', '!', '?', '—']
operations = ['+', '-', '*', '/', '(', ')']

# Главная функция
def main():
    print()
    text = ['...для меня теория игр оказалась весьма полезна, -4-(5-2+1)',
    '5/7— добавил я,',
    'поневоле оправдываясь. — В самых неожиданных областях.-5 - 7',
    '— Да? Например? — Дни рождения, — ответил я и тут же пожалел об этом.',
    'Саша перестала жевать. В глазах у нее что—то блеснуло мимолетно,',
    'словно остальные ее личности навострили уши. — Продолжай,',
    '— заинтересовалась она, и я ощутил, как прислушивается вся Банда.',
    '— Ничего особенного.11 +14 - 98',
    'Просто пример. — Так расскажи. — Саша вскинула голову Сьюзен.',
    'Я пожал плечами. Не было смысла раздувать проблему.',
    '— Ну, согласно теории игр, нельзя никому говорить,',
    'когда у тебя день рождения...',
    '2 + 5 / (4 + 2) - 1 / 3 + 20']

    # Поиск самой длинной строки
    longestLenString = 0
    for string in text:
        lenString = len(string)
        if longestLenString < lenString:
            longestLenString = lenString

    [print(string) for string in text]

    while True:
        userChoice = menu()

        if userChoice == '1':
            for string in text:
                print(string.ljust(longestLenString))
        elif userChoice == '2':
            for string in text:
                print(string.rjust(longestLenString))
        elif userChoice == '3':
            for string in text:
                lenString = len(string)
                words = string.split()
                lenWords = len(words)
                if lenWords < 2 or lenString == longestLenString:
                    print(string)
                else:

                    # Вычисление необходимого количества пробелов
                    # для выравнивания по ширине
                    spaces = (longestLenString - lenString\
                              + lenWords) // lenWords

                    # Заполнение пробелами для выравнивания по ширине
                    currentLength = 0
                    for i in range(lenWords):
                        if i != lenWords - 1:
                            print(words[i] + ' ' * spaces, end = '')
                            currentLength += len(words[i]) + 1 * spaces
                        else:
                            print(words[i].rjust(longestLenString\
                                                 - currentLength))
        elif userChoice == '4':
            word = input('Введите слово, которое хотите удалить: ')
            deleteWord(word, text)
        elif userChoice == '5':
            word = input('Введите слово, которое хотите заменить: ')
            newWord = input('Введите слово, на которое хотите заменить: ')

            lenText = len(text) - 1
            for i in range(lenText):
                text[i] = text[i].replace(' ' + word, ' ' + newWord)
            print()
            [print(string) for string in text]

        elif userChoice == '6':
            mathFormulInText = False
            for string in text:
                mathFormul = ''
                isMathFormul = False

                # Удаление пробелов
                string = string.strip().replace(' ', '')

                for sym in string:
                    if sym.isdigit() or sym in operations:
                        isMathFormul = True
                        mathFormul += sym
                if isMathFormul:
                    mathFormulPolish =\
                    ' '.join(reversePolishConversion(mathFormul.strip()))
                    answer = reversePolishNotation(mathFormulPolish.split())
                    print("Значение выражения " + mathFormul
                           + " равно " + str(answer))
                    mathFormulInText = True
            if not mathFormulInText:
                print("В тексте нет математических выражений")
            print()

        elif userChoice == '7':
            maxLenWords = 0
            for string in text:
                words = string.split()
                lenWords = len(words)
                if maxLenWords < lenWords:
                    maxLenWords = lenWords
                    maxWords = words
                    maxString = string

            lenWords = []
            [lenWords.append(len(word)) for word in maxWords]
            shortestLenWord = max(lenWords)

            for word in maxWords:
                lenWord = len(word)
                if shortestLenWord > lenWord:
                    shortestLenWord = lenWord
                    shortestWord = word

            shortestWords = []
            for word in maxWords:
                if len(shortestWord) == len(word) and word not in pointing:
                    shortestWords.append(word)        

            print('Самое длинное по числу слов' +
                  'предложение/предложения: ', maxString)
            print('Самое короткое слово/слова: ', end = '')
            [print(word, end = ' ') for word in shortestWords]
            print()
            newString = ''
            for word in maxWords:
                if word not in shortestWords: 
                    newString += ''.join(' ' + word)
            text = [newString if string == maxString\
                              else string for string in text]
            print()
            [print(string) for string in text]

        # Выход из программы
        elif userChoice.lower() == 'выход':
            exit()
        else:
            print('Такого пункта нет в меню!')

# Меню программы
def menu():
    print('\nМеню')
    print('1. Выравнивание текста по левому краю')
    print('2. Выравнивание текста по правому краю')
    print('3. Выравнивание текста по ширине')
    print('4. Удаление заданного слова')
    print('5. Замена одного слова другим во всём тексте')
    print('6. Вычисление арифметического выражения')
    print('7. Удалить самое короткое слово в самом длинном '
        + 'по числу слов предложении')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()
    return userChoice

# 4. Удаление заданного слова
def deleteWord(word, text):
    deleteWord = ''
    lenText = len(text) - 1

    for i in range(lenText):
        text[i] = text[i].replace(' ' + word, deleteWord)

    print()
    [print(string) for string in text]

def reversePolishConversion(st):
    string = ''
    lenSt = len(st)
    for i in range(lenSt):
        if st[i] in operations:
            string += ' ' + st[i] + ' '
        else:
            string += st[i]

    string = string.split()
    A = []
    stack = []
    stack.append(0)
    n = ''
    for s in string:
        if s.isdigit():
            A.append(s)
        else:
            if (s == '+' or s == '-') and\
                (stack[len(stack) - 1] == '+'or\
                stack[len(stack) - 1] == '-'):
                while (s == '+' or s == '-') and\
                       (stack[len(stack) - 1] == '+' or\
                       stack[len(stack) - 1] == '-'):
                    n = stack.pop()
                    A.append(n)
                stack.append(s)
                continue
            elif (s == '*' or s == '/') and (st[len(st) - 1] == '*' or st[len(st) - 1] == '/'):
                while (s == '*' or s == '/') and (st[len(st) - 1] == '*' or st[len(st) - 1] == '/'):
                    n = st.pop()
                    A.append(n)
                st.append(s)
                continue

            if s != ')':
                st.append(s)
            else:
                n = st.pop()
                while n != '(':
                    A.append(n)
                    n = st.pop()
    while len(st) > 1:
        n = st.pop()
        A.append(n)
    return A

def reversePolishNotation(s):
    print(s)
    s = ['4', '-', '5', '2', '-', '1', '+', '-']
    A = []
    lenS = len(s)
    for i in range(lenS):
        if (s[i] != '+' and s[i] != '-' and s[i] != '*' and s[i] != '/'):
            A.append(s[i])
        else:
            try:
                a = int(A.pop())
                b = int(A.pop())
                if (s[i] == '+'):
                    A.append(b + a)
                elif (s[i] == '-'):
                    A.append(b - a)
                elif (s[i] == '*'):
                    A.append(b * a)
                elif (s[i] == '/'):
                    A.append(b / a)
            except IndexError:
                if (s[i] == '+'):
                    A.append(a)
                elif (s[i] == '-'):
                    A.append(-a)
    answer = A[0]
    return answer


if __name__ == "__main__":
    main()