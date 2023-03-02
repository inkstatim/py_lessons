# https://www.codewars.com/kata/558fc85d8fd1938afb000014/python

def sum_two_smallest_numbers(numbers):
    min_first = min(numbers)
    numbers.remove(min_first)
    min_second = min(numbers)
    return min_first+min_second

# АГА , можно было сделать
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])


import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)


