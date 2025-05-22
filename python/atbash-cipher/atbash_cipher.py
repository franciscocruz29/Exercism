# Step 1 - Problem Understanding
#
# What are the expected inputs?
# - Data type: string
# - Description: A string that may contain uppercase or lowercase letters, digits, spaces, and punctuation.
#               * Only alphabetic characters are encoded using the Atbash cipher.
#               * Digits are preserved as-is.
#               * Punctuation is removed.
#               * All letters are converted to lowercase before encoding.
#
#
# What are the expected outputs?
# - Data type: string
# - Description:
#               * For encoding: a lowercase string where alphabetic characters are replaced with their reversed alphabet counterparts, digits are preserved, and all non-alphanumeric characters are removed. The result is grouped in blocks of five characters, separated by spaces.
#               * For decoding: a lowercase string where Atbash-encoded letters are decoded back to the original text, digits are preserved, and spaces are removed.
#
# What are the key rules or constraints?
# - The Atbash cipher replaces each letter with its corresponding letter in a reversed alphabet (a ↔ z, b ↔ y, ..., m ↔ n).
# - Only alphabetic characters are encoded; digits remain unchanged.
# - Punctuation and spaces are removed before encoding.
# - Encoded output is written in lowercase and grouped into chunks of 5 characters separated by spaces.
# - Decoding removes the grouping and returns the plain text in lowercase.
#
# What is the mental model?
# - To encode:
#   * Clean the input by removing punctuation and converting letters to lowercase.
#   * Apply the Atbash substitution for each letter.
#   * Leave digits as they are.
#   * Group the resulting string into chunks of 5 characters separated by spaces.
#
# - To decode:
#   * Remove all spaces.
#   * Apply the Atbash substitution to decode letters.
#   * Leave digits as they are.


# Step 2 - Examples
#
# Encode:
#
# Input: "test"
# Output: "gvhg"
#
# Input: "mindblowingly"
# Output: "nrmwy oldrm tob"
#
# Input: "Testing,1 2 3, testing."
# Output: "gvhgr mt123 gvhgr mt"
#
# Decode:
#
# Input: "vcvix rhn"
# Output: "exercism"
#
# Input: "gvhgr mt123 gvhgr mt"
# Output: "testing123testing"
#
# Input: "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
# Output: "thequickbrownfoxjumpsoverthelazydog"


# Step 3 - Algorithm design

# Encoding Algorithm:
#
# 1. Start with an empty result.
# 2. Go through each character in the input:
#   - If it's a letter:
#       - Convert it to lowercase.
#       - Replace it with the corresponding letter from the reversed alphabet (e.g., a → z, b → y, c → x, etc.).
#       - Add the ciphered letter to the result.
#   - If it's a number (0–9):
#       - Leave it as it is and add it to the result.
#   - If it's anything else (like punctuation or spaces):
#       - Ignore it. Don't include it in the result.
# 3. Once all characters have been processed, take the resulting string and split it into groups of five characters.
#   - If the final group has fewer than five characters, that’s okay—just leave it as-is.
# 4. Join the groups together using spaces, and that’s your final encoded message.
#
# Decoding Algorithm:
#
# 1. Start by removing all spaces from the input string.
# 2. Go through each character in the cleaned-up string:
#   - If it's a letter:
#       - Replace it with the corresponding letter from the reversed alphabet (same rule: a ↔ z, b ↔ y, etc.).
#       - Add the decoded letter to the result.
#   - If it's a number:
#       - Leave it unchanged and add it to the result.
#   - Ignore any other characters, though there shouldn’t be any if the input is valid.
# 3. Return the result as a single, lowercase string with no spaces.


# Step 4 - Implementation

import string
from textwrap import wrap

# Create the Atbash cipher mapping (a ↔ z, b ↔ y, c ↔ x, etc.)
ATBASH_MAP = str.maketrans(
    string.ascii_lowercase,
    string.ascii_lowercase[::-1]  # Reverse the alphabet
)


def remove_punctuation_and_spaces(text):
    """
    Keep only letters and numbers, convert to lowercase.
    Example: "Hello, World! 123" → "helloworld123"
    """
    return ''.join(char.lower() for char in text if char.isalnum())


def group_into_chunks(text, chunk_size=5):
    """
    Split text into groups of 5 characters separated by spaces.
    Example: "helloworld" → "hello world"
    """
    return ' '.join(wrap(text, chunk_size))


def encode(plain_text):
    """
    Encode text using the Atbash cipher.

    Steps:
    1. Remove punctuation and convert to lowercase
    2. Apply Atbash substitution to letters (digits stay the same)
    3. Group result into chunks of 5 characters

    Example: "Hello World!" → "svool dliow"
    """
    # Step 1: Clean the input
    cleaned_text = remove_punctuation_and_spaces(plain_text)

    # Step 2: Apply Atbash cipher
    encoded_characters = []
    for character in cleaned_text:
        if character.isalpha():
            # Apply Atbash substitution to letters
            encoded_characters.append(character.translate(ATBASH_MAP))
        else:
            # Keep digits unchanged
            encoded_characters.append(character)

    # Step 3: Join and group into chunks
    encoded_text = ''.join(encoded_characters)
    return group_into_chunks(encoded_text)


def decode(encoded_text):
    """
    Decode an Atbash-encoded string.

    Steps:
    1. Remove all spaces
    2. Apply Atbash substitution to letters (digits stay the same)

    Example: "svool dliow" → "helloworld"
    """
    # Step 1: Remove spaces
    text_without_spaces = encoded_text.replace(' ', '')

    # Step 2: Apply Atbash cipher (same operation as encoding)
    decoded_characters = []
    for character in text_without_spaces:
        if character.isalpha():
            # Apply Atbash substitution to letters
            decoded_characters.append(character.translate(ATBASH_MAP))
        else:
            # Keep digits unchanged
            decoded_characters.append(character)

    return ''.join(decoded_characters)
