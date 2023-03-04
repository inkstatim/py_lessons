# https://www.codewars.com/kata/58cbfe2516341cce1e000001/train/python

def count_zeros_n_double_fact(n):
    prod = 1
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            prod *= i
    else:
        for i in range(1, n+1, 2):
            prod *= i
    return len(str(prod)) - len(str(prod).rstrip('0'))



import codewars_test as test


@test.describe("Basic tests")
def test_group():
    @test.it("Please pass examples in kata description")
    def test_case():
        test.assert_equals(count_zeros_n_double_fact(8), 0)
        test.assert_equals(count_zeros_n_double_fact(30), 3)
