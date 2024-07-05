/* Step 1: Understand the problem.

What is the input?
A positive number

What is the output?
A positive number and zero

What are the rules?
- The square of the sum of the first N natural numbers is (1 + 2 + ... + N)² = N²(N+1)²/4
- The sum of the squares of the first N natural numbers is 1² + 2² + ... + N² = N(N+1)(2N+1)/6

What is the goal?
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

*/

/* Step 2: Examples

The square of the sum of the first two natural numbers is (1 + 2)² = 9
The sum of the squares of the first two natural numbers is 1² + 2² = 5

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first two natural numbers is 9 - 5 = 4


The square of the sum of the first three natural numbers is (1 + 2 + 3)² = 36
The sum of the squares of the first two natural numbers is 1² + 2² + 3² = 14

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first two natural numbers is 36 - 14 = 22

*/

/* Step 3: Write the algorithm

1. Start by getting the input value N, which is a positive number.

2. Calculate the square of the sum of the first N natural numbers:
   - First, find the sum of the first N natural numbers using the formula: Sum = N * (N + 1) / 2
   - Then, square this sum to get: Square of Sum = (Sum)^2

3. Calculate the sum of the squares of the first N natural numbers:
   - Use the formula: Sum of Squares = N * (N + 1) * (2N + 1) / 6

4. Find the difference between the square of the sum and the sum of the squares:
   - Difference = Square of Sum - Sum of Squares

5. Return or print the resulting difference.
*/

/* Step 4: Write the code */
#include "difference_of_squares.h"

// Function to calculate the square of the sum of the first N natural numbers
unsigned int square_of_sum(unsigned int number)
{
  unsigned int sum_of_natural_numbers = number * (number + 1) / 2;
  unsigned int squared_sum = sum_of_natural_numbers * sum_of_natural_numbers;
  return squared_sum;
}

// Function to calculate the sum of the squares of the first N natural numbers
unsigned int sum_of_squares(unsigned int number)
{
  unsigned int sum_squares = number * (number + 1) * (2 * number + 1) / 6;
  return sum_squares;
}

// Function to calculate the difference between the square of the sum and the sum of the squares
unsigned int difference_of_squares(unsigned int number)
{
  return square_of_sum(number) - sum_of_squares(number);
}
