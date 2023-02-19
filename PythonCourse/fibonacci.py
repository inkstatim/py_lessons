# Variant 1
a = int(input())
fib = []
for i in range(1, a + 1):
    if i == 1 or i == 2:
        fib.append(1)
        print(1, end=' ')
    else:
        print(fib[-2] + fib[-1], end=' ')
        fib.append(fib[-2] + fib[-1])

# Variant 2
# def fib(n):
#     f1, f2 = 1, 1
#     while n > 0:
#         f1, f2 = f2, f1 + f2
#         n = n - 1
#     return f2
# n = int(input()) - 2
# print(fib(n))
