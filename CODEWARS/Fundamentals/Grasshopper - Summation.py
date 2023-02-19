# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

"""Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0."""


def summation(num):
    suma = 0
    for i in range(1, num + 1):
        suma += i
    return suma


