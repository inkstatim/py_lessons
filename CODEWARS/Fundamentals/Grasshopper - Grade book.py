# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

def get_grade(s1, s2, s3):
    score = (s1+s2+s3)/3
    if 90 <= score <= 100:
        return 	'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


import codewars_test as test

@test.describe("Grade book")
def fixed_tests():
    @test.it('should return an A')
    def a_test_case():
        test.assert_equals(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")
        test.assert_equals(get_grade(100, 85, 96), "A", "get_grade(100, 85, 96)")
        test.assert_equals(get_grade(92, 93, 94), "A", "get_grade(92, 93, 94)")
        test.assert_equals(get_grade(100, 100, 100), "A", "get_grade(100, 100, 100)")

    @test.it("should return a B")
    def b_test_case():
        test.assert_equals(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
        test.assert_equals(get_grade(82, 85, 87), "B", "get_grade(82, 85, 87)")
        test.assert_equals(get_grade(84, 79, 85), "B", "get_grade(84, 79, 85)")

    @test.it("should return a C")
    def c_test_case():
        test.assert_equals(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")
        test.assert_equals(get_grade(75, 70, 79), "C", "get_grade(75, 70, 79)")
        test.assert_equals(get_grade(60, 82, 76), "C", "get_grade(60, 82, 76)")

    @test.it("should return a D")
    def d_test_case():
        test.assert_equals(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")
        test.assert_equals(get_grade(66, 62, 68), "D", "get_grade(66, 62, 68)")
        test.assert_equals(get_grade(58, 62, 70), "D", "get_grade(58, 62, 70)")

    @test.it("should return an F")
    def f_test_case():
        test.assert_equals(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
        test.assert_equals(get_grade(48, 55, 52), "F", "get_grade(48, 55, 52)")
        test.assert_equals(get_grade(58, 59, 60), "F", "get_grade(58, 59, 60)")
        test.assert_equals(get_grade(0, 0, 0), "F", "get_grade(0, 0, 0)")