// Step 1 - Problem Understanding:

// What are the input?
// A single positive integer, n.

// What is the output?
// A string indicating whether the number n is "perfect," "abundant," or "deficient."

// What are the rules?:
// - Aliquot Sum: The sum of the proper divisors of n (i.e., divisors excluding n itself).
// - Classifications:
//       Perfect: If the aliquot sum equals n.
//       Abundant: If the aliquot sum is greater than n.
//       Deficient: If the aliquot sum is less than n.
// - The input will always be a positive integer.

// What is the mental model?
// You can think of this as a process where for a given number n, you gather all its divisors
// (excluding n itself), sum them up, and then compare the sum to n.
// Based on this comparison, the number is classified into one of the three categories.

// Step 2 - Examples and Test Cases:

// Example 1:
// Input: 6
//   Factors: 1, 2, 3
//   Aliquot sum: 1 + 2 + 3 = 6
// Output: Perfect

// Example 2:
// Input: 12
//   Factors: 1, 2, 3, 4, 6
//   Aliquot sum: 1 + 2 + 3 + 4 + 6 = 16
// Output: Abundant

// Example 3:
// Input: 8
//   Factors: 1, 2, 4
//   Aliquot sum: 1 + 2 + 4 = 7
// Output: Deficient

// Step 3 - Algorithm Design:

// 1. Check if the input n is positive. If not, return an error.
// 2. Initialize a variable sum to 0 to store the aliquot sum.
// 3. Iterate from 1 to n/2 (since no number greater than n/2 (except n itself) can be a divisor of n):
//    a. If the current number is a divisor of n, add it to sum.
// 4. Compare sum with n:
//    a. If sum equals n, return PERFECT_NUMBER.
//    b. If sum is greater than n, return ABUNDANT_NUMBER.
//    c. If sum is less than n, return DEFICIENT_NUMBER.

// Step 4 - Implementation:

#include "perfect_numbers.h"

kind classify_number(int n) {
    if (n <= 0) {
        return ERROR;
    }

    int sum = 0;

    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }

    if (sum == n) {
        return PERFECT_NUMBER;
    } else if (sum > n) {
        return ABUNDANT_NUMBER;
    } else {
        return DEFICIENT_NUMBER;
    }
}
