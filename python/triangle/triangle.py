# 1. Understand the problem:

# What is the input?
# An array of three integers that represent the lengths of the sides of a triangle

# What is the output?
# True if a triangle is equilateral, isosceles, or scalene otherwise False

# What are the rules?
# A triangle is equilateral if all three sides are equal
# A triangle is isosceles if two sides are equal
# A triangle is scalene if all three sides are different
# For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side:
# a + b ≥ c
# b + c ≥ a
# a + c ≥ b

# 2. Examples:

# Input: equilateral([2, 2, 2])
# Output: True

# Input: equilateral([0, 0, 0])
# Output: False

# Input: isosceles([4, 4, 3])
# Output: True

# Input: isosceles([3, 1, 1])
# Output:False

# Input: scalene([5, 4, 6])
# Output: True

# Input: scalene([7, 3, 2])
# Output: False

# 3. Algorithm:

# 1. Write a function to check if the given sides can form a triangle:
#   1.1 Unpack the sides from the input list
#   1.2 Check if the sum of any two sides is greater than or equal to the length of the third side
#   1.3 If the condition is true, return True, otherwise return False

# 2. Write a function to check if the triangle is equilateral
#   2.1 Unpack the sides from the input list
#   2.2 Check if the sides can form a triangle and if all the sides are equal (using the set() function)

# 3. Write a function to check if the triangle is isosceles
#   3.1 Unpack the sides from the input list
#   3.2 Check if the sides can form a triangle and if at most two sides are equal (using the set() function)

# 4. Write a function to check if the triangle is scalene
#   4.1 Unpack the sides from the input list
#   4.2 Check if the sides can form a triangle and if all the sides are different (using the set() function)

# 4. Implementation:

""" def is_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


def equilateral(sides):
    x, y, z = sides[0], sides[1], sides[2]
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    x, y, z = sides[0], sides[1], sides[2]
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    x, y, z = sides[0], sides[1], sides[2]
    return is_triangle(sides) and len(set(sides)) == 3 """

# 5. Refactoring:

""" A decorator is a special function that takes another function as an argument and extends or alters its behavior without modifying it directly. 
By using the decorator, the code separates the concern of validating the triangle from the logic of determining its type. This makes the code cleaner and easier to maintain. 
The decorator allows for reusability and modularity. The validation logic is written once and applied to multiple functions without duplicating code. """


def valid_triangle(f):
    def inner(sides):
        return sum(sides) > 2 * max(sides) and f(sides)
    return inner


@valid_triangle
def equilateral(sides):
    return len(set(sides)) == 1


@valid_triangle
def isosceles(sides):
    return len(set(sides)) < 3


@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3
