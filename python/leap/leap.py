# Step 1: Understand the problem

#     What are the inputs?
#         A postive integer that represents the year

#     What are the outputs?
#         A boolean; True if the year is leap, false if the year is not leap

#     What are the rules?
#         A leap year (in the Gregorian calendar) occurs:
#             The year must be divisible by 4.
#             If the year is divisible by 100, it must also be divisible by 400.

# Step 2: Examples

#     1997 was not a leap year as it's not divisible by 4
#     1900 was not a leap year as it's not divisible by 400

"""
    All the leap years since 1900 are as follows:
        
    1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020
"""

# Step 3: The algorithm

#     1. Check if the year is divisible by 4.
#         If not, the year is not a leap year.
#         If yes, proceed to the next step.

#     2. Check if the year is divisible by 100.
#         If yes, check if the year is also divisible by 400.
#             If yes, the year is a leap year.
#             If not, the year is not a leap year.
#        If no, the year is a leap year.

# Step 4: The implementation

"""
def leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
"""

# Step 5: The refactored version

def leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.

    :param year: A positive integer representing the year.
    :return: True if the year is a leap year, False otherwise.
    :raises ValueError: If the input is not a positive integer.
    """

    # Validate input
    if not isinstance(year, int) or year <= 0:
        raise ValueError("Input must be a positive integer representing the year")

    # Step 1: Check if the year is divisible by 4
    divisible_by_4: bool = year % 4 == 0

    # Step 2: Check if the year is divisible by 100 and 400 (if divisible by 100)
    divisible_by_100: bool = year % 100 == 0
    divisible_by_400: bool = year % 400 == 0

    # Conditions for a leap year
    if divisible_by_4 and (not divisible_by_100 or divisible_by_400):
        return True
    else:
        return False
