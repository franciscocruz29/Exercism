# Step 1 - Problem Understanding:
#
# * What are the expected inputs? (Data type, Description)
#   - A string representing the name of the customer
#   - A positive integer from 1 up to 999 representing the customer's position in the line
#
# * What are the expected outputs? (Data type, Description)
#   - A string representing a sentence with this format "[name], you are the [number][suffix] customer we serve today. Thank you!"
#
# * Explicit requirements: What is clearly stated?
#   - The output message has to be formatted as "[name], you are the [number][suffix] customer we serve today. Thank you!"
#   - The suffix should be "st" for numbers ending in 1 (unless ending in 11), "nd" for numbers ending in 2 (unless ending in 12), "rd" for numbers ending in 3 (unless ending in 13), and "th" for all other numbers.
#   - Use numbers from 1 up to 999.
#
# * Implicit requirements: What is implied through examples or logic?
#   - The 11, 12, 13 exception rule overrides the last-digit rule.
#   - The name should be used exactly as provided (no formatting or validation implied).
#   - The output must be preserve: Commas, periods, capitalization and exact spacing.
#
# * Problem domain: Define any domain-specific terms or concepts
#   - Ordinal numerals are numbers that indicate position or order in a sequence.
#
# * Clarifying questions: What needs confirmation or is ambiguous?
#   - Are inputs guaranteed to always be within 1–999?
#   - Is the output expected to match the string exactly, including punctuation?
#
# * What is the mental model — a high-level description of how you think about the problem from start to finish (without worrying yet about implementation).
#   - Using the name and number from the input, return a sentence with the following format: "[name], you are the [number][suffix] customer we serve today. Thank you!" where [suffix] is the ordinal suffix for the number.

# Step 2 - Examples / Test Cases:
#
# Input: "Mary", 1
# Output: "Mary, you are the 1st customer we serve today. Thank you!"
#
# Input: "Jacqueline", 11
# Output: "Jacqueline, you are the 11th customer we serve today. Thank you!"
#
# Input: "Haruto", 2
# Output: "Haruto, you are the 2nd customer we serve today. Thank you!"
#
# Input: "Juan", 12
# Output: "Juan, you are the 12th customer we serve today. Thank you!"
#
# Input: "Henriette", 3
# Output: "Henriette, you are the 3rd customer we serve today. Thank you!"
#
# Input: "Patricia", 13
# Output: "Patricia, you are the 13th customer we serve today. Thank you!"
#
# Input: "Dahir", 162
# Output: "Dahir, you are the 162nd customer we serve today. Thank you!"
#
# Input: "Mateo", 111
# Output: "Mateo, you are the 111th customer we serve today. Thank you!"

# Step 3 - Data Structure:
#
# Input Data Types:
#  - name: String (to be used directly in the output).
#  - number: Integer (to be used for mathematical operations to determine the suffix).
#
# Intermediate Variables/Structures:
#  - Integer Variables: I will use variables to store the results of modulo operations:
#     - last_digit: number % 10 (to identify 1, 2, 3).
#     - last_two_digits: number % 100 (to identify the 11, 12, 13 exceptions).
#  - Dictionary (Optional but recommended): A dictionary mapping the remainders 1, 2, 3 to their respective suffixes "st", "nd", "rd". This replaces a long if/elif chain and makes the code more readable.
#     Example: {1: "st", 2: "nd", 3: "rd"}.
#
# Output Data Type:
#  - String: An f-string will be used to interpolate the name, number, and derived suffix into the final template.
#
# Mapping to Mental Model:
#   Input (name, number) → Derive suffix using integer operations and
#   conditionals → Format output string with f-string → Return result
#
#   Each data structure choice directly supports one step in this pipeline:
#   - Integers + modulo = suffix derivation
#   - String variables = clear intermediate state
#   - F-string = output construction

# Step 4 - Algorithm Design:
#
# 1. Input: name(string), number(integer)
# 2. Compute:
#      last_digit = number % 10
#      last_two_digits = number % 100
# 3. Determine the suffix:
#      IF last_two_digits is 11 OR 12 OR 13
#           suffix = "th"
#      ELSE IF last_digit is 1
#           suffix = "st"
#      ELSE IF last_digit is 2
#           suffix = "nd"
#      ELSE IF last_digit is 3
#           suffix = "rd"
#      ELSE
#           suffix = "th"
# 4. Construct the final message string using the exact template:
#       "[name], you are the [number][suffix] customer we serve today. Thank you!"
# 5. RETURN the final message

# Step 5 - Implementation:
#
def line_up(name: str, number: int) -> str:
    last_digit = number % 10
    last_two_digits = number % 100
    if last_two_digits in [11, 12, 13]:
        suffix = "th"
    elif last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"


# Step 6 - Refactoring:
#
# * Review your working code for clarity, efficiency, and adherence to style guides.
# * Make sure your code still handles edge cases and satisfies all test cases after refactoring.
