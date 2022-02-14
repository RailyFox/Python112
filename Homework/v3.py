def strng(res):
    for i in res:
        print(i, end=' ')
    print()


print('Задание 1', end='\n\n')
res1 = set(input('Введите первую строку: ')) - set(input('Введите вторую строку: '))
print('Искомыми буквами являются:')
strng(res1)

print('\nЗадание 2', end='\n\n')
a = 'Привет, мир!'
c = 0
for i in a:
    if i in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
        c += 1

print('Количество гласных равно: ', c)

print('\nЗадание 3', end='\n\n')
res3 = set(input('Введите первую строку: ') + input('Введите вторую строку: '))
print('Искомыми буквами являются:')
strng(res3)

print('\nЗадание 4', end='\n\n')
res4 = set(input('Введите первую строку: ')) ^ set(input('Введите вторую строку: '))
print('Искомыми буквами являются:')
strng(res4)
