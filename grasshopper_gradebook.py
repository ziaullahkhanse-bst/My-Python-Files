def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade(95, 90, 93))
print(get_grade(85, 80, 87))
print(get_grade(75, 72, 78))
print(get_grade(65, 60, 63))
print(get_grade(55, 50, 48))