#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test fun module'

__author__ = 'Michael Liao'


import math
import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型不对')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


def person1(name, age, city, job):
    print(name, age, city, job)


def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # a, b = b, a + b
        t = (b, a + b)
        a = t[0]
        b = t[1]
        n = n + 1
    return 'done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


def add(x, y, f):
    return f(x) + f(y)



def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    def fn(x, y):
        if  not isinstance(x, str):
            raise  TypeError('数据格式错误，只能输入数字')
        return x * 10 + y

    return reduce(fn, map(char2num, s))


def cap(L):
    # print(args)
    def fn(x):
        if  not  isinstance(x,str):
            raise TypeError('只能输入字符')
        return x.capitalize();
    return list(map(fn,L));

def prod(L):
    def squre(x,y):
        return x*y
    return (reduce(squre,L))


def str2float(s):
    def fix(x,y):
        return x*10+y
    def str2num(n):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[n]
    [a,b]=s.split('.')

    integer = reduce(fix,map(str2num,a))
    decimals = reduce(fix,map(str2num,b))/( 10**len(b))
    return integer + decimals

def is_odd(n):
    return n % 2 == 1

@log
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


