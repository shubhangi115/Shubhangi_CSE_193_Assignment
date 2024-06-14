#  Write a python program that checks if two strings are anagrams of each other.

word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word: ")

word_1 = word_1.lower()
word_2 = word_2.lower()

sorted_word1 = sorted(word_1)
sorted_word2 = sorted(word_2)

if sorted_word1 == sorted_word2:
    print('"{}" and "{}" are anagrams.'.format(word_1, word_2))
else:
    print('"{}" and "{}" are anagrams.'.format(word_1, word_2))
