# Write a program that copies the contents of one text file to another
read = open(r'C:\Users\i5\OneDrive\Desktop\STRING INPUT FROM USER\output_from user.txt', 'r')
write = open(r'C:\Users\i5\OneDrive\Desktop\STRING INPUT FROM USER\file_ques25.txt','w')
print(read.read(), file=write)