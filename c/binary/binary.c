// Step 1: Understand the problem

// What is the input?
// - A string representing a binary number

// What is the output?
// - An integer representing the decimal value of the binary number.

// What are the rules?
// - Do not use built-in functions or libraries that directly perform binary to decimal conversion
// - The input is always a string. The function should return a specific value or error message for invalid input.

// What is the mental model?
// - Given a binary input string, the function should produce a decimal output
// https: www.geeksforgeeks.org/wp-content/uploads/binary2decimal.png

// Step 2: Examples

// Input: "0"
// Output: 0

// Input: "101" => 1*2^2 + 0*2^1 + 1*2^0 => 1*4 + 0*2 + 1*1 => 4 + 1 => 5 base 10
// Output: 5

// Input: "10001101000"
// Output: 1128

// Input: "01201"
// Output: -1

// Input: "001 nope"
// Output: -1

// Step 3: What are the steps for converting the input to output?

// 1. Initialize variables:
//    * Start with a variable called decimal_value and set it to 0. This will hold the decimal value of the binary number.
//    * Set a variable position to 0 to track the power of 2.
// 2. Iterate through the binary string:
//    * Start from the rightmost character of the binary string and move leftward (reverse the string for easier traversal).
//    * For each character:
//      - Check if it`s a valid binary digit('0' or '1'):
//        - If not, return -1 to indicate invalid input
//      - Convert the binary digit to its decimal value:
//        - Multiply the digit by 2 raised to the power of position
//        - Add this value to decimal value
//      - Increment position by 1 for the next digit
// 3. Return the result

// Step 4: Implementation
#include "binary.h"
#include <string.h>
#include <ctype.h>

// Helper function to check if the input is a valid binary string
static int is_valid_binary(const char *binary)
{
  for (int i = 0; binary[i] != '\0'; i++)
  {
    if (binary[i] != '0' && binary[i] != '1')
    {
      return 0; // Invalid binary string
    }
  }
  return 1; // Valid binary string
}

// Function to convert binary string to decimal
int convert(const char *binary)
{
  if (!is_valid_binary(binary))
  {
    return INVALID;
  }

  int decimal_value = 0;
  int position = 0;
  int length = strlen(binary);

  for (int i = length - 1; i >= 0; i--)
  {
    if (binary[i] == '1')
    {
      decimal_value += 1 << position; // Equivalent to 1 * 2^position
    }
    position++;
  }

  return decimal_value;
}
