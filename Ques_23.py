#  Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
choice = input("Enter 'C/c' to convert Celsius to Fahrenheit, or 'F/f' to convert Fahrenheit to Celsius: ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("{} Celsius is equal to {} Fahrenheit.".format(celsius,fahrenheit))

elif choice.upper() == 'f':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("{} Fahrenheit is equal to {} Celsius.".format(fahrenheit,celsius))

else:
    print("Invalid choice. Please enter 'c' or 'f'.")
