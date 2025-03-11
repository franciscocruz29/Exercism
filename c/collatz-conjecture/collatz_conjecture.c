// 1. Understand the problem:

// What are the inputs?
// A number n >= 1

// What are the outputs?
// The number of steps required to reach 1

// What are the rules?
// Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n
// is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process
// indefinitely. The conjecture states that no matter which number you start
// with, you will always reach 1 eventually. If n is not a positive integer,
// stop the program from being executed further and return an error message.

// 2. Examples:

// Starting witn n = 4, the steps would be as follows: 4, 2, 1. So for input n =
// 4, the return value would be 2. Starting with n = 6, the steps would be as
// follows: 6, 3, 10, 5, 16, 8, 4, 2, 1. So for input n = 6, the return value
// would be 8. Starting with n = 12, the steps would be as follows: 12, 6, 3,
// 10, 5, 16, 8, 4, 2, 1. So for input n = 12, the return value would be 9.

// 3. Algorithm:

// 1. If n is not a positive integer, return an error message.
// 2. If n = 1, return 0.
// 3. Initialize result = 0.
// 4. While n is not equal to 1:
//    4.1 If n is even, divide n by 2 to get n / 2.
//    4.2 If n is odd, multiply n by 3 and add 1 to get 3n + 1.
//    4.3 Increment result by 1.
// 5. Return result.

// 4. Implementation:
#include "collatz_conjecture.h"
/*
int steps(int start) {
    if (start <= 0) {
        return ERROR_VALUE;
    }

    int n = start;
    int result = 0;

    while (n != 1) {
        if (n % 2 == 0){
            n = n/2;
        } else {
            n = 3 * n + 1;
        }
        result++;
    }
    return result;
}
*/

// 5. Refactoring:
int steps(int start) {
  int steps = (start > 0) ? 0 : -1;
  while (start > 1) {
    start = (start % 2) ? 3 * start + 1 : start / 2;
    steps++;
  }

  return steps;
}
