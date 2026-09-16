def open_or_senior(data):
    result = []
    for person in data:
        age = person[0]
        handicap = person[1]
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior([[55, 8], [54, 8], [55, 7], [60, 10]]))
print(open_or_senior([]))