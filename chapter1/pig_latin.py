""" Generates pig latin based on a given word """

def pig_latin(word):
    """ Takes a given word and returns its piglatin counterpart. """
    return word[1:] + word[0] + 'ay'
