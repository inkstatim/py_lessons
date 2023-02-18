# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    names = name.upper().split()
    return f'{names[0][0]}.{names[1][0]}'
