# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    errors = 0
    for letter in s:
        if letter not in "abcdefghijklm":
            errors += 1
    return f'{errors}/{len(s)}'