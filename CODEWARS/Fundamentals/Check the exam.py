# https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):

        if arr1[i] == arr2[i]:
            score+=4
        elif arr2[i] == '':
            continue
        elif arr1[i] != arr2[i]:
            score-=1
    return score if score > 0 else 0



import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
        test.assert_equals(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]), 7)
        test.assert_equals(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
        test.assert_equals(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]), 0)
