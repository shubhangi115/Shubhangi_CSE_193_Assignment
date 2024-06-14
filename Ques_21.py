# Write a python program that counts the occurrences of a specific element in a list.
# Input list of elements from user
str_1 = input("Enter elements of the list separated by spaces: ").split()

element_to_count = input("Enter the element to count: ")

count = 0

for i in str_1:
    if i == element_to_count:
        count += 1

print("The element '{}' appears {} times in the list.".format(element_to_count,count))
