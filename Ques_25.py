# Write a program that copies the contents of one text file to another
read_file= open(r'C:\Users\i5\OneDrive\Desktop\STRING INPUT FROM USER\output_from user.txt', 'r')
write_file = open(r'C:\Users\i5\OneDrive\Desktop\STRING INPUT FROM USER\file_ques25.txt','w')
print(read_file.read(), file=write_file)