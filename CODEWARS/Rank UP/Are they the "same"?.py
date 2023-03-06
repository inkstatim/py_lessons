# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    array1.sort()
    array2.sort()
    test = 0
    l = [len(array1),len(array2)]
    for i in range(min(l)):
        if array1[i] ** 2 == array2[i] or array2[i] ** 2 == array1[i]:
            continue
        else:
            test += 1
    return test <= 0

# Но в решениях понравилось
# def comp(array1, array2):
#     try:
#         return sorted([i ** 2 for i in array1]) == sorted(array2)
#     except:
#         return False


import codewars_test as test


@test.describe("Same")
def tests():
    @test.it("Fixed tests")
    def basics():
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        test.assert_equals(comp(a1, a2), True)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        test.assert_equals(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        test.assert_equals(comp(a1, a2), False)
