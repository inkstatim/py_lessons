# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python


def delete_nth(order,max_e):
    new_order = []
    for i in order:
        if new_order.count(i) < max_e:
            new_order.append(i)
    return new_order


import codewars_test as test
test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])