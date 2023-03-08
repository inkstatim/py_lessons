# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

def multiplication_table(n):
    table = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            table[i][j] = (i + 1) * (j + 1)
    return table


# def multiplicationTable(size):
#     return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]