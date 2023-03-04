# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def productFib(prod):
    a, b = 0, 1

    while a * b < prod:
        a, b = b, a + b
    fib = (a, b, a * b == prod)
    return list(fib)


import codewars_test as test
test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])
