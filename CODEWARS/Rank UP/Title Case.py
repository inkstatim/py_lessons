# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

def title_case(title, minor_words=''):
    title = title.title().split()
    minor_words = minor_words.lower().split()
    for i in range(1,len(title)):
        if title[i].lower() in minor_words:
            title[i] = title[i].lower()
    return ' '.join(title)






import codewars_test as test

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(title_case(''), '')
        test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')
