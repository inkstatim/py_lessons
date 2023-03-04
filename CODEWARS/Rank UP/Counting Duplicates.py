# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    n = {}
    c = 0
    if len(text) == 0:
        return c
    else:
        for i in text.lower():
            n[i] = n.get(i, 0) + 1
        for key, value in n.items():
            if value > 1:
                c += 1
        return c