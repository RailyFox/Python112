# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# sum = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         sum += a[i]
# print(sum)

# a = list(range(21, 41))
# print(a)
# sum = 0
# ch = 0
# for i in a:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         sum += i
# print(ch, sum)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# sum = n = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         sum += a[i]
#         n += 1
# print(sum/n)

# s = list(range(1,8))
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4]) #4
# print(s[4:1:-1])
# print(s[2:5])
# print(s[-5:-2])

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# d = []
# for i in a:
#     if i > 0:
#         d.extend([i])
# print(a)
# print(d)

# c = []
# for i in range(1,11):
#     c.extend([i**2])
# print(c)

# s = []
# n = int(input('Кол-во элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на', 3, 'без остатка.')
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# print('Введите элемент:')
# k = int(input('k = '))
# a.remove(k)
# a.sort(reverse=True)
# print(a)


# import math
# # r=int(input(':'))
# # print('-', round(2*math.pi*r,2))

# a, b = int(input('a= ')), int(input('b= '))
# print(':', math.sqrt(a**2+b**2))

# from random import randint

# a = [randint(1, 100) for i in range(20)]
# m = max(a)
# print(a)
# a.remove(m)
# a.insert(0, m)
# print('Max: ',m)
# print(a)

# a = [randint(-20, 20) for i in range(10)]
# print(a, sorted(a, reverse=True), sep='\n')

# a = [randint(10, 100) for i in range(10)]
# m = min(a)
# print(a)
# print('Min: ', m)
# print('Index min: ', a.index(m))
# del a[0:a.index(m)]
# print(a)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, '')
# print(time.strftime('Сегодня: %B %d, %Y', time.localtime()))
# print(time.strftime('Today %B %d, %Y', time.localtime()))
#
# print('test')


# def hello():
#     print('Hello')
#
#
# hello()


# def symbol(num, s1, s2):
#  ch=''
#     while ch != num:
#         if ch % 2 ==0:
#             ch+s1
#         else:
#             ch+s2
# print(ch)
#
# symbol(9, '+', '-')
# symbol(7, 'X', '0')


# def math(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# a, b = int(input('введите первое число:')), int(input('введите первое число:'))
# print(math(a, b))
#
# def fib(n):
#
#
#     a, b = 0,1
#
#     while a < n:
#         print(a, end=' ')
#
#
# fib(15)

# def chg(lst):
#     lst.sort(reverse=True)
#
#
# print(chg([1, 2, 3]))
# chg([9, 12, 33, 54, 105])
# chg(['с','л','о','н'])



