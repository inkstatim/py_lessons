# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    if len(str(n)) == 1:
        return 0
    count = 0
    while n >= 10:
        prod = 1
        for i in str(n):
            prod*=int(i)

        n = prod
        count+=1
    return count

print(persistence(25))


