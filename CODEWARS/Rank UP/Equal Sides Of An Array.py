# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    n = len(arr)
    for i in range(n):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1






import codewars_test as test
test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
test.assert_equals(find_even_index(list(range(1,100))),-1)
test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
test.assert_equals(find_even_index(list(range(-100,-1))),-1)
