# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
    words = x.split()
    highest_word = ''
    highest_score = 0
    for word in words:
        score = sum(ord(c) - 96 for c in word)
        if score > highest_score:
            highest_word = word
            highest_score = score
        elif score == highest_score:
            if words.index(word) < words.index(highest_word):
                highest_word = word

    return highest_word

#
# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")



