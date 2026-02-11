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
# * What data structures will be used and why?.Determine the appropriate data structure(s) to work with to convert the input to the output.
# * Think about how your mental model maps to data structure choices.
# * This choice is critical because it will influence the algorithm.

# Step 4 - Algorithm Design:
#
# * Determine a series of precise instructions (pseudocode) that will transform the input to the desired output.
# * Ensure the algorithm is detailed enough to be easily coded, but not written at the programming language level to maintain flexibility.
# * Manually test the algorithm with your examples to ensure confidence.

# Step 5 - Implementation:
#
# * Translate your algorithm into code in your chosen programming language.

# Step 6 - Refactoring:
#
# * Review your working code for clarity, efficiency, and adherence to style guides.
# * Make sure your code still handles edge cases and satisfies all test cases after refactoring.


def line_up(name, number):
    pass
