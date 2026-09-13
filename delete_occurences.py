def delete_nth(order, max_e):
    counts = {}
    result = []
    for num in order:
        if counts.get(num, 0) < max_e:
            result.append(num)
            counts[num] = counts.get(num, 0) + 1
        else:
            print(f"Skipping {num} (already appeared {max_e} times)")
    return result


# Example 1
order1 = [1, 2, 3, 1, 2, 1, 2, 3]
max_e1 = 2
print("Input:", order1)
print("Max allowed:", max_e1)
result1 = delete_nth(order1, max_e1)
print("Output:", result1)
print("-" * 40)

# Example 2
order2 = [20, 37, 20, 21]
max_e2 = 1
print("Input:", order2)
print("Max allowed:", max_e2)
result2 = delete_nth(order2, max_e2)
print("Output:", result2)