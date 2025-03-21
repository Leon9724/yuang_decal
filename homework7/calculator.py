#calculator
import math_tools

num1 = float(input("enter the 1st num"))
num2 = float(input("enter the 2nd num"))

operation = input("choose an op(add, subtract, multiply, divide) ")

if operation == "add":
    result = math_tools.add(num1, num2)
elif operation == "subtract":
    result = math_tools.subtract(num1, num2)
elif operation == "multiply":
    result = math_tools.multiply(num1, num2)
elif operation == "divide":
    result = math_tools.divide(num1, num2)
else:
    result = "error"

print(result)