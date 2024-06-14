# Write a python program that takes a list of numbers and returns their sum
str_1=input("Enter the string ")
list1=[]                             #list1=list(str) can also be used
j=0
while j<len(str_1):
    list1=list1+list(str_1[j])
    j=j+1
print("The list is: ", list1)
sum=0
i=0
while i<len(list1):
    sum=sum+int(list1[i])
    i=i+1
print("The sum is: ",sum)