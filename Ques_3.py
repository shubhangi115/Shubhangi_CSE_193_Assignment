# Write a python program that calculates the factorial of a given number
num=int(input("Enter the number: "))
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print("the factorial of {} is {}".format(num,fact))