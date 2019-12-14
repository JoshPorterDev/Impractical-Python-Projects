def check_palingram(phrase):
    phrase = phrase.replace(' ', '')

    if phrase == phrase[::-1]:
        print(f"The phrase ({phrase}) is a palingram.")
    else:
        print(f"The phrase ({phrase}) is not a palingram.")

import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
palingram_list = []

for word in word_list:
    stripped_word = word.replace(' ', '')
    if stripped_word == word[::-1]:
        palingram_list.append(word)
    
print(f"\nNumber of palingrams found = {len(palingram_list)}\n")
print(f"Out of {len(word_list)}!\n")
print(*palingram_list, sep='\n')