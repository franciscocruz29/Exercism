# Step 1. Understand the problem:

# What is the input?
# - An array of color names (strings) representing the resistor bands

# What is the output?
# - A two-digit number representing the resistance value

# What are the rules?
# - Each color corresponds to a specific digit (black: 0, brown: 1, red: 2, etc.).
# - Only the first two colors are used to calculate the output value.
# - The output is formed by concatenating the digits of the first and second color bands.

# What is the mental model?
# - The mental model is to map the first and second color names to their respective digits and then combine these digits to form a two-digit number representing the resistor's value.


# Step 2. Examples:

# Input: ['brown', 'black']
# Output: 10

# Input: ['orange', 'orange'])
# Output: 33

# Input: ['green', 'brown', 'orange']
# Output: 51


# Step 3. Write the algorithm - steps for converting the input to output

# 1. Define a dictionary with the color names as keys and their corresponding numeric values as values.
# 2. Take the first two colors from the input array.
# 3. Find the value of the first color from the dictionary and multiply it by 10.
# 4. Find the value of the second color from the dictionary.
# 5. Add the two numeric values to form the final two-digit number.


# Step 4. Implementation
COLORS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def value(colors):
    return COLORS[colors[0]] * 10 + COLORS[colors[1]]
