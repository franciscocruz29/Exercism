# 1. Understand the problem:

    # What is the input?
        # A string that contains a simple math word problem

    # What is the output?
        # A integer that represents the answer to the math problem
        
    # What are the rules?
        # 1. Problems with no operations simply evaluate to the number given.
        
        # 2. Addition, Subtraction, Multiplication and Division
            # They have the following structure: "What is X operation Y?"
            # Where X is the first number, Y is the second number, and operation is the operation to be performed.
            
        # 3. Multiple Operations:
            # Handle a set of operations, in sequence.
            # Since these are verbal word problems, evaluate the expression from left-to-right, ignoring the typical order of operations.
            
        # 4. The parser should reject:
            # Unsupported operations ("What is 52 cubed?")
            # Non-math questions ("Who is the President of the United States")
            # Word problems with invalid syntax ("What is 1 plus plus 2?")
            
            # This exercise requires that you use the raise statement to "throw" a ValueError if the question passed to answer() is malformed/invalid, 
            # or contains an unknown operation. The tests will only pass if you both raise the exception and include a message with it.

# 2. Test cases and examples:

# Rule 1:
    # Input: "What is 5?"
    # Output: 5
    
# Rule 2:
    # Input: "What is 5 plus 5?"
    # Output: 10
    
    # Input: "What is 4 minus -12?"
    # Output: 16
    
    # Input: "What is -3 multiplied by 25?"
    # Output: -75
    
    # Input: "What is 33 divided by -3?"
    # Output: -11
    
# Rule 3:
    # Input: "What is 1 plus 1 plus 1?"
    # Output: 3
    
    # Input: "What is 2 multiplied by -2 multiplied by 3?"
    # Output: -12
    
    # Input: "What is -3 plus 7 multiplied by -2?"
    # Output: -8
    
# Rule 4:
    # Input: "What is 52 cubed?"
    # Output: ValueError("unknown operation")
    
    # Input: "What is?"
    # Output: ValueError("syntax error")
    
    # Input: "What is 1 plus plus 2?"
    # Output: ValueError("syntax error")

# 3. Algorithm:

# 1. Preprocess the input string

    # Remove the unnecessary words like "What is" and replace the word equivalents of math operations with the actual operators (+, -, *, /).
    # Remove any trailing question mark and split the string into a list of words.

# 2. Check for syntax errors or unknown operations

    # Check if the question list is empty, which indicates a syntax error (Rule 4).
    # Try to convert the last element of the question list into an integer. If it fails, check if it's a valid operation. If not, raise a ValueError for unknown operations (Rule 4).
    # Check if the first element of the question list can be converted to an integer. If it fails, raise a ValueError for syntax errors (Rule 4).

# 3. Perform the calculations

    # Iterate through the question list.
    # Check for adjacent elements that are both digits, which indicates a syntax error (Rule 3).
    # Perform the calculations based on the operators (+, -, *, /) in the question list and update the result r.
    # If any error occurs during the calculation, raise a ValueError for syntax errors (Rule 4).

# 4. Return the final result
    # The function returns the final result, which is the answer to the math word problem.

# 4. Implementation:

def answer(question):
    # Preprocess the input string
    question = question.replace("What is", "").replace("?", "").lower()
    question = question.replace("plus", "+").replace("minus", "-")
    question = question.replace("multiplied by", "*").replace("divided by", "/")
    question_list = question.split()

    # Check for syntax errors or unknown operations
    if not question_list:
        raise ValueError("syntax error")
    
    try:
        last_element = question_list[-1]
        last_element = int(last_element)
    except ValueError:
        if last_element not in ['+', '-', '*', '/']:
            raise ValueError("unknown operation")
        else:
            raise ValueError("syntax error")  # Missing operand after operator

    try:
        int(question_list[0])
    except ValueError:
        raise ValueError("syntax error")

    # Perform the calculations
    result = int(question_list[0])
    operator = None  # Track the current operator
    for token in question_list[1:]:
        if token in ['+', '-', '*', '/']:
            if operator is not None:
                raise ValueError("syntax error")  # Reject two operators in a row
            operator = token
        else:
            if operator is None:
                raise ValueError("syntax error")  # Reject missing operator
            try:
                operand = int(token)
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "*":
                    result *= operand
                elif operator == "/":
                    result //= operand
                operator = None  # Reset operator after using it
            except ValueError:
                raise ValueError("syntax error")
    
    return result
