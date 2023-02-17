def count_positives_sum_negatives(arr: list):
    if arr:
        count = 0
        suma = 0
        for i in arr:
            if i > 0:
                count += 1
            elif i < 0:
                suma += i
        return [count, suma]
    else:
        return []


print(count_positives_sum_negatives([]))
