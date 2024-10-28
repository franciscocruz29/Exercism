# Step 1 - Problem Understanding:
#
# - What are the expected inputs?
#   - Data type: String
#   - Description: A string representing the text to be translated.
#
# - What are the expected outputs?
#   - Data type: String
#   - Description: Words modified according to the Pig Latin rules.
#
# - What are the key rules or constraints?
#   We need to translate English words into Pig Latin based on four specific rules:
#   - Rule 1: Words that begin with a vowel (a, e, i, o, u) or start with "xr" or "yt" are handled similarly, with "ay" appended to the word.
#   - Rule 2: Words that start with one or more consonants move those consonants to the end, then append "ay".
#   - Rule 3: If a word starts with a consonant followed by "qu", the consonants and "qu" are moved to the end, then "ay" is appended.
#   - Rule 4: If a word starts with one or more consonants followed by "y", the consonants before "y" are moved to the end, then "ay" is added.
#
# - What is the mental model?
#   - The problem can be viewed as identifying structural patterns in a sequence of characters (the word),
#     applying a set of defined transformations (shifting and appending), and outputting the modified sequence.

# Step 2 - Examples:
#
# Input: "apple"
# Output: "appleay"
#
# Input: "chair"
# Output: "airchay"
#
# Input: "quick"
# Output: "ickquay"
#
# Input: "rhythm"
# Output: "ythmrhay"
#
# Input: "quick fast run"
# Output: "ickquay astfay unray"

# Step 3 - Algorithm Design:
#
# 1. Split the input string into individual words.
# 2. Identify the rule that applies to each word:
#    - Check if it starts with a vowel or the special prefixes "xr" or "yt".
#    - Otherwise, check for consonants, consonant clusters, or specific patterns like "qu"
# 3. Modify the word based on the rule:
#    - Based on the determined rule, apply the transformation to each word:
#       - For Rule 1: word + "ay"
#       - For Rule 2: word[vowel_pos:] + word[:vowel_pos] + "ay"
#       - For Rule 3: word[2:] + "quay"
#       - For Rule 4: word[vowel_pos:] + word[:vowel_pos] + "ay"
# 4. Join the translate words back into a single output string

# Step 4 - Implementation:

from typing import List

VOWELS = "aeiou"

def is_vowel(char: str) -> bool:
    """Check if the character is a vowel."""
    return char in VOWELS

def find_first_vowel_pos(word: str) -> int:
    """Find the position of the first vowel or the 'y' treated as a vowel after consonants."""
    for i, char in enumerate(word):
        # Special case: 'qu' combination
        if char == 'q' and i < len(word) - 1 and word[i + 1] == 'u':
            return i + 2

        # Treat 'y' as a vowel if it's not the first letter
        if char == 'y' and i > 0:
            return i

        # Regular vowel check
        if is_vowel(char):
            return i

    # Return length of word if no vowels are found
    return len(word)

def transform_word(word: str) -> str:
    """Convert a single word into Pig Latin."""
    if word.startswith(('xr', 'yt')) or is_vowel(word[0]):
        return word + 'ay'

    if word.startswith('qu'):
        return word[2:] + 'quay'

    vowel_pos = find_first_vowel_pos(word)
    return word[vowel_pos:] + word[:vowel_pos] + 'ay'

def translate(text: str) -> str:
    """Convert a sentence into Pig Latin."""
    words: List[str] = text.split()
    return ' '.join(transform_word(word) for word in words)
