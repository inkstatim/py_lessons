# https://www.codewars.com/kata/5782dd86202c0e43410001f6/train/python

def do_math(s):
    q = []
    for i in sorted(s, key=lambda x: x.isalpha()):
        res = ''
        for j in i:
            if j.isdigit():
                res+=j
        q.append(int(res))



import codewars_test as test
test.assert_equals(do_math("24z6 1z23 y369 89z 900b"),1414)
test.assert_equals(do_math("24z6 1x23 y369 89a 900b"),1299)
test.assert_equals(do_math("10a 90x 14b 78u 45a 7b 34y"),60)
test.assert_equals(do_math("111a 222c 444y 777u 999a 888p"),1459)
test.assert_equals(do_math("1z 2t 3q 5x 6u 8a 7b"),8)

# Your code starts here ... may the FORCE be with you