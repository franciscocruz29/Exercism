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


# Step 5 - Implementation

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one, list_two):
    pass
