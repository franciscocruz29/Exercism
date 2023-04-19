# 1. Understand the problem:

# What are the inputs? An integer

# What are the outputs? A string

# What are the rules?
# if a given number has 3 as a factor, add 'Pling' to the result.
# if a given number has 5 as a factor, add 'Plang' to the result.
# if a given number has 7 as a factor, add 'Plong' to the result.
# if a given number does not have 3, 5, or 7 as a factor, the result should be the digits of the number.

# Examples
# convert(1) -> '1'
# convert(6) -> 2 * 3 -> 'Pling'
# convert(14) -> 2 * 7 -> 'Plong'
# convert(15) -> 3 * 5 -> 'PlingPlang'
# convert(105) -> 3 * 5 * 7 -> 'PlingPlangPlong'

# The goal: to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.

# 2. steps for converting input to output

# 1. create a function that takes in an integer
# 2. create an empty string
# 3. check if the number has 3 as a factor. If so, add 'Pling' to the result.
# 4. check if the number has 5 as a factor. If so, add 'Plang' to the result.
# 5. check if the number has 7 as a factor. If so, add 'Plong' to the result.
# 6. if the number does not have 3, 5, or 7 as a factor, the result should be the digits of the number.
# 7. return the result

# 3. Implement the solution


""" def convert(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
        
    if number % 5 == 0: 
        result += "Plang"
        
    if number % 7 == 0:
        result += "Plong"
    
    if result == "":
        result = str(number)
        
    return result
 """
# 4. Refactor the solution

# This version uses a list of tuples to store the factors and their corresponding sounds.

def convert(number):
    result = ""
    factors = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

    for factor, sound in factors:
        if number % factor == 0:
            result += sound

    return result or str(number)
