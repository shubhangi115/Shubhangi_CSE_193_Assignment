#  Write a python program that calculates the sum of the digits of a given number
str=input("enter number ")
sum=0
i=0
while i< len(str):
    sum=sum+int(str[i])
    i=i+1
print("the sum is: ",sum)
