# Программа для создания текстового файла
#

import pickle as p
import random as r

filename = 'my_data.txt'

try:
    with open(filename, 'w') as writeFile:
        for n in range(10000):
            number = r.randint(-100, 100)
            print(number, end=' ', file=writeFile)
except OSError:
    print('Недостаточно места для записи!')