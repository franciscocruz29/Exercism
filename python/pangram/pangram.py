# 1. Problem Understanding:

# * What are the expected inputs?
#   - Data type: string
#   - A string representing the sentence to be checked.

# * What are the expected outputs?
#   - Data type: boolean
#   - true if the sentence is a pangram, false otherwise.

# * What are the key rules or constraints?
#   - Case Insensitivity: The comparison of letters should be case-insensitive, meaning that 'a' and 'A' are considered the same letter.
#   - Alphabet Letters Only: Only the 26 letters of the English alphabet ('a' to 'z') matter. Any other characters, such as digits, punctuation, or spaces, should be ignored.
#   - Presence of All Letters: A sentence must contain at least one occurrence of each letter of the alphabet. If any letter is missing, the sentence is not a pangram.

# * What is the mental model?
#   - We need to verify if every letter of the alphabet appears at least once in the sentence.

# 2. Examples and Test Cases:

# Input: "The quick brown fox jumps over the lazy dog"
# Output: true

# Input: "The quick brown fox jumps over the lazy cat"
# Output: false

# Input: "AbCdEfGhIjKlMnOpQrStUvWxYz"
# Output: true

# Input: "Hello, World!"
# Output: false

# 3. Data Structure Selection:

# * What data structure(s) would best suit this problem?
#   - We'll use a set to store unique alphabetic characters. This ensures that each letter is counted only once

# 4. Algorithm Design:

# 1. Define the Alphabet: Create a set of all 26 lowercase alphabetic characters ('a' to 'z') using ascii_lowercase from the string module.
# 2. Convert the Sentence to Lowercase: Convert the input sentence to lowercase to ensure case-insensitivity when comparing the letters.
# 3. Check if Alphabet is a Subset: Using the issubset method, check if the alphabet set is a subset of the set of characters in the lowercase version of the sentence. This will automatically ignore non-alphabetical characters.
# 4. Return Result: If the alphabet is a subset, return True (indicating the sentence is a pangram); otherwise, return False

from string import ascii_lowercase

ALPHABET: set[str] = set(ascii_lowercase)

def is_pangram(sentence: str) -> bool:
    return ALPHABET.issubset(set(sentence.lower()))
