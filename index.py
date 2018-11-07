# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

import math
from collections import Iterable
import os

#
# age = 90
# if age >= 19:
#     print("adult")
# else:
#     print("teenager")
#
# a = "abc"
# b = a
# a = "xyz"
# print(b, a)
#
# print(9/3,9//3,9%3)
# print(10/3,10//3,10%3)
#
# print(ord('A'))
# print(chr(66))
#
# print('\u4e2d\u6587')
#
# print(b'abc')
#
# print('abc'.encode('ascii'))
#
# print('中午'.encode('utf-8'))
#
# # print('中午'.encode('ascii'))
#
# print(b'abc'.decode('ascii'))
#
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#
# print(len('abc'))
#
# print(len(b'abc'))
#
# print(len('中午'.encode('utf-8')))
#
# print('Age: %d, Gender: %s' % (25, 'Male'))
#
# print('%2d, %02d' % (3, 1))
#
# print('%.2f %%' % 3.14159)
#
#

# classmates = [1, 2, 3]
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[-1])
# classmates.append(4)
# classmates.insert(1, 5)
# classmates.pop()
# classmates.pop(0)
# classmates[1] = 9
# print(classmates)
#
# LIST = [True, 1, ['a', False], 'c']
# print(LIST)
# print(len(LIST))
#
# TUPLE = (1, 2)
# TUPLE1 = (1, )
# TUPLE2 = (3)
# print(TUPLE)
# print(TUPLE1)
# print(TUPLE2)

# age = 3
# if age > 18:
#     print('adult')
# elif age > 6:
#     print('teenager')
# else:
#     print('kid')
#
# names = [12, 23, 34]
# for name in names:
#     print(name)
#
# total = 0
# for x in list(range(5)):
#     total += x
# print(total)

# total = 0
# n = 99
# while n > 0:
#     n = n - 2
#     if n < 20:
#         break
#     if n % 3 == 0:
#         continue
#     total += n
# print(total)
#
# d = {'a': 95, 'b': 90}
# d['c'] = 101
# print(d)
# print('abc' in d)
# print(d.get('abc'))
# print(d.get('abc', -1))
# print(d.pop('a'))
# print(d)
#
# setList = set([12, 23, 34, 23, 34])
# setList.add(56)
# setList.add(78)
# setList.add(89)
# setList.remove(23)
# print(setList)
#
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)
# print(set([[2]]))
#
# list1 = [3, 5, 9, 6, 2, 1]
# list1.sort()
# print(list1)
#
# str1 = 'abc'
# str2 = str1.replace('a', 'A')
# print(str1, str2)
#
# t1 = (1, 2, [3, 4])
# t1[2][0] = 30
# print(t1)


def ma_abs(x):
    if x >= 0:
        return x
    if x < 0:
        return -x


print(ma_abs(-190))


def nop():
    pass


def check_params(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    if x < 0:
        return -x


print(check_params(10))
# print(check_params('a'))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(200, 200, 100, math.pi / 6)
print(r)


# def add_end(end_list=[]):
def add_end(end_list=None):
    if end_list is None:
        end_list = []
    end_list.append('END')
    return end_list


print(add_end())
print(add_end())
print(add_end())


def calc(*numbers):
    total = 0
    for n in numbers:
        total += n * n
    return total


print(calc(1, 2, 3))
print(calc(*[5, 6, 7]))
print(calc())


def person(name, age, **extra):
    if 'city' in extra:
        print('We got a city param')
    if 'job' in extra:
        print('We got a job param')
    print('name:', name, 'age:', age, 'other:', extra)


person('tom', 86, gender='M', job='Engineer')
person('Jerry', 88, **{'city': 'Beijing', 'hobby': 'basketball'})


def person(name, age, *args, city='Beijing', job):
    print(name, age, city, job)


person('tom', 88, job='Engineer')
person('Jerry', 88, job='Player', city='Tianjin')


def f1(a, b, c=88, *args, d, **kw):
    print(a, b, c, args, d, kw)


tuple_param = (1, 2, 3, 4)
dict_param = {'d': 99, 'x': 98, 'y': 96}
f1(1, 2, d=5)

f1(*tuple_param, **dict_param)


def fact1(n):
    if n == 1:
        return 1
    return n * fact1(n-1)


print(fact1(100))


def tail_recursion(n, res=1):
    if n == 1:
        return res
    return tail_recursion(n-1, n*res)


print(tail_recursion(100, 1))

sliceList = list(range(100))

print(sliceList[: 10])
print(sliceList[-10:])
print(sliceList[20: 30])
print(sliceList[-20: -10])
print(sliceList[:10:2])
print(sliceList[20:60:5])
print(sliceList[::5])
print(sliceList[:])

print((1, 2, 3, 4, 5)[2:3])
print('welcome'[3:])


def my_trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return my_trim(s[1:])
    elif s[-1] == ' ':
        return my_trim(s[: -1])
    else:
        return s


print(my_trim('  hello    '))


def iterable_print():
    d = {'a': 3, 'b': 6}
    for key in d:
        print(key)
    for value in d.values():
        print(value)
    for k, v in d.items():
        print(k, v)
    for letter in 'love':
        print(letter)
    for i, v in enumerate(['a', 'b']):
        print(i, v)


iterable_print()

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

print(list(range(1, 11)))

list_arrays = []
for x in range(11, 21):
    list_arrays.append(x * x)
print(list_arrays)

print([x * x for x in range(30, 40)])

print([x * x for x in range(50, 60) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

dist_object = {'x': 'A', 'y': 'B', 'z': 88}
print([k + '=' + v.lower() for k, v in dist_object.items() if isinstance(v, str)])

g1 = (x * x for x in range(1, 10))
for n in g1:
    print(n)


def fib(count):
    n, a, b = 0, 0, 1
    while n < count:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


print(fib(6))


def yield_fib(count):
    n, a, b = 0, 0, 1
    while n < count:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


y_f = yield_fib(8)
print(y_f)
print(next(y_f))
print(next(y_f))
print(next(y_f))
print(next(y_f))


def f101(map_x):
    return map_x * map_x


map_list = [1, 2, 3, 4]
print(list(map(f101, map_list)))
print(list(map(str, map_list)))






