import random

print('Задание 1', end='\n\n')


def slicer(tpl, elem):
    lst = list(tpl)
    if elem in lst:
        if lst.count(elem) > 1:
            return tuple(lst[lst.index(elem):lst.index(elem, lst.index(elem) + 1) + 1])
        return tuple(lst[lst.index(elem):])
    else:
        lst = []
        return tuple(lst)


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

print('\nЗадание 2', end='\n\n')


def new_tuple(x1=-1):
    if x1 > 0:
        tpl1 = ([random.randint(0, 5) for i in range(10)])
        return tuple(tpl1)
    else:
        tpl2 = ([random.randint(-5, 0) for i in range(10)])
        return tuple(tpl2)


a = new_tuple(1)
b = new_tuple()
c = a + b
print(a)
print(b)
print(tuple(c))
print('0 =', c.count(0))
