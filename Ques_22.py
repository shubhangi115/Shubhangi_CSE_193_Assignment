# write a python program that returns the minimum and maximum values in a list of numbers.
list1=input("ENTER LIST with spaces between elements: ").split()
print("the list ")
m=list1[0]
i=0
while i<len(list1):
    if list1[i]<m:
        m=list1[i]
    i=i+1
print("min is: ",m)

m1=list1[0]
i=0
while i<len(list1):
    if list1[i]>m1:
        m=list1[i]
    i=i+1
print("max is: ",m)