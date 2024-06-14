# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str=input("Enter the string: ")
str_1=input("Enter the substring to be checked for prefix/suffix: ")
if str[0]==str_1 and str[-1]==str_1:
    print("The strings contains both the {} in end and in start ".format(str_1))
elif str[0]==str_1:
    print("{} starts with {}".format(str,str_1))
elif str[-1]==str_1:
    print("{} ends with {}".format(str,str_1))
else:
    if str_1 in str:
        print("it does not starts with {} , its is in middle".format(str_1))
    else:
        print("it does not contain {}".format(str_1))