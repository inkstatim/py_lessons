# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    url = url.replace('http://', '').replace('https://', '').replace('www.', '')

    return url.split('/')[0].split('.')[0]


import codewars_test as test

test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")
