# write a python program that returns the minimum and maximum values in a list of numbers.
list_1=input("ENTER LIST with spaces between elements: ").split()
print("the list ")
m=list_1[0]
i=0
while i<len(list_1):
    if list_1[i]<m:
        m=list_1[i]
    i=i+1
print("min is: ",m)

m1=list_1[0]
i=0
while i<len(list_1):
    if list_1[i]>m1:
        m=list_1[i]
    i=i+1
print("max is: ",m)