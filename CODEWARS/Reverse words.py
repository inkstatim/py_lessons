#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

def reverse_words(text):
    words = []
    for i in text.split(' '):
        words.append(i[::-1])
    return ' '.join(words)


print(reverse_words('double  spaced  words'))
