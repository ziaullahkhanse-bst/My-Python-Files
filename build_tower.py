def tower_builder(n_floors):
    result = []
    for i in range(1, n_floors + 1):
        spaces = " " * (n_floors - i)
        stars = "*" * (2 * i - 1)
        result.append(spaces + stars + spaces)
    return result

print(tower_builder(3))
print(tower_builder(6))