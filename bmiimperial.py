impweight = float(input("Enter your weight in pounds: "))
impheight = float(input("Enter your height in inches: "))
weight = impweight * 0.453592
# print("Here is your weight in KG: " + str(weight))
height = impheight * 0.0254
# print("Here is your height in meters: " + str(height))
BMI = weight/(height*height)
print("BMI is {:.10f}".format(BMI))
# print("BMI is " + str(BMI))
