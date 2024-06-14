# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str=input("Enter the string: ")
str1=input("Enter the substring to be checked for prefix/suffix: ")
if str[0]==str1 and str[-1]==str1:
    print("The strings contains both the {} in end and in start ".format(str1))
elif str[0]==str1:
    print("{} starts with {}".format(str,str1))
elif str[-1]==str1:
    print("{} ends with {}".format(str,str1))
else:
    if str1 in str:
        print("it does not starts with {} , its is in middle".format(str1))
    else:
        print("it does not contain {}".format(str1))