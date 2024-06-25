# 1. Understand the problem:

# What is the input?
# A list of 1, 4, or 5 colors

# What is the output?
# A string with the resistance value in multiple units and the tolerance in percentage

# What are the rules?
# - Each band color acts as a digit of a number.
# - The first two colors stand for the value of the resistor.
# - There are one band resistors. One band resistors only have the color black with a value of 0.
# - The four-band resistor is built up like this: Value_1 Value_2 Multiplier Tolerance
# - The five-band resistor is built up like this: Value_1 Value_2 Value_3 Multiplier Tolerance
# - When there are more than a thousand ohms, we say "kiloohms"
# - When there are more than a million ohms, we say "megaohms"

# - The color bands are encoded as follows:
#   - black: 0
#   - brown: 1
#   - red: 2
#   - orange: 3
#   - yellow: 4
#   - green: 5
#   - blue: 6
#   - violet: 7
#   - grey: 8
#   - white: 9

# - The tolerance band will have one of these values:
#   - Grey - 0.05%
#   - Violet - 0.1%
#   - Blue - 0.25%
#   - Green - 0.5%
#   - Brown - 1%
#   - Red - 2%
#   - Gold - 5%
#   - Silver - 10%


# 2. Examples:

# Input: ["black"]
# Output: "0 ohms"

# Input: ["orange", "orange", "black", "green"]
# Output: "33 ohms ±0.5%"

# Input: ["orange", "orange", "brown", "green"]
# Output: "330 ohms ±0.5%"

# Input: ["orange", "orange", "orange", "grey"]
# Output: "33 kiloohms ±0.05%"

# Input: ["orange", "orange", "blue", "red"]
# Output: "33 megaohms ±2%"

# Input: ["orange", "orange", "orange", "black", "green"]
# Output: "333 ohms ±0.5%"

# Input: ["orange", "red", "orange", "blue", "violet"]
# Output: "323 megaohms ±0.10%"

# 3. Algorithm:

# 3.1 Define Constants: Create dictionaries to map color names to their corresponding digit values, multipliers, and tolerances
# 3.2 Calculate Resistance:
#     3.2.1 If there are four colors:
#           Extract the first two colors, convert them to their digit values, and combine them to form a number.
#           Multiply this number by the value of the third color(which acts as a multiplier).
#     3.2.2 If there are five colors:
#           Extract the first three colors, convert them to their digit values, and combine them to form a number.
#           Multiply this number by the value of the fourth color(which acts as a multiplier).
# 3.3 Determine Unit:
#     3.3.1 Check if the resistance is greater than or equal to 1, 000, 000 (use "megaohms").
#     3.3.2 Check if the resistance is greater than or equal to 1, 000 (use "kiloohms").
#     Otherwise, use "ohms".
# 3.4 Format Resistance:
#     Format the resistance value to have no more than two decimal places, and remove any trailing zeros after the decimal point.
# 3.5 Generate Output:
#     3.5.1 For a single black band, return "0 ohms".
#     3.5.2 For valid inputs(4 or 5 bands), combine the formatted resistance value, its unit, and the tolerance(determined by the last color band) into a readable string.
#     Return "Invalid input" for invalid inputs.

# 4. Implementation:

from typing import List, Dict, Union, Tuple

# Constants
COLOR_TO_DIGIT: Dict[str, int] = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
}

MULTIPLIER: Dict[str, int] = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "violet": 10000000, "grey": 100000000, "white": 1000000000
}

TOLERANCE: Dict[str, str] = {
    "grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%",
    "brown": "1%", "red": "2%", "gold": "5%", "silver": "10%"
}


def calculate_resistance(colors: List[str]) -> Union[int, str]:
    """Calculate the resistance value based on color bands."""
    if len(colors) == 4:
        digit1 = COLOR_TO_DIGIT[colors[0]]
        digit2 = COLOR_TO_DIGIT[colors[1]]
        multiplier = MULTIPLIER[colors[2]]
        value = (digit1 * 10 + digit2) * multiplier
    elif len(colors) == 5:
        digit1 = COLOR_TO_DIGIT[colors[0]]
        digit2 = COLOR_TO_DIGIT[colors[1]]
        digit3 = COLOR_TO_DIGIT[colors[2]]
        multiplier = MULTIPLIER[colors[3]]
        value = (digit1 * 100 + digit2 * 10 + digit3) * multiplier
    else:
        return "Invalid input"

    return value


def determine_unit(resistance: int) -> Tuple[float, str]:
    """Determine the appropriate unit for the resistance value."""
    if resistance >= 1_000_000:
        return resistance / 1_000_000, "megaohms"
    elif resistance >= 1_000:
        return resistance / 1_000, "kiloohms"
    else:
        return resistance, "ohms"


def format_resistance(resistance: float) -> str:
    """Format the resistance value with appropriate precision."""
    if resistance >= 100:
        return f"{resistance:.0f}"
    elif resistance >= 10:
        return f"{resistance:.1f}".rstrip('0').rstrip('.')
    else:
        return f"{resistance:.2f}".rstrip('0').rstrip('.')


def resistor_label(colors: List[str]) -> str:
    """Decode resistor color bands and return formatted resistance value."""
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    if len(colors) not in (4, 5):
        return "Invalid input"

    resistance = calculate_resistance(colors)

    resistance_value, unit = determine_unit(resistance)
    formatted_resistance = format_resistance(resistance_value)
    tolerance = TOLERANCE[colors[-1]]

    return f"{formatted_resistance} {unit} ±{tolerance}"
