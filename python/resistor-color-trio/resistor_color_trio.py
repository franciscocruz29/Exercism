# 1. Understand the problem:

# What is the input?
# A list of three colors

# What is the output?
# A string with the resistance value in ohms

# What are the rules?
# - Each band color acts as a digit of a number.
# - The first two colors stand for the number.
# - The third color stands for how many zeros need to be added to the main value.
# - A metric prefix is used to indicate a larger magnitude of ohms.

# 2. Examples:

# Input: ["orange", "orange", "black"]
# Output: "33 ohms"

# Input: ["blue", "grey", "brown"],
# Output: "680 ohms"

# Input: ["orange", "orange", "orange"]
# Output: "33 kiloohms"

# Input: ["blue", "green", "yellow", "orange"])
# Output: "650 kiloohms"

# 3. Algorithm:

# 1. Define COLORS as a dictionary mapping color names to their corresponding numeric values representing digits.
# 2. Define UNITS as a list of strings representing units of resistance, in increasing order of magnitude.

# 3. Define a class Resistance with attributes value and unit to represent a resistance value.

# 4. Define a function to_resistance(x: float) -> Resistance that converts a given resistance value in raw form to a standardized Resistance object.
# a. Set the default unit to "ohms".
# b. Iterate through the UNITS list.
# i. If the value is greater than or equal to 1000, divide the value by 1000 and update the unit to the corresponding unit from UNITS.
# ii. Return a Resistance object with the standardized value and unit.

# 5. Define a function label(color_array: List[str]) -> str that calculates the resistance value from the given color bands and returns a formatted string representation of the resistance.
# a. Calculate the raw resistance value by combining the values of the first two colors and multiplying them by 10 raised to the power of the third color.
# b. Convert the raw resistance value to a standardized Resistance object using the to_resistance() function.
# c. Return a formatted string containing the value and unit of the resistance.


from typing import List

COLORS = {
    "black": 0, "brown": 1, "red": 2, "orange": 3,
    "yellow": 4, "green": 5, "blue": 6, "violet": 7,
    "grey": 8, "white": 9
}

UNITS = ["ohms", "kiloohms", "megaohms", "gigaohms"]


class Resistance:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit


def to_resistance(x: float) -> Resistance:
    unit = "ohms"
    for i in range(1, 4):
        if x >= 1000:
            x /= 1000
            unit = UNITS[i]

    if int(x) == x:
        x = int(x)

    return Resistance(x, unit)


def label(color_array: List[str]) -> str:

    raw = (COLORS[color_array[0]] * 10 + COLORS[color_array[1]]) * \
          (10 ** COLORS[color_array[2]])

    resistance = to_resistance(raw)

    return f"{resistance.value} {resistance.unit}"
