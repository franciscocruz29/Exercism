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

# Step 4 - Implementation
#
def encode(plain_text):
    pass


def decode(ciphered_text):
    pass
