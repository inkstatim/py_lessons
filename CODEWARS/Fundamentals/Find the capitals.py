# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python

def capitals(word):
    upp = []
    for i in range(len(word)):
        if word[i].isupper():
            upp.append(i)
    return upp