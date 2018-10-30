# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
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



