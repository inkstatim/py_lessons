# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    steps = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for direction in walk:
        steps[direction] += 1

    if steps['n'] == steps['s'] and steps['e'] == steps['w']:
        return True
    else:
        return False


import codewars_test as test

@test.describe('Walk Validator - fixed tests')
def sample_tests():
    @test.it ("should return true for a valid walk")
    def _():
        test.assert_equals(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True, 'should return True');
    @test.it ("should return false if walk is too long")
    def _():
        test.assert_equals(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False, 'should return False');
    @test.it ("should return false if walk is too short")
    def _():
        test.assert_equals(is_valid_walk(['w']), False, 'should return False');
    @test.it ("should return false if walk does not bring you back to start")
    def _():
        test.assert_equals(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), False, 'should return False');