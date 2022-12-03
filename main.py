import csv

e = open('data.txt', 'r').readlines()
with open("notebook.csv", mode="w+", encoding='utf-8') as w:
    file_writer = csv.writer(w, delimiter=",", lineterminator='')
    for i in e:
        file_writer.writerow(i.split(','))


def looksort():
    n = input('\n1. номеру\n2. задаче\n3. времени\n4. дате\n5. степени важности\n6. степени выполнения')
    if n == '1':
        sortnum()
    if n == '2':
        sortask()
    if n == '3':
        sortime()
    if n == '4':
        sortdate()
    if n == '5':
        sortimp()
    if n == '6':
        sortrea()


def look():
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            print(*row)


def sortnum():
    sss = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            sss.append(row)
        sss.sort(key=(lambda note: note[0]))
    for i in sss:
        print(*i)


def sortask():
    sss = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            sss.append(row)
        sss.sort(key=(lambda note: note[1]))
    for i in sss:
        print(*i)


def sortime():
    sss = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            sss.append(row)
        sss.sort(key=(lambda note: note[2]))
    for i in sss:
        print(*i)


def sortdate():
    sss = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            sss.append(row)
        sss.sort(key=(lambda note: note[3]))
    for i in sss:
        print(*i)


def sortimp():
    sss = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            sss.append(row)
        sss.sort(key=(lambda note: note[4]))
    for i in sss:
        print(*i)


def sortrea():
    sss = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            sss.append(row)
        sss.sort(key=(lambda note: note[5]))
    for i in sss:
        print(*i)


def create():
    with open("notebook.csv", mode="a", encoding='utf-8') as w:
        file_writer = csv.writer(w, delimiter=",", lineterminator='')
        file_writer.writerow(['\n'] + input(
            'Введите через запятую: номер, задачу, время, дату, степень важности, степень выполнения ').split(','))


def change():
    eee = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            eee.append(row)
    n = int(input('Введите номер строки которую нужно изменить: '))
    print(*eee[n - 1])
    eee[n - 1] = input(
        'Введите через запятую: номер, задачу, время, дату, степень важности, степень выполнения ').split(',') + ['\n']
    with open("notebook.csv", mode="w+", encoding='utf-8') as w:
        file_writer = csv.writer(w, delimiter=",", lineterminator='\n')
        for i in eee:
            file_writer.writerow(i)


def delete():
    eee = []
    with open("notebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            eee.append(row)
    n = int(input('Введите номер строки которую нужно удалить: '))
    del eee[n - 1]
    with open("notebook.csv", mode="w+", encoding='utf-8') as w:
        file_writer = csv.writer(w, delimiter=",", lineterminator='')
        for i in eee:
            file_writer.writerow(i)


print(
    'Доступные действия:\n1. Посмотреть список существующих блокнотов\n2. Создать новый блокнот\n3. Изменить существующий блокнот\n4. Удалить существующий блокнот\n5. Сортировать по:')
while 1:
    print()
    n = input('Введите номер команды: ')
    if n == '1':
        look()
    if n == '2':
        create()
    if n == '3':
        change()
    if n == '4':
        delete()
    if n == '5':
        looksort()