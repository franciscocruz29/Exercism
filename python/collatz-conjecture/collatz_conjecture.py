# Step 1: Understand the problem:
    # What is the input?
    # A number n >= 1

    # What is the output?
    # The number of steps required to reach 1

    # What are the rules?
    # Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely.
    # The conjecture states that no matter which number you start with, you will always reach 1 eventually.
    # If n is not a positive integer, stop the program from being executed further and return an error message.

# Step 2: Examples:
    # Starting witn n = 4, the steps would be as follows: 4, 2, 1. So for input n = 4, the return value would be 2.
    # Starting with n = 6, the steps would be as follows: 6, 3, 10, 5, 16, 8, 4, 2, 1. So for input n = 6, the return value would be 8.
    # Starting with n = 12, the steps would be as follows: 12, 6, 3, 10, 5, 16, 8, 4, 2, 1. So for input n = 12, the return value would be 9.

# Step 3: Algorithm:
    # 1. Check if the input number is positive. If not, raise a ValueError.
    # 2. If the number is 1, return 0 (no steps needed).
    # 3. If the number is even, divide it by 2.
    # 4. If the number is odd, multiply it by 3 and add 1.
    # 5. Recursively call the function with the new number.
    # 6. Add 1 to the result of the recursive call to count the current step.
    # 7. Return the total number of steps.

# Step 4: Implementation
"""
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return 0

    if number % 2 == 0:
        number = number / 2
    else:
        number = 3 * number + 1

    return 1 + steps(number)
"""

# Step 5: Refactoring

def steps(n: int) -> int:
    """
    Count the number of steps to reach 1 using the Collatz conjecture.

    Args:
        n (int): The starting positive integer.

    Returns:
        int: The number of steps to reach 1.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Only positive integers are allowed")

    if n == 1:
        return 0

    next_n = n // 2 if n % 2 == 0 else 3 * n + 1

    return 1 + steps(next_n)
