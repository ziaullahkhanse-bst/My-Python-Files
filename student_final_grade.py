def final_grade(exam, projects):
    if exam >90 or projects>10:
        finalgrade=100
    elif exam >75 and projects>=5:
        finalgrade=90
    elif exam >50 and projects>=2:
        finalgrade=75
    else:
        finalgrade=0

    return finalgrade



print(final_grade(100,12))
print(final_grade(99,0))
print(final_grade(10,15))
print(final_grade(85,5))
print(final_grade(55,3))
print(final_grade(55,0))
print(final_grade(20,2))