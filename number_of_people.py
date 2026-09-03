def number(bus_stops):
    people = 0
    for stop in bus_stops:
        people = people + stop[0]
        people = people - stop[1]
    return people

print(number([[10, 0], [3, 5], [5, 8]]))
print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
print(number([[1, 0], [2, 1], [3, 2], [4, 3]]))