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
            '— Ничего особенного.',
            'Просто пример. — Так расскажи. — Саша вскинула голову Сьюзен.',
            'Я пожал плечами. Не было смысла раздувать проблему.',
            '— Ну, согласно теории игр, нельзя никому говорить,',
            'когда у тебя день рождения...',
            '2+5/(4+2)-1/3+20/10+4']
            # '2 + 5 % (4 + 2) - 1 // 3 + 20 // 10 + 4']

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
                    # Вычисление необходимого количества пробелов для выравнивания по ширине
                    spaces = (longestLenString - lenString + lenWords) // lenWords

                    # Заполнение пробелами для выравнивания по ширине
                    currentLength = 0
                    for i in range(lenWords):
                        if i != lenWords - 1:
                            print(words[i] + ' ' * spaces, end = '')
                            currentLength += len(words[i]) + 1 * spaces
                        else:
                            print(words[i].rjust(longestLenString - currentLength))

        elif userChoice == '4':
            word = input('Введите слово, которое хотите удалить: ')
            deleteWord = ''
            
            lenText = len(text) - 1
            for i in range(lenText):
                text[i] = text[i].replace(' ' + word, deleteWord)
            [print(string) for string in text]

        elif userChoice == '5':
            word = input('Введите слово, которое хотите заменить: ')
            newWord = input('Введите слово, на которое хотите заменить: ')

            lenText = len(text) - 1
            for i in range(lenText):
                text[i] = text[i].replace(word, newWord)
            [print(string) for string in text]

        # elif userChoice == '6':
        #     mathFormulInText = False
        #     lenText = len(text)
        #     for i in range(lenText):
        #         mathFormul = ''
        #         isMathFormul = False
        #         for j in operations:
        #             if j in text[i]:
        #                 lenText_i = len(text[i])
        #                 for k in range(lenText_i):
        #                     if text[i][k] in number or text[i][k] in operations:
        #                         try:
        #                             if text[i][k + 1] != ' ' and text[i][k+1].lower() not in abcEng and text[i][k+1].lower() not in abcRus and text[i][k+1].lower() not in pointing:
        #                                 isMathFormul = True
        #                                 mathFormul += text[i][k]
        #                         except IndexError:
        #                             mathFormul += text[i][k]
        #                 break

        elif userChoice == '6':
            mathFormulInText = False
            for string in text:
                mathFormul = ''
                isMathFormul = False

                # Удаление пробелов
                string = string.strip().replace(' ', '')

        elif userChoice == '7':
            maxLenWords = 0
            for string in text:
                words = string.split()
                lenWords = len(words)
                if maxLenWords < lenWords:
                    maxLenWords = lenWords
                    maxWords = words
                    maxString = string

            # shortestLenWord = 0
            # for word in maxWords:
            #     lenWord = len(word)
            #     if shortestLenWord < lenWord:
            #         shortestLenWord = lenWord
            # print(shortestLenWord)

            # lenWords = []
            # for word in maxWords:
            #     lenWords.append(len(word))
            # shortestLenWord = max(lenWords)

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

            print('Самое длинное по числу слов предложение: ', maxString)
            print('Самое короткое слово: ', end = '')
            [print(word, end = ' ') for word in shortestWords]
            print()
            newString = ''
            for word in maxWords:
                if word not in shortestWords: 
                    newString += ''.join(' ' + word)
            text = [newString if string == maxString else string for string in text]
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
    print('7. Удалить самое короткое слово в самом длинном по числу слов предложении')
    print('\nДля выхода из программы наберите "Выход"\n')
    userChoice = input('Выберите пункт меню: ')
    print()
    return userChoice

def reversePolishConversion(st):
    string = ''
    lenSt = len(st)
    for i in range(lenSt):
        if st[i] in operations:
            string += ' ' + st[i] + ' '
        else:
            string += st[i]

    s = string.split()
    A = []
    st = []
    st.append(0)
    n = ''
    lenS = len(s)
    for i in range(lenS):
        if (s[i] != '+' and s[i] != '-' and s[i] != '*' and s[i] != '/' and s[i] != '(' and s[i] != ')'):
            A.append(s[i])
        else:
            if (s[i] == '+' or s[i] == '-') and (st[len(st) - 1] == '*' or st[len(st) - 1] == '/'):
                while (s[i] == '+' or s[i] == '-') and (st[len(st) - 1] == '*' or st[len(st) - 1] == '/'):
                    n = st.pop()
                    A.append(n)
                st.append(s[i])
                continue
            elif (s[i] == '*' or s[i] == '/') and (st[len(st) - 1] == '*' or st[len(st) - 1] == '/'):
                while (s[i] == '*' or s[i] == '/') and (st[len(st) - 1] == '*' or st[len(st) - 1] == '/'):
                    n = st.pop()
                    A.append(n)
                st.append(s[i])
                continue

            if s[i] != ')':
                st.append(s[i])
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
    A = []
    lenS = len(s)
    for i in range(lenS):
        if (s[i] != '+' and s[i] != '-' and s[i] != '*' and s[i] != '/'):
            A.append(s[i])
        else:
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
    answer = A[0]
    return answer


if __name__ == "__main__":
    main()