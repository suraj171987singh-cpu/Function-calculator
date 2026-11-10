def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("FUNCTION CALCULATOR")
try:
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    operator = input("Enter the operator (add, subtract, multiply, divide): ")

    if operator == "add":
        result = add(first_num, second_num)
        print(result)
    elif operator == "subtract":
        result = subtract(first_num, second_num)
        print(result)
    elif operator == "multiply":
        result = multiply(first_num, second_num)
        print(result)
    elif operator == "divide":
        result = divide(first_num, second_num)
        print(result)
    else:
        print("Invalid operator")
except ValueError:
        print("Enter a valid number")
except ZeroDivisionError:
    print("The number cannot be divided by zero")
finally:
    print("Thanks for using the calculator!")

                 


