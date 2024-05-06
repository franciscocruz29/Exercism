# 1. Understand the problem:

# What is the input?
# A string and an integer representing the number of letters to rotate the string from 0 to 26

# What is the output?
# A string, the rotated version of the input string

# What are the requirements?
# The letter is shifted for as many values as the value of the key

# What are the rules of the problem?
# The general notation for rotational ciphers is `ROT + <key>`


# 2. Examples:

# rotate("O M G", 5) -> "T R L"
# rotate("a", 1) -> "b"
# rotate("Testing 1 2 3 testing", 4) -> "Xiwxmrk 1 2 3 xiwxmrk"


# 3. Algorithm:

# !!! This approach only supports the English alphabet. Non-English alphabets are not contiguous in their ascii number ranges, and are not consistently defined across platforms.

# 1. Receive the text message and the rotation key (an integer representing the number of positions each letter should be shifted).
# 2. Check if the rotation key is within the range of 0 to 26 (inclusive). If it's not, handle the error accordingly.
# 3. Iterate through each character in the text message.
#       For each character:
#       If it's an alphabetic character(a letter):
#           Determine if it's uppercase or lowercase.
#           Calculate the new position of the letter by adding the rotation key to its ASCII value.
#           Handle wrapping around the alphabet(e.g., if Z is shifted by 1, it becomes A).
#       If it's not an alphabetic character(e.g., punctuation, spaces), leave it unchanged.
#       Append the modified character to the cipher text.
# 4. Return the cipher text.


# 4. Implementation:

""" def rotate(text, key):
    # Validate rotation key
    if not 0 <= key <= 26:
        return "Rotation key must be between 0 and 26."

    cipher_text = ""

    for char in text:
        if char.isalpha():
            # Determine if it's uppercase or lowercase
            if char.isupper():
                base = ord('A')
            else:
                # (returns the Unicode code point for a given character)
                base = ord('a')
            # Calculate new position of the letter
            new_pos = (ord(char) - base + key) % 26 + base
            # Convert ASCII value back to character
            cipher_char = chr(new_pos)
        else:
            # Non-alphabetic characters remain unchanged
            cipher_char = char
        cipher_text += cipher_char

    return cipher_text """


# 5. Refactoring:
def rotate(text, key):
    """
    Encrypts text using a rotational cipher with the given key.

    Args:
        text: The text to encrypt (string).
        key: The rotation key (integer between 0 and 25).

    Returns:
        The encrypted text (string).

    Raises:
        ValueError: If the rotation key is not between 0 and 25.
    """

    # Validate rotation key
    if not 0 <= key <= 26:
        raise ValueError("Rotation key must be between 0 and 26.")

    # Define a function for character encryption
    def encrypt_char(char):
        if not char.isalpha():
            return char  # Non-alphabetic characters remain unchanged

        base = ord('A') if char.isupper() else ord('a')
        new_pos = (ord(char) - base + key) % 26 + base
        return chr(new_pos)

    # Apply encryption to each character
    cipher_text = ''.join(encrypt_char(char) for char in text)
    return cipher_text
