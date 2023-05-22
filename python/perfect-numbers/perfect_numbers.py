# 1. Understand the problem:

# What are the input?: a positive integer
# What are the output?: a string, the classification of the input integer, "perfect", "abundant", or "deficient"

# What are the requirements?:
#   The input integer must be positive
#   Determine if a number is perfect, abundant, or deficient based on Nicomachus classification scheme for positive integers.

# What are the rules?:
#   The aliquot sum is defined as the sum of the factors of a number not including the number itself
#   Perfect: The aliquot sum equals the number
#   Abundant: The aliquot sum is greater than the number
#   Deficient: The aliquot sum is less than the number

# 2. Examples:

# 6 is a perfect number because (1 + 2 + 3) = 6
# 24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
# 8 is a deficient number because (1 + 2 + 4) = 7 // Prime numbers are deficient

# 3. Algorithm:

#   1. Determine if the number is positive
#   2. Determine the aliquot sum
#    2.1 Find the factors of a positive integer excluding the number itself
#    2.2 Find the sum of the factors
#   3. Determine the classification of the number

# 4. Implementation:

# def get_factors(n):
#     return [i for i in range(1, n) if n % i == 0]

# def aliquot_sum(n):
#     return sum(get_factors(n))

# def classify(number):
#     """ A perfect number equals the sum of its positive divisors.

#     :param number: int a positive integer
#     :return: str the classification of the input integer
#     """
#     if number <= 0:
#         raise ValueError("Classification is only possible for positive integers.")

#     aliquot = aliquot_sum(number)
#     if aliquot == number:
#         return "perfect"
#     elif aliquot > number:
#         return "abundant"
#     else:
#         return "deficient"

# 5. Refactoring:

import math

""" The current implementation of the get_factors function is not very efficient because it checks every number up to n to see if it is a factor. 
We can improve this by only checking up to the square root of n, because any factor larger than the square root of n would have a corresponding factor smaller than the square root.

Also, we can calculate the aliquot sum directly in the classify function, without the need for the get_factors and aliquot_sum functions. 
This will reduce the number of function calls and improve performance. """

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")

    aliquot = 1
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            aliquot += i
            if i * i != number:
                aliquot += number // i

    if aliquot == number and number != 1:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
