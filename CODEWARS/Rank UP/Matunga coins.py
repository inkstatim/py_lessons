# https://www.codewars.com/kata/59799cb9429e83b7e500010c/train/python

def min_price(coins):
    n = max(coins) + 1
    found = False
    while not found:
        for i in range(1, n+1):
            if i not in coins:
                if all((i-j) in coins for j in coins):
                    return i
        n += 1
        if n > 10**6:
            return -1


# возвращаем сумму, которую нельзя получить монетами

print(min_price([3, 5])) # expected output: 8
print(min_price([4, 7])) # expected output: 18
print(min_price([5, 15])) # expected output: -1
print(min_price([6, 7, 8])) # expected output: 18
print(min_price([9, 14])) # expected output: 104
