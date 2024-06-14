# Write a program in python that converts a string into a list of its characters
str_1=input("Enter the string ")
list1=[]                             
j=0
while j<len(str):
    list1=list1+list(str[j])
    j=j+1
print("The list is: ", list1)