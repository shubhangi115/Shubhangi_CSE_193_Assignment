# write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

num_1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num_2 = float(input("Enter the second number: "))

if operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
elif operator == '/':
    if num_2 != 0:
        result = num_1 / num_2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Result: {}".format(result))
