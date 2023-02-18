# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
"""
The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(string):
    new_dict = {}
    for i in string:
        if i not in new_dict:
            new_dict.setdefault(i, 1)
        else:
            new_dict[i] += 1
    return new_dict



# test.assert_equals(count('aba'), {'a': 2, 'b': 1})
# test.assert_equals(count(''), {})
