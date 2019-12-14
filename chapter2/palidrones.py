""" Finds palidromes in a dictionary file. """

import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')
palidrome_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palidrome_list.append(word)

print(f"\nNumber of palidromes found = {len(palidrome_list)}\n")
print(f"Out of {len(word_list)}!\n")
print(*palidrome_list, sep='\n')
