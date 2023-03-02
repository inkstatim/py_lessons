# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(s):
    alhphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = True
    for i in alhphabet:
        if i not in s.lower():
            result = False
    return result