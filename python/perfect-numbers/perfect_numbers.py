# Step 1 - Problem Understanding:

# What are the input?
# A single positive integer, n.

# What is the output?
# A string indicating whether the number n is "perfect," "abundant," or "deficient."

# What are the rules?:
# - Aliquot Sum: The sum of the proper divisors of n (i.e., divisors excluding n itself).
# - Classifications:
#       Perfect: If the aliquot sum equals n.
#       Abundant: If the aliquot sum is greater than n.
#       Deficient: If the aliquot sum is less than n.
# - The input will always be a positive integer.

# What is the mental model?
# You can think of this as a process where for a given number n, you gather all its divisors
# (excluding n itself), sum them up, and then compare the sum to n.
# Based on this comparison, the number is classified into one of the three categories.

# Step 2 - Examples and Test Cases:

# Example 1:
# Input: 6
#   Factors: 1, 2, 3
#   Aliquot sum: 1 + 2 + 3 = 6
# Output: Perfect

# Example 2:
# Input: 12
#   Factors: 1, 2, 3, 4, 6
#   Aliquot sum: 1 + 2 + 3 + 4 + 6 = 16
# Output: Abundant

# Example 3:
# Input: 8
#   Factors: 1, 2, 4
#   Aliquot sum: 1 + 2 + 4 = 7
# Output: Deficient

# Step 3 - Algorithm Design:

# 1. Accept the input number
# 2. Find all factors of the number (excluding the number itself):
#   - Iterate from 1 to the square root of the number
#   - If the number is divisible by the current iterator, add both the iterator and the result of the division to the factors list (unless they're the same)
# 3. Calculate the aliquot sum by summing all the factors
# 4. Compare the aliquot sum to the original number:
#   - If equal, classify as "perfect"
#   - If greater, classify as "abundant"
#   - If less, classify as "deficient"
# 5. Return the classification

# Step 4 - Implementation:

import math
from typing import List, Union

def find_factors(n: int) -> List[int]:
    factors: List[int] = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    factors.remove(n)  # Remove the number itself
    return factors

def calculate_aliquot_sum(factors: List[int]) -> int:
    return sum(factors)

def classify(n: int) -> str:
    if n <= 0:
        raise ValueError( "Classification is only possible for positive integers.")

    factors = find_factors(n)
    aliquot_sum = calculate_aliquot_sum(factors)

    if aliquot_sum == n:
        return "perfect"
    elif aliquot_sum > n:
        return "abundant"
    else:
        return "deficient"
