# Step 1 - Understand the problem:

# What is the expected input?
# - Data type: string
# - Description: A string containing any combination of brackets [], braces {}, parentheses (), and potentially other characters.

# What is the expected output?
# - Data type: boolean
# - Description:
#   - True if all opening brackets, braces, and parentheses have corresponding closing counterparts in the correct order.
#   - False otherwise.

# What are the rules?
# - Matching:
#       - Brackets must be matched with their correct pair type: [] {} ()
#       - Brackets must be properly nested(e.g., "([)]" is invalid, "[([])]" is valid)
# - Other Characters: Ignore all non-bracket characters.
# - Empty Input: An empty string is considered balanced, so return True.

# What is the mental model?
# - Imagine keeping track of opening brackets using a stack. When encountering a closing bracket,
#   check if it correctly matches the most recent opening bracket in the stack.
#   If all brackets are matched and the stack is empty at the end, the string is balanced. Otherwise, it is not.

# Step 2 - Examples:

# Input: ""
# Output: True

# Input: "[]"
# Output: True

# Input: "[["
# Output: False

# Input: "[({}])"
# Output: False

# Input: "(((185 + 223.85) * 15) - 543)/2"
# Output: True

# Step 3 - Data structure selection:

# The stack data structure is the best choice for solving this problem. Here's why:

# 1. LIFO (Last-In-First-Out) Property:
#   - A stack operates on the principle of last-in, first-out, which matches the requirement of balancing brackets.
# 2. Efficient Push and Pop Operations:
#   - Checking and removing the top element(pop) or adding a new one(push) is an O(1) operation. This ensures the algorithm processes each character in the string efficiently.
# 3. Tracking Open Brackets:
#   - As you iterate through the string, opening brackets([, {, () are pushed onto the stack.
#   - When encountering a closing bracket (], }, )), you check if it matches the bracket at the top of the stack. If so, pop the top element. If not, the string is unbalanced.
# 4. Validation:
#   - At the end of the traversal, the stack should be empty if all brackets were matched and nested correctly. If not, it indicates an imbalance.

# Step 4 - Algorithm design:

# 1. Initialization:
#   - Create an empty stack to store opening brackets.
#   - Create a dictionary to map opening brackets to their corresponding closing brackets. { '(': ')', '{': '}', '[': ']' }
# 2. Iterate thorugh the input string:
#   - For each character in the string:
#       - Case 1: Opening Bracket:
#           - If the character is an opening bracket, push it onto the stack.
#       - Case 2: Closing Bracket:
#           - If the character is a closing bracket:
#               - Check for Empty Stack: If the stack is empty, the string is unbalanced (return False).
#               - Pop Opening Bracket: Pop the top element from the stack. This should be the corresponding opening bracket.
#               - Match Check:
#                   - Check if the popped opening bracket and the current closing bracket form a valid pair using the dictionary.
#                   - If they don't match, the string is unbalanced(return False).
# 3. Final Check:
#   - After processing all characters, if the stack is empty, return True (balanced). Otherwise, return False (unbalanced).

# Step 5 - Implementation:

def is_paired(input_string: str) -> bool:
    """
    Check if all brackets in the input string are properly paired and nested.

    Args:
        input_string (str): The string containing brackets and other characters.

    Returns:
        bool: True if brackets are balanced, False otherwise.
    """
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in input_string:
        if char in matching_brackets.values():  # If it's an opening bracket
            stack.append(char)
        elif char in matching_brackets:  # If it's a closing bracket
            if not stack:  # No matching opening bracket
                return False
            if stack.pop() != matching_brackets[char]:  # Check for a match
                return False

    return len(stack) == 0
