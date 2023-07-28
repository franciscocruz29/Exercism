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
    # The function returns the final result r, which is the answer to the math word problem.

# 4. Implementation:

def answer(question):
    question=question.replace("What is","")
    question=question.replace("plus","+")
    question=question.replace("minus","-")
    question=question.replace("multiplied by","*")
    question=question.replace("divided by","/")
    question=question.replace("?","")
    question=question.split()
    
    if question == []:
        raise ValueError("syntax error")
    try:
        int(question[-1])
    except:
        if question[-1] not in ("+","-","/","*"):
            raise ValueError("unknown operation")
        if question == "":
            raise ValueError("syntax error")
    try:
        r = int(question[0])
    except:
        raise ValueError("syntax error")
    for i in range(0,len(question),1):
        try:
            if question[i].isdigit() and question[i+1].isdigit():
            
                raise ValueError("syntax error")
        except IndexError:
            continue
        
        if question[i] == "+":
            try:
                r+=int(question[i+1])
            except:
                raise ValueError("syntax error")
        if question[i] == "-":
            try:
                r -= int(question[i+1])
            except:
                raise ValueError("syntax error")
        if question[i] == "*":
            try:
                r*= int(question[i+1])
            except:
                raise ValueError("syntax error")
        if question[i] == "/":
            try:
                r/=int(question[i+1])
            except:
                raise ValueError("syntax error")
    
    return(r)
