def bmi(weight, height):
    BMI=weight/(height*height)

    if BMI<=18.5:
        return "Underweight"
    elif BMI<=25.0:
        return "Normal"
    elif BMI<=30.0:
        return "Overweight"
    elif BMI>30:
        return "Obese"


print(bmi(50,1.80))
print(bmi(80,1.80))
print(bmi(90,1.80))
print(bmi(100,1.80))