# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    odds = []
    evens = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return odds[0] if len(odds) < len(evens) else evens[0]


import codewars_test as test

test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
