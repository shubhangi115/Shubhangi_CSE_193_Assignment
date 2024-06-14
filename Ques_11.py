#  Write a python program that generates the first n numbers in the Fibonacci sequence.
num=int(input("Enter n: "))
a=0
b=1
sum=0
i=1
while i<=num:
    sum=sum+a
    print(sum)
    a=b
    b=sum
    i=i+1
    

