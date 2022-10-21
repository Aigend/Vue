# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @project : py_study
# @File    : py_yield.py
# @Date    : 2022/07/06:23:27
# @Author  : jinwenlong@oppo.com
def fi(n):
    yield 1


print(type(fi))
print(dir(fi(3)))


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)


coro = simple_coroutine()
next(coro)
coro.send('this message from caller.')