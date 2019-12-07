""" Counts the number of occurances for a character in a string. """
from collections import defaultdict

def main(string):
    """ Prints a dictionary containing the ammount of occurances for each letter in a string. """
    default_dict = defaultdict(int)
    for char in string:
        if char != ' ':
            default_dict[char.lower()] += 1

    return default_dict
