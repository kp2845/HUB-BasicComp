weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = weight/(height*height)
if BMI < 18.5:
    category = "Underweight"
elif BMI >= 18.5 and BMI < 24.9:
    category = "Normal"
elif BMI >= 25.0 and BMI < 29.9:
    category = "Overweight"
elif BMI > 30:
    category = "Obese"
print("BMI is {:.2f}".format(BMI) + ", Status is {}".format(category))
# print("BMI is " + str(BMI))
