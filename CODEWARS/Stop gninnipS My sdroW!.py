# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    new_sentence = []
    for word in sentence.split():
        if len(word) >= 5:
            new_sentence.append(word[::-1])
        else:
            new_sentence.append(word)
    return ' '.join(new_sentence)
