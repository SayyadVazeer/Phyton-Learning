operator = input ( "Enter an operator (+ - * /)")
num1 = float(input("enter the num1 : "))
num2 = float(input("enter the num2 : "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print("Enter Valid operation ")