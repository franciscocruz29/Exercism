// Step 1 - Problem Understanding:
//
// * What are the expected inputs? (Data type, Description)
//   - Input: A non-negative integer
//
// * What are the expected outputs? (Data type, Description)
//   - Output: A boolean (true if Armstrong number, false otherwise)
//
// * Explicit requirements: What is clearly stated?
//   - Determine if the given number equals the sum of its own digits each raised to the power of the number of digits.
//
// * Implicit requirements: What is implied through examples or logic?
//   - Examples show that single-digit numbers (e.g., 9) are Armstrong numbers.
//   - Assume non-negative integers unless otherwise specified
//
// * Problem domain: Define any domain-specific terms or concepts
//   - An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
//
// * Clarifying questions: What needs confirmation or is ambiguous?
//   - How should invalid input types be handled (if applicable)?
//   - Is there a maximum number size we need to consider?
//
// * What is the mental model?
//   - Take a number → determine how many digits it has →
//     raise each digit to that count → sum the results →
//     compare the sum to the original number → return true or false.


#include "armstrong_numbers.h"
