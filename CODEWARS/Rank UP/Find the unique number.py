# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

def find_uniq(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count == 1:
            return num


# VAriant 2
# def find_uniq(arr):
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b


try:
    import codewars_test as test
except:
    pass


@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)