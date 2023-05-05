# 1. Understand the problem:

#   - What is the input?
#       A nested list

#   - What is the output?
#       A single flattened list with all values except None

#   - What are the requirements or the goal?
#      To write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure

#   - What are the constraints?
#     The output list should not contain any None values


# 2. Examples:

# input = []
# expected = []

# input = [[[]]]
# expected = []

# input = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
# expected = [0, 2, 2, 3, 8, 100, 4, 50, -2]

# inputs = [None, [[[None]]], None, None, [[None, None], None], None]
# expected = []

# 3. Algorithm - steps for converting the input to the output

# 1. Create an empty one-dimensional array to hold the flattened elements.
# 2. Traverse the input array recursively, and for each element:
#    a. If the element is not an array and it is not equal to None, add it to the one-dimensional array.
#    b. If the element is an array, recursively traverse the array and repeat step 2 for each element.
# 3. Return the one-dimensional array.

#  4. Implementation

""" 
def flatten(arr):
    flat_arr = []
    for elem in arr:
        if isinstance(elem, list):
            flat_arr += flatten(elem)
        elif elem is not None:
            flat_arr.append(elem)
    return flat_arr """

# 5. Refactor


def flatten(arr):
    return [
        item
        for elem in arr
        for item in (flatten(elem) if isinstance(elem, list) else [elem])
        if elem is not None
    ]
