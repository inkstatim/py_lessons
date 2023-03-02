# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    new_word = word.lower()
    result = ''
    for i in new_word:
        if new_word.count(i) > 1:
            result+=')'
        else:
            result+='('
    return result




print(duplicate_encode("EFAwZzGHi("))
print(duplicate_encode("recede"), "()()()")
print(duplicate_encode("Success"), ")())())", "should ignore case")
print(duplicate_encode("(( @"), "))((")
