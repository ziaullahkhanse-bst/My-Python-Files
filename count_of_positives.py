def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count_pos = 0
    sum_neg = 0
    
    for num in arr:
        if num > 0:
            count_pos = count_pos + 1
        elif num < 0:
            sum_neg = sum_neg + num
    
    return [count_pos, sum_neg]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([0, 0, 0]))
print(count_positives_sum_negatives([1, -1, 2, -2, 3, -3]))