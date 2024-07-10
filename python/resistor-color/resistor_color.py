# Step 1: Understand the problem
# What is the input?
# The input is a color name as a string.

# What is the output?
# The output is the numerical value associated with that color as an integer.

# What are the rules?
# The color names must be one of the predefined resistor colors.
# The function should return the corresponding number for the given color.
# There should be a way to list all the possible resistor colors.

# Step 2: Examples
# color_code('orange') => 3
# color_code('white') => 9
# color_code('black') => 0

# Step 3: Write the algorithm
# Define a list of colors where the index represents the numerical value of the color.
# Create a function `colors` that returns the list of colors.
# Create a function `color_code` that takes a color name as input and returns the index of that color in the list.

# Step 4: Implementation
from typing import List

# List of resistor colors in order
RESISTOR_COLORS: List[str] = [
    "black",  # 0
    "brown",  # 1
    "red",    # 2
    "orange", # 3
    "yellow", # 4
    "green",  # 5
    "blue",   # 6
    "violet", # 7
    "grey",   # 8
    "white"   # 9
]

def colors() -> List[str]:
    """
    Returns the list of resistor colors.

    :return: List of color names as strings.
    """
    return RESISTOR_COLORS

def color_code(color: str) -> int:
    """
    Returns the numerical value associated with a given resistor color.

    :param color: The color name as a string.
    :return: The numerical value corresponding to the color.
    :raises ValueError: If the color is not found in the resistor colors list.
    """
    if color not in RESISTOR_COLORS:
        raise ValueError(f"Invalid color '{color}'. Valid colors are: {', '.join(RESISTOR_COLORS)}")
    return RESISTOR_COLORS.index(color)
