# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    res = dict()
    for i in seq:
        res[str(i)] = res.get(str(i), 0)+1
    for k,v in res.items():
        if v%2==0:
            continue
        else:
            return int(k)

print(find_it([1,2,3,3,2,1,4,1,2,3]))

#
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i