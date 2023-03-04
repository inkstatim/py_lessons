# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
    alpha = a1+a2
    set_a = set(alpha)
    return ''.join(sorted(set_a))