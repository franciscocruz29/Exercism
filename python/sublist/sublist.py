# Step 1 - Problem Understanding:

# What are the expected inputs?
# - Data type: Two lists
# - Description: Each list can contain any number of elements (including zero elements for empty lists)

# What are the expected outputs?
# - Data type: A string or label
# - Description: The output should be one of the following values based on the relationship between the lists:
#   * "equal": When both lists contain exactly the same values in the same order.
#   * "superlist": When list A contains a contiguous sequence of values that exactly matches list B.
#   * "sublist": When list B contains a contiguous sequence of values that exactly matches list A.
#   * "unequal": When none of the above relationships hold.

# What are the key rules or constraints?
# 1. Equality requires same elements in same order (and implicitly, same length)
# 2. For superlist/sublist relationships, the contained list must appear as a contiguous sequence within the container list
# 3. The order of elements matters (as seen in the last example where [1,2,3] and [1,3,2] are considered unequal)
# 4. Empty lists have special handling:
#   * Two empty lists are considered equal
#   * An empty list is considered a sublist of any list
#   * Any non-empty list is considered a superlist of an empty list
# 5. The relationship must be exactly one of the four categories (they are mutually exclusive)

# What is the mental model?
# We need to determine which of four possible relationships exists between two given lists.


# Step 2 - Examples:

# Input: A = [], B = []
# Output: EQUAL

# Input: A = [1,2,3], B = []
# Output: SUPERLIST

# Input: A = [], B = [1,2,3]
# Output: SUBLIST

# Input: A = [1,2,3], B = [1,2,3,4,5]
# Output: SUBLIST

# Input: A = [1,2,3], B = [1,3,2]
# Output: UNEQUAL

# Input: A = [1,2,3,4,5], B = [2,3,4]
# Output: SUPERLIST


# Step 3 - Strategies:

# Strategy 1: Direct comparasion
# This approach examines the lists by directly checking for each relationship type in a specific order.
# - Key aspects: Simple, straightforward logic that follows the problem definition directly.
# Easy to understand but potentially performs redundant comparisons. Good for clarity but less efficient for large lists.

# Strategy 2: Unified Function-Based Approach
# This approach centralizes the logic by creating a single "is_sublist" function to determine
# if one list appears contiguously within another, then uses this function to determine all possible relationships.
# - Key aspects: Centralizes the core sublist detection logic in a reusable function.
# Improves code maintainability and reduces duplication. Cleaner logical structure but requires careful implementation of the central function.

# Strategy 3: Pattern Matching and Sliding Window
# This approach views the problem as a pattern matching challenge, using a sliding window technique to find one list within another.
# - Key aspects: Most efficient for large inputs, but more complex to implement.


# Step 4 - Algorithm Design:

# Initial Special Cases:
#   1. If both list_one and list_two are empty:
#       - Return EQUAL

#   2. Handle Other Empty List Cases:
#       - If list_one is empty: Return SUBLIST
#       - If list_two is empty: Return SUPERLIST

# Main Classification Logic:
#   3. Check for Equality:
#       - If list_one and list_two have the same length AND contain identical elements in the same order:
#       - Return EQUAL

#   4. Check for Sublist/Superlist Relationships:
#       - If length(list_one) < length(list_two):
#           - For each possible starting position i in list_two:
#               - If list_one matches list_two[i:i+length(list_one)]:
#                   - Return SUBLIST

#       - If length(list_one) > length(list_two):
#           - For each possible starting position i in list_one:
#               - If list_two matches list_one[i:i+length(list_two)]:
#                   - Return SUPERLIST

#   5. Default Case:
#       - Return UNEQUAL


# Step 5 - Implementation:

SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"
