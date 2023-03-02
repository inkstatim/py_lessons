# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# Мы начинаем с предположения, что n может быть максимальным возможным значением,
# то есть мы начинаем с n = int(sqrt((2*m)**0.5)), где m - заданная сумма объемов.

def find_nb(m):
    n = int((-1 + (1 + 8*(m**(1/2)))**(1/2))/2)
    if (n*(n+1)//2)**2 == m:
        return n
    else:
        return -1

# ВАРИНАТ 2 - когда уже нашел способ 
# def find_nb(m):
#     n = 1
#     volume = 0
#     while volume < m:
#         volume += n**3
#         if volume == m:
#             return n
#         n += 1
#     return -1


import codewars_test as test
test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
