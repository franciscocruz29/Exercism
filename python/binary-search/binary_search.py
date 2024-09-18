# Step 1 - Problem Understanding:

# - Inputs:
# A sorted list (search_list) and a value to find (value).

# - Output:
# The index of the value in the list if found, or a ValueError if not found.

# - Requirements:
#   * The list must be sorted in ascending order.
#   * If the value is found, return its index.
#   * If the value is not found, raise a ValueError with the message "value not in array".

# - Mental model:
# Repeatedly divide the search space in half, comparing the middle element with the target value
# until the value is found or the search space is exhausted.


# Step 2 - Examples and Test Cases:

# Example 1: Middle Element Found
# Input: [1, 3, 4, 6, 8, 9, 11], 6
# Output: 3

# Example 2: Element Not Found
# Input: [1, 3, 4, 6, 8, 9, 11], 7
# Output: ValueError("value not in array")

# Edge Case: Empty List
# Input: [], 1
# Output: ValueError("value not in array")


# Step 3 - Algorithm Design:

# 1. Initialize:
#   - Set left to 0 (the start of the list).
#   - Set right to len(search_list) - 1 (the end of the list).
# 2. Iterate and Search:
#   - While left is less than or equal to right:
#       * Calculate mid as the average of left and right, rounded down to the nearest integer: mid = (left + right) // 2.
#       * If the value at search_list[mid] is equal to the value we're searching for, return mid.
#       * If search_list[mid] is less than the value, it means the value (if it exists) must be in the right half of the list. Update left = mid + 1.
#       * If search_list[mid] is greater than the value, it means the value (if it exists) must be in the left half of the list. Update right = mid - 1.
# 3. Value Not Found:
#   - If the loop completes without returning, it means the value was not found in the list. Raise a ValueError with the message "value not in array".


# Step 4 - Implementation:

from typing import List

def find(search_list: List[int], value: int) -> int:
    left: int = 0
    right: int = len(search_list) - 1

    while left <= right:
        mid: int = (left + right) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")
