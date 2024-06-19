def BMI_Calculator(weight, height):
    BMI = weight/(height**2)
    if BMI < 18.5:
        return f"Your BMI is {BMI}, you are underweight."
    elif BMI < 24.9:
        return f"Your BMI is {BMI}, you have a normal weight."
    elif BMI < 29.9:
        return f"Your BMI is {BMI}, you are overweight."
    elif BMI < 34.9:
        return f"Your BMI is {BMI}, you are obese (I)."
    elif BMI < 39.9:
        return f"Your BMI is {BMI}, you are obese (II)."
    else:
        return f"Your BMI is {BMI}, you are obese (III)."