# Write a program that takes a string input from the user and writes it to a text file
str1 = input("What do you like to write in your file? ")
sample_file = open(r'C:\Users\i5\OneDrive\Desktop\STRING INPUT FROM USER\output_from user.txt', 'w')
print(str1, file = sample_file)