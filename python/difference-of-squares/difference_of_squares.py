def square_of_sum(number):
    """Return the square of the sum of the first n natural numbers."""
    sum_of_natural_numbers = number * (number + 1) // 2
    squared_sum = sum_of_natural_numbers ** 2
    return squared_sum


def sum_of_squares(number):
    """Return the sum of the squares of the first n natural numbers."""
    square_of_natural_numbers = [n ** 2 for n in range(1, number + 1)]
    sum_of_squares = sum(square_of_natural_numbers)
    return sum_of_squares


def difference_of_squares(number):
    """Return the difference between the square of the sum and the sum of the squares of the first n natural numbers."""
    return square_of_sum(number) - sum_of_squares(number)
