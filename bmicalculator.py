weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in cms): "))

height_in_meters = height/100  

bmi = weight / (height_in_meters ** 2)

print("Your BMI is: ", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:  
    print("You are normal weight")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
else:
    print("You are obese")