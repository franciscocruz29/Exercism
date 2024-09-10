# Step 1: Understand the problem

# What are the inputs?
# - An integer

# What are the outputs?
# - A string that represents the raindrop sounds

# What are the rules?
# - if a given number has 3 as a factor, add 'Pling' to the result.
# - if a given number has 5 as a factor, add 'Plang' to the result.
# - if a given number has 7 as a factor, add 'Plong' to the result.
# - if a given number does not have 3, 5, or 7 as a factor, the result should be the number as a string.

# What is the mental model?
# - The task is to convert a number into a string containing specific raindrop sounds depending on whether it has 3, 5, or 7 as factors. If none of these conditions apply, the output is simply the number as a string.

# Step 2:Examples

# Input: 1
# Output: '1'
# (Edge case: No factors of 3, 5, or 7)

# Input: 6
# Output: 'Pling'
# (Divisible by 3, but not by 5 or 7)

# Input: 14
# Output: 'Plong'
# (Divisible by 7, but not by 3 or 5)

# Input: 15
# Output: 'PlingPlang'
# (Divisible by 3 and 5, but not by 7)

# Input: 105
# Output: 'PlingPlangPlong'
# (Divisible by 3, 5, and 7)


# Step 3: Algorithm design

# 1. Initialize an empty string result to accumulate the sounds.
# 2. Define a list of tuples factors where each tuple contains a factor (3, 5, or 7) and its corresponding sound ("Pling", "Plang", or "Plong").
# 3. Iterate through the factors list:
#    - For each factor and sound tuple:
#      - If the input number is divisible by the factor, append the sound to the result.
# 4. If the result string is still empty (meaning no factors were found), set result to the string representation of the input number.
# 5. Return the result.

# Step 4: Implementation

# def convert(number: int) -> str:
#     result = ""
#     factors = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

#     for factor, sound in factors:
#         if number % factor == 0:
#             result += sound

#     return result or str(number)

# Step 5: Refactoring solution
def convert(number: int) -> str:
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    factors_sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = "".join(sound for factor,
                     sound in factors_sounds if number % factor == 0)

    return result or str(number)
