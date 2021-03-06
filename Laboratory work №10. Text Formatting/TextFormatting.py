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

from math import e, pi

variables = {"e": e, "pi": pi}

# Главная функция
def main():
    longestLenString = 0
    text = ['...для меня теория игр оказалась весьма полезна, 5-2+1',
            '— добавил я,',
            'поневоле оправдываясь. — В самых неожиданных областях.',
            '— Да? Например? — Дни рождения, — ответил я и тут же пожалел об этом.',
            'Саша перестала жевать. В глазах у нее что-то блеснуло мимолетно,',
            'словно остальные ее личности навострили уши. — Продолжай,',
            '— заинтересовалась она, и я ощутил, как прислушивается вся Банда.',
            '— Ничего особенного.',
            'Просто пример. — Так расскажи. — Саша вскинула голову Сьюзен.',
            'Я пожал плечами. Не было смысла раздувать проблему.',
            '— Ну, согласно теории игр, нельзя никому говорить,',
            'когда у тебя день рождения...']

    # Поиск самой длинной строки
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
                text[i] = text[i].replace(word +  ' ', deleteWord)
            [print(string) for string in text]

        elif userChoice == '5':
            word = input('Введите слово, которое хотите заменить: ')
            newWord = input('Введите слово, на которое хотите заменить: ')

            lenText = len(text) - 1
            for i in range(lenText):
                text[i] = text[i].replace(word, newWord)
            [print(string) for string in text]

        elif userChoice == '6':
            incorrect_expressions = []
            _text = []
            for line in text:
                line = line.replace("= ", "=").replace(" =", "=")
                eq_index = line.find("=")
                while eq_index != -1:
                    if eq_index == 0:
                        continue
                    elif eq_index == len(line) - 1:
                        break
                    try:
                        to_left = line[:eq_index].strip().split()
                        to_right = line[eq_index + 1:].strip().split()
                        if not to_left or not to_right:
                            left_hand_side = ""
                            right_hand_side = ""
                        else:
                            left_hand_side = to_left[-1]
                            right_hand_side = to_right[0]
                        declaration = [left_hand_side, right_hand_side]
                        declaration_s = "{}={}".format(*declaration)
                        line = line.replace(
                            declaration_s, "")
                        variables[declaration[0]] = float(declaration[1])
                        if variables[declaration[0]].is_integer():
                            variables[declaration[0]] = int(declaration[1])
                    except ValueError:
                        incorrect_expressions.append(declaration_s)
                    eq_index = line.find("=")
                _text.append(line)

            for line in _text:
                expressions = []
                expr_started = False
                expr = ""
                prev_sym = None
                for v in variables:
                    line = line.replace(v, str(variables[v]))
                for sym in line:
                    if sym.isdigit() or \
                            sym in ["*", "+", "-", "/", "(", "%", "√"] or \
                            expr_started and sym in [" ", ".", ")"] and \
                            prev_sym not in [" ", "."]:
                        if expr_started:
                            expr += sym
                        else:
                            expr = sym
                            expr_started = True
                    elif expr_started:
                        expressions.append(expr.strip())
                        expr_started = False
                    prev_sym = sym
                if expr_started:
                    expressions.append(expr.strip())

                for expr in expressions:
                    try:
                        line = line.replace(expr, exec_expr(expr))
                    except (
                        OverflowError, ZeroDivisionError, ValueError, IndexError
                    ):
                        incorrect_expressions.append(expr)
                print(line)
            if incorrect_expressions:
                import sys

                print("\033[91mНайдены некорректные выражения:",
                    *incorrect_expressions,
                    sep="\n", file=sys.stderr)
                print('\033[0m')

        elif userChoice == '7':
            maxLenWords = 0
            # maxWords = 
            for string in text:
                words = string.split()
                lenWords = len(words)
                if maxLenWords < lenWords:
                    maxLenWords = lenWords
                    maxWords = words
                    maxString = string

            shortestWord = maxWords[0]
            shortestLenWord = len(shortestWord)
            for word in maxWords:
                lenWord = len(word)
                if shortestLenWord > lenWord:
                    shortestLenWord = lenWord
                    shortestWord = word
            
            print('Самое длинное по числу слов предложение: ', maxString)
            print('Самое короткое слово: ', shortestWord)
            print()

            deleteWord = ''
            text = [string.replace(shortestWord + ' ', deleteWord) if string == maxString else string for string in text]
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


