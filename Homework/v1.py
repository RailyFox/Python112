import math

print('\t\tЗадание 1')


def rectang(a, b):
    s = a * b
    return s


def triang(a, h):
    s = 1 / 2 * a * h
    return s


def circle(r):
    s = round(math.pi, 2) * r ** 2
    return s


print('Площадь какой фигуры вы хотели бы найти?')
ch = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг: '))
match ch:
    case 1:
        a, b = int(input('Введите длину: ')), int(input('Введите ширину: '))
        print(rectang(a, b))
    case 2:
        a, h = int(input('Введите основание: ')), int(input('Введите высоту: '))
        print(triang(a, h))
    case 3:
        r = int(input('радиус круга: '))
        print(circle(r))

print('\t\tЗадание 2')


def first_func(x):
    prime_num = []
    num = []
    for j in x:
        k = 0
        for i in range(2, j // 2 + 1):
            if (j % i == 0):
                k += 1
        if (k <= 0 and j != 1):
            prime_num.append(j)
        else:
            num.append(j)
    print('Min: ', min(prime_num), '\nMax: ', max(num))


lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]

first_func(lst)
