# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ''
    new_c = dict((key, 0) for key in list_of_cat)
    new_a = [x.split() for x in list_of_art]
    for i in new_a:
        if i[0][0] in new_c:
            new_c[i[0][0]] += int(i[1])
    return ' - '.join(f'({key} : {value})' for key, value in new_c.items())





import codewars_test as test


@test.describe("Testing")
def _():
    @test.it("Tests")
    def _():
        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        test.assert_equals(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")
