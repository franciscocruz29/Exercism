def is_pangram(sentence):
    """
    Return True if the sentence is a pangram, False otherwise.
    """
    return set('abcdefghijklmnopqrstuvwxyz') <= set(sentence.lower())

