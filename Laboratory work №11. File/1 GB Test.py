# Программа для создания тестового файла размером 1 ГБ
# 

import pickle as p

filename = 'C:/Users/Engine/Desktop/Database.txt'
book = {'book': 'numberBook', 'author' : 'authorName',\
        'name': 'bookName', 'year': 'numberYear'}
try:
    with open(filename, 'wb') as wf:
        for n in range(50000):
            book['book'] = n + 1
            book['author'] = 'Толкин'
            book['name'] = 'Властелин колец. Братство кольца'
            book['year'] = '1963'
            p.dump(book, wf)
except OSError:
    print('Недостаточно места для записи!')