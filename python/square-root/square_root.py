# Step 1 - Problem Understanding:
#
# - What are the expected inputs?
#   - Data type: An integer
#   - Description: A positive integer called a "radicand".
#
# - What are the expected outputs?
#   - Data type: An integer
#   - Description: The square root of the input number, which is also an integer (the exact square root without decimals)
#
# - What are the key rules or constraints?
#   - No built-in functions or modules can be used.
#   - You need to calculate the square root manually using a custom algorithm.
#   - The square root should be exact (integer).
#
# - What is the mental model?
#   - Given a positive integer, find another positive integer that, when multiplied by itself, equals the original integer.

# Step 2 - Examples:
#
# Input: 1
# Output: 1
#
# Input: 25
# Output: 5
#
# Input: 65025
# Output: 255

# Step 3 - Algorithm Design:
#
# Step 1: Identify the range of possible square roots.
#   - The square root of a number n must lie between 1 and n itself. You can narrow this down using a range-based approach.
# Step 2: Use Binary Search to optimize the square root calculation.

# Step 4 - Implementation:

def square_root(radicand: int) -> int:
    """Calculate the exact square root of a perfect square using binary search.

    Args:
        radicand: A positive perfect square integer.

    Returns:
        The exact square root of the input.

    Raises:
        ValueError: If the input is not a positive integer or not a perfect square.
    """
    if not isinstance(radicand, int) or radicand < 1:
        raise ValueError("Input must be a positive integer")

    if radicand == 1:
        return 1

    start, end = 1, radicand // 2 + 1

    while start <= end:
        candidate = (start + end) // 2
        candidate_squared = candidate * candidate

        if candidate_squared == radicand:
            return candidate
        elif candidate_squared < radicand:
            start = candidate + 1
        else:
            end = candidate - 1

    raise ValueError("Input must be a perfect square")
