#  Write a python program that checks if two strings are anagrams of each other.

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word1 = word1.lower()
word2 = word2.lower()

sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

if sorted_word1 == sorted_word2:
    print('"{}" and "{}" are anagrams.'.format(word1, word2))
else:
    print('"{}" and "{}" are anagrams.'.format(word1, word2))
