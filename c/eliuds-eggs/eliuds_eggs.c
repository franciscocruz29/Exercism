// Step 1: Understand the problem

// What is the input?
// - An integer representing the position information shown on the digital display, which represents a binary encoding of the chicken coop's egg-laying spots.

// What is the output?
// - An integer representing the actual number of eggs present in the coop, which corresponds to the count of 1's in the binary representation of the input number.

// What are the rules?
// - Each bit in the binary number represents whether an egg is present (1 for egg, 0 for no egg).
// - Keep your hands off that bit-count functionality provided by your standard library! Solve this one yourself using other basic tools instead.

// What is the mental model?
// - The problem involves interpreting a decimal number as a binary sequence where each bit indicates whether an egg is present in a specific spot.
// - The task is to convert the decimal number to its binary form, and then count how many 1's appear in that binary representation to determine the number of eggs.

// Step 2: Examples

// Input: 0
// Output: 0

// Input: 16
// Output: 1

// Input: 89
// Output: 4

// Input: 2000000000
// Output: 13

// Step 3: Steps for converting the input to output

// 1. Start by setting a counter to zero. This counter will keep track of how many 1s are in the binary representation of the number.
// 2. While the number is greater than zero:
//   - The least significant bit of a number can be obtained by checking number % 2. If number % 2 == 1, it means the current least significant bit is 1 (there is an egg).
//   - If the result of number % 2 is 1, increment the egg counter by 1.
//   - Perform an integer division by 2 (i.e., number = number // 2), which shifts the number to the right, effectively removing the LSB.
// 3. Return the counter as the final output.

#include "eliuds_eggs.h"

int egg_count(int number)
{
  int count = 0;

  while (number > 0)
  {
    if (number % 2 == 1)
    {
      count++;
    }
    number = number / 2;
  }

  return count;
}
