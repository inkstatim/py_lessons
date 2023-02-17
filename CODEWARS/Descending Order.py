# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python


def descending_order(num):
    numbers = []
    for i in str(num):
        numbers.append(int(i))
    sorted_num = (sorted(numbers, reverse=True))
    return int(''.join(str(n) for n in sorted_num))


