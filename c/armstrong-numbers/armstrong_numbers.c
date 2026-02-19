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

// Step 2 - Examples/Test Cases
//
// Input: 0
// Output: true
// Reason: 0 = 0^1 = 0
//
// Input: 9
// Output: true
// Reason: 9 = 9^1 = 9
//
// Input: 153
// Output: true
// Reason: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
//
// Input: 154
// Output: false
// Reason: 154 = 1^3 + 5^3 + 4^3 = 190
//
// Input: 9926315
// Output: true
// Reason: 9926315 = 9^7 + 9^7 + 2^7 + 6^7 + 3^7 + 1^7 + 5^7 = 9926315
//
// Input: -153
// Output: false
// Reason: Negative numbers are not Armstrong numbers.

// Step 3 - Data Structure
//
// I will keep everything as integers and use simple variables to hold intermediate values.
// No complex data structures (arrays, hashes, strings) are needed.
//
// * Approach: Mathematical digit extraction (no arrays or strings)
//   - The number remains an integer throughout processing.
//   - Digits are handled individually using arithmetic.
//   - Each digit contributes to an accumulated integer sum.
//   - The final sum (integer) is compared to the original integer, producing a boolean result.

// Step 4 - Algorithm Design:
//
// 1. If the input number is 0:
//      - Return true
// 2. Store the input number in originalNumber
// 3. Count digits (FIRST LOOP):
//      - Set copy to originalNumber
//      - Initialize digitCount to 0
//      - While copy > 0:
//            - Increment digitCount by 1
//            - Integer divide copy by 10
// 4. Compute powered sum (SECOND LOOP):
//      - Set copy to originalNumber
//      - Initialize sum to 0
//      - While copy > 0:
//            - Extract digit = copy % 10
//            - Compute poweredDigit = digit raised to digitCount
//            - Add poweredDigit to sum
//            - Integer divide copy by 10
// 5. Return whether sum == originalNumber

// Step 5: Implementation
//
#include "armstrong_numbers.h"
#include <stdbool.h>

bool is_armstrong_number(int candidate) {
    if (candidate == 0) {
        return true;
    }
    int originalNumber = candidate;
    int digitCount = 0;
    int copy = originalNumber;
    while (copy > 0) {
        digitCount++;
        copy /= 10;
    }
    copy = originalNumber;
    int sum = 0;
    while (copy > 0) {
        int digit = copy % 10;
        int poweredDigit = 1;
        for (int i = 0; i < digitCount; i++) {
            poweredDigit *= digit;
        }
        sum += poweredDigit;
        copy /= 10;
    }
    return sum == originalNumber;
}
