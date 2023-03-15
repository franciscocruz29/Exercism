from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(sentence):
    """
    Return True if the sentence is a pangram, False otherwise.
    """
    return ALPHABET.issubset(sentence.lower())