def is_number(string):
    """
    Является ли строка int или float?
    :param string: Строка, которую надо проверить
    :return: True/False, в зависимости от того, пройдена ли проверка
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def exec_op(op_type, first_arg, second_arg=""):
    """
    Вычисление значения операции.
    :param op_type: Тип операции, строка как в исходном выражении.
    Поддерживаются: + - * % // /
    :param first_arg: Первый аргумент
    :param second_arg: Второй аргумент (необязателен, например, в корне)
    :return: Вычисленное значение в виде int или float
    """

    if op_type == "/":
        return float(first_arg) / float(second_arg)
    use_float = False
    if "." in first_arg or "." in second_arg:
        use_float = True
    if op_type == "+":
        if use_float:
            return float(first_arg) + float(second_arg)
        return int(first_arg) + int(second_arg)
    if op_type == "-":
        if use_float:
            return float(first_arg) - float(second_arg)
        return int(first_arg) - int(second_arg)
    if op_type == "//":
        if use_float:
            return float(first_arg) // float(second_arg)
        return int(first_arg) // int(second_arg)
    if op_type == "%":
        if use_float:
            return float(first_arg) % float(second_arg)
        return int(first_arg) % int(second_arg)
    if use_float:
        return float(first_arg) * float(second_arg)
    return int(first_arg) * int(second_arg)


def exec_expr(expression, stage=0):
    """
    Вычисление арифметического выражения
    :param expression: Выражение, значение которого требуется вычислить
    :param stage: Этап вычислений
    :return: Вычисленное значение в виде строки
    """

    if not expression:
        raise ValueError(expression)

    # Удаление пробелов. Замена двойных минусов
    expression = expression.strip().replace(' ', '').replace('--', '+')

    # Вычисление выражений в скобках
    if expression.find("(") != -1:
        bracket_expr = []
        level = 0
        left_round_bracket = -1
        right_round_bracket = -1
        expr_len = len(expression)
        for index in range(expr_len):
            sym = expression[index]
            if sym == "(":
                level += 1
                if level == 1:
                    left_round_bracket = index
            elif sym == ")":
                if level == 1:
                    right_round_bracket = index
                if -1 < left_round_bracket < right_round_bracket < expr_len:
                    bracket_expr.append(expression[left_round_bracket + 1: right_round_bracket])
                level -= 1

        if level != 0:
            raise ValueError(expression)

        for b_expr in bracket_expr:
            expression = expression.replace("(" + b_expr + ")", exec_expr(b_expr))
        return expression if is_number(expression) else exec_expr(expression)

    # Этап 2.5. Некорректное выражение: открывающей нет, а закрывающая есть!
    elif expression.find(")") != -1:
        raise ValueError(expression)

    # "Расчленяем" выражение на слагаемые, считаем их отдельно, затем складываем
    elif stage == 0 and (expression.find("+") != -1 or expression.find("-", 1) != -1):
        parts = []
        first_part_sym = 0
        last_sym = "+"
        for index in range(len(expression)):
            if expression[index] in ["+", "-"] and (index == 0 or expression[index - 1].isdigit()):
                if expression[first_part_sym:index]:
                    parts.append([last_sym, expression[first_part_sym:index]])
                    first_part_sym = index + 1
                    last_sym = expression[index]
        parts.append([last_sym, expression[first_part_sym:]])
        result = "0"
        for part in parts:
            result = str(exec_op(part[0], result, part[1] if is_number(part[1]) else exec_expr(part[1], stage = 1)))
        return result

    # Этап 4. "Расчленяем" слагаемые на множители, считаем их отдельно, затем умножаем
    elif expression.count("*") % 2 or expression.find("/") != -1 or expression.find("%") != -1:
        parts = []
        first_part_sym = 0
        last_sym = "*"
        expression = expression.replace("**", "POW")
        for index in range(len(expression)):
            if expression[index] == "%":
                parts.append([last_sym, expression[first_part_sym:index]])
                first_part_sym = index + 1
                last_sym = expression[index]
            elif expression[index] == "*":
                if expression[first_part_sym:index]:
                    parts.append([last_sym, expression[first_part_sym:index]])
                    first_part_sym = index + 1
                    last_sym = expression[index]
            elif expression[index] == "/":
                if expression[index - 1] != expression[index] and expression[index + 1] != expression[index]:
                    parts.append([last_sym, expression[first_part_sym:index]])
                    first_part_sym = index + 1
                    last_sym = expression[index]
                else:
                    if expression[index - 1] == expression[index]:
                        parts.append([last_sym, expression[first_part_sym:index - 1]])
                        first_part_sym = index + 1
                        last_sym = "//"
        parts.append([last_sym, expression[first_part_sym:]])
        result = "1"
        for part in parts:
            result = str(exec_op(part[0], result, part[1] if is_number(part[1]) else exec_expr(part[1].replace("POW", "**"))))
        return result

    # Этап 5. Считаем степени. Поведение как в Python, 2 ** 5 ** 3 = 2 ** 125
    elif expression.find("**") != -1:
        parts = expression.split("**")[::-1]
        result = parts[0]
        for i in range(1, len(parts)):
            result = str(
                exec_op("**", parts[i] if is_number(parts[i]) else exec_expr(parts[i]), result if is_number(result) else exec_expr(result)))
        return result

    # Этап 6. Считаем корни
    elif not is_number(expression):
        expression = expression.replace("+", "")
        if not is_number(expression):
            return str(exec_op("√", exec_expr(expression[1:])))

    return expression


if __name__ == "__main__":
    main()