# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(func=None):
    if func:
        return func(0)
    return 0

def one(func=None):
    if func:
        return func(1)
    return 1

def two(func=None):
    if func:
        return func(2)
    return 2

def three(func=None):
    if func:
        return func(3)
    return 3

def four(func=None):
    if func:
        return func(4)
    return 4

def five(func=None):
    if func:
        return func(5)
    return 5

def six(func=None):
    if func:
        return func(6)
    return 6

def seven(func=None):
    if func:
        return func(7)
    return 7

def eight(func=None):
    if func:
        return func(8)
    return 8

def nine(func=None):
    if func:
        return func(9)
    return 9

def plus(num):
    def inner(x):
        return x + num
    return inner

def minus(num):
    def inner(x):
        return x - num
    return inner

def times(num):
    def inner(x):
        return x * num
    return inner

def divided_by(num):
    def inner(x):
        return x // num
    return inner


import codewars_test as test
test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)