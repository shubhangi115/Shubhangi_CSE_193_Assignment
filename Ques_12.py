#  Write a python program that calculates the sum of the digits of a given number
str_1=input("enter number ")
sum=0
i=0
while i< len(str_1):
    sum=sum+int(str_1[i])
    i=i+1
print("the sum is: ",sum)
