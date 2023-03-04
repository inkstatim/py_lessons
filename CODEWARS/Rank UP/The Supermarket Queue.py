# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    tills = [0] * n
    for c in customers:
        tills[tills.index(min(tills))] += c
    return max(tills)

# Понравилось решение
# def queue_time(customers, n):
#     qn = [0] * n
#     for c in customers:
#         qn = sorted(qn)
#         qn[0] += c
#     return max(qn)