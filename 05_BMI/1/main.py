weight = float(input("Enter Your Weight(kg) : "))
height = float(input("Enter Your Height(m) : "))
BMI = weight/(height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 24.9:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 29.9:
    print(f"Your BMI is {BMI}, you are overweight.")
elif BMI < 34.9:
    print(f"Your BMI is {BMI}, you are obese (I).")
elif BMI < 39.9:
    print(f"Your BMI is {BMI}, you are obese (II).")
else:
    print(f"Your BMI is {BMI}, you are obese (III).")