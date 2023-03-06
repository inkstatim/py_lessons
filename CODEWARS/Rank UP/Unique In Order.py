# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    if not sequence:
        return []
    uniq = [sequence[0]]
    for i in range(1, len(sequence)):
        q = sequence[i]
        if q == uniq[-1]:
            continue
        else:
            uniq.append(q)
    return uniq
    # uniq = [sequence[0]]
    # for i in range(len(sequence)-1):
    #     q = sequence[i+1]
    #     if q == uniq[i-1]:
    #         continue
    #     else:
    #         uniq.append(q)
    # return uniq