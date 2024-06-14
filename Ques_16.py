# Write a program in python that counts the frequency of each character in a string.
str_1 = input("Enter a string: ")
frequency_dict = {}
i = 0
while i < len(str_1):
    char = str_1[i]
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1
    i += 1
keys = list(frequency_dict.keys())
i = 0
while i < len(keys):
    char = keys[i]
    print(f"The count of '{char}' is {frequency_dict[char]}")
    i += 1
