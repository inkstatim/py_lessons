# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    new_str = ''
    for i in range(len(string_)):
        if string_[i] in vowels:
            new_str += ''
        else:
            new_str += string_[i]
    return new_str


print(disemvowel('This website is for losers LOL!'))
#
# import codewars_test as test
#
# @test.describe("Fixed Tests")
# def basic_tests():
#     @test.it("First fixed test")
#     def fixed_test_1():
#         test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
