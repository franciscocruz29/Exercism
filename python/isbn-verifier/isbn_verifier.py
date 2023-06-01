# 1. Understand the problem:

# What is the input? 
# A string of numbers with or without hyphens

# What is the output? 
# A boolean, True if the string is a valid ISBN, False if not.

# What are the rules?
# The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). 
# In the case the check character is an X, this represents the value '10'. 

# It can be checked by the following formula:
# (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0

# If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

# 2. Examples:

# Input: '3-598-21508-8'
# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
# Output: True

# Input: '3-598-21507-X'
# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 7 * 2 + 10 * 1) mod 11 == 0
# Output: True

# Input: '3598215088'
# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
# Output: True

# Input: ''
# Output: False

# Input: '3-598-21507-A'
# Output: False

# Input: '3-598-2X507-9'
# Output: False

# Input: '134456729'
# Output: False

# 3. Algorithm:

# Step 1: Remove hyphens from the ISBN
# Step 2: Check if the length of the ISBN is 10
# Step 3: Initialize the total to 0
# Step 4: Iterate over each character in the ISBN
        # If the character is X and it's the last character, consider it as 10
        # Else if the character is a digit, add it to the total multiplied by its weight
        # If the character is not a digit and it's not X at the last position, return False
# Step 5: If the total modulo 11 is 0, then the ISBN is valid, otherwise it's invalid

# 4. Implementation:

""" def is_valid(isbn: str) -> bool:
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    total = 0

    for i, char in enumerate(isbn):
        if char == 'X' and i == 9:
            total += 10
        
        elif char.isdigit():
            total += int(char) * (10 - i)
        
        else:
            return False

    return total % 11 == 0 """

# 5. Refactoring:

def remove_hyphens(isbn: str) -> str:
    """Remove hyphens from the ISBN."""
    return isbn.replace('-', '')

def is_valid_length(isbn: str) -> bool:
    """Check if the length of the ISBN is 10."""
    return len(isbn) == 10

def calculate_total(isbn: str) -> int:
    """Calculate the total of the ISBN according to the validation rules."""
    return sum((10 - i) * (10 if c == 'X' else int(c)) for i, c in enumerate(isbn))

def is_digit_or_x(isbn: str) -> bool:
    """Check if every character is a digit or if the last character is X."""
    return all(c.isdigit() or (c == 'X' and i == 9) for i, c in enumerate(isbn))

def is_valid(isbn: str) -> bool:
    isbn = remove_hyphens(isbn)
    
    if not is_valid_length(isbn) or not is_digit_or_x(isbn):
        return False

    return calculate_total(isbn) % 11 == 0

