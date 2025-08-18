from PyBasics.Day1 import result

firstNum = float(input("Please enter the first number: "))
operator = input("Please enter the operator (+, -, *, /, //, e): ")
secondNum = float(input("Please enter the second number: "))
if(operator == '+'):
    result = firstNum + secondNum
elif(operator == '-'):
    result = firstNum - secondNum
elif(operator == '*'):
    result = firstNum * secondNum
elif(operator == '/'):
    if secondNum != 0:
        result = firstNum / secondNum
    else:
        result = "Error: Division by zero is not allowed."
elif(operator == '//'):
    if secondNum != 0:
        result = firstNum // secondNum
    else:
        result = "Error: Division by zero is not allowed."
elif(operator == 'e'):
    result = firstNum ** secondNum
else:
    result = "Error: Invalid operator."

print("The result is:", result)


