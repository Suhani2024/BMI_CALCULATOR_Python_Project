weight = int(input("enter your weight in kgs: "))
height = int(input("enter your height in cm: "))

bmi = (weight *703) / (height * height)
print(bmi)

if bmi > 0:
    if (bmi < 18.5):
        print("under weight")
    if (bmi >= 18.5) and (bmi <= 24.9):
        print("normal weight")
    if (bmi >= 25) and (bmi <= 29.9):
        print("overweight")
    if (bmi >= 30) and (bmi <= 34.9):
        print("obese")
    if (bmi >= 35) and (bmi <= 39.9):
        print("severely obese")
    if (bmi >=40) and (bmi < 100):
        print("over morbidly obese")
else:
    print("incorrect")