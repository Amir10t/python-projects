try:
    number1 = int(input("Enter Number one : "))
    number2 = int(input("Enter Number two : "))
    
    operator = input("Enter Operator ,\n+ : Plus , - : Minus , * : Multiple , / : Divide  : ")

    def Plus(num1,num2):
        return num1 + num2

    def Minus(num1,num2):
        return num1 - num2

    def Multiple(num1,num2):
        return num1 * num2

    def Divide(num1,num2):
        return num1 / num2

    
    if operator == '+':
        number = Plus(number1,number2)
    elif operator == '-':
        number = Minus(number1,number2)
    elif operator == '*':
        number = Multiple(number1,number2)
    elif operator == '/':
        number = Divide(number1,number2)
    else:
        print("Error : Please Type Operator !!!")

    print(number)

except:
    print("Error : Please Enter Integer Number !!!")