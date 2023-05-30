# 1. Understand the problem:

# What is the input? A datetime object (year, month, day, hour, minute, second)
# What is the output? A datetime object (year, month, day, hour, minute, second)

# What is the requirement? 
# Determine the date and time one gigasecond after the input date.
# A gigasecond is one thousand million seconds

# 2. Examples:

# Input: datetime(2015, 1, 24, 22, 0)
# Output: datetime(2046, 10, 2, 23, 46, 40)

# Input: datetime(1977, 6, 13, 0, 0)
# Output: datetime(2009, 2, 19, 1, 46, 40)

# 3. The algorithm:
#   1. Define a function that takes in a datetime object
#   2. Add a gigasecond to the datetime object
#   3. Return the datetime object

# 4. Implementation:
""" 
from datetime import timedelta
def add(moment):
    return moment + timedelta(seconds=10**9) """

# 5. Refactoring:

from datetime import datetime, timedelta

GIGASECOND = timedelta(seconds=10**9)

def add(moment: datetime) -> datetime:
    return moment + GIGASECOND

