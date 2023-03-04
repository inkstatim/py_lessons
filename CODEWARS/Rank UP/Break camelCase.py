# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
import re
def solution(s):
    words = re.sub(r"(\w)([A-Z])", r"\1 \2", s)

    return words


import codewars_test as test
test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")