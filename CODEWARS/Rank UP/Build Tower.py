# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        spaces = " " * (n_floors - i)
        star = "*" * (2 * i - 1)
        tower.append(spaces + star + spaces)
    return tower


print(tower_builder(6))

# import codewars_test as test
# @test.describe("Build Tower")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(tower_builder(1), ['*', ])
#         test.assert_equals(tower_builder(2), [' * ', '***'])
#         test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])
