# 1. Understand the problem:

# What is the input?
    # A binary string that represents a number in base 10 ranging from 1 to 31.

# What is the output?
    # A sequential actions comprising the secret handshake, presented in the form of a list of strings.
    
# What are the rules?
    # The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary. 
    # Start at the right-most digit and move left.

    # The actions for each number place are:

    # 00001 = wink
    # 00010 = double blink
    # 00100 = close your eyes
    # 01000 = jump
    # 10000 = Reverse the order of the operations in the secret handshake.

# 2. Examples:

# 9 in binary is 1001.

# The digit that is farthest to the right is 1, so the first action is wink.
# Going left, the next digit is 0, so there is no double-blink.
# Going left again, the next digit is 0, so you leave your eyes open.
# Going left again, the next digit is 1, so you jump.

# That was the last digit, so the final code is:
# ["wink", "jump"]


# Given the number 26, which is 11010 in binary, we get the following actions:

# double blink
# jump
# reverse actions

# That was the last digit, so the final code is:
# ["jump", "double blink"]

# 3. Algorithm:
    # 1. Create a empty list to store the actions
    # 2. Check the rightmost digit of the binary string. If it is '1', append the string "wink" to the actions list.
    # 3. Check the second rightmost digit of the binary string. If it is '1', append the string "double blink" to the actions list.
    # 4. Check the third rightmost digit of the binary string. If it is '1', append the string "close your eyes" to the actions list.
    # 5. Check the fourth rightmost digit of the binary string. If it is '1', append the string "jump" to the actions list.
    # 6. Check the leftmost digit of the binary string. If it is '1', reverse the order of the elements in the actions list using the reverse() method.
    # 7. Return the actions list.


""" def commands(binary_str):
    actions = []
    
    if binary_str[-1] == "1":
        actions.append("wink")
    if binary_str[-2] == "1":
        actions.append("double blink")
    if binary_str[-3] == "1":
        actions.append("close your eyes")
    if binary_str[-4] == "1":
        actions.append("jump")
    if binary_str[-5] == "1":    
        actions.reverse()
        
    return actions """

# 4. Refactoring:

from typing import List

def commands(binary_str: str) -> List[str]:
    """
    Generate a secret handshake sequence based on a binary string.

    Args:
        binary_str: The binary string representing a number.

    Returns:
        A list of strings representing the secret handshake actions.

    Example:
        >>> commands('11010')
        ['jump', 'double blink']
    """

    actions = []

    action_mapping = {
        '1': "wink",
        '2': "double blink",
        '3': "close your eyes",
        '4': "jump"
    }

    for i, digit in enumerate(binary_str[::-1]):
        if i == 4 and digit == '1':
            actions.reverse()
        elif i < 4 and digit == '1':
            actions.append(action_mapping[str(i + 1)])

    return actions
