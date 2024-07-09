/* Step 1: Understand the problem
   What is input?
     - A square number on the chessboard (1-64)
   What is the output?
     - Number of grains on the given square
     - Total number of grains on the chessboard
   What are the rules?
     - The first square has 1 grain
     - Each subsequent square doubles the number of grains from the previous square
     - There are 64 squares on the chessboard */

/* Step 2: Examples
   Square 1: 1 grain
   Square 2: 2 grains
   Square 3: 4 grains
   Square 4: 8 grains
   ...
   Square 64: 2^63 grains */

/* Step 3: Write the Algorithm
   1. Create a function 'square' to calculate grains on a given square:
      - Check if the input number is between 1 and 64, raise ValueError if not
      - Use 2^(number - 1) to calculate grains
   2. Create a function 'total' to calculate total grains on the chessboard:
      - Use the formula: 2^64 - 1 (sum of geometric series) */

/* Step 4: Implementation */
#include "grains.h"
#include <stdint.h>

uint64_t square(uint8_t index) {
    if (index < 1 || index > 64) {
        return 0;
    }
    // Use 2^(number - 1) to calculate grains
    // The bitwise left shift operation 1 << (index - 1) is equivalent to calculating 2^(index - 1)
    return (uint64_t)1 << (index - 1);
}

uint64_t total(void) {
    // Use the formula: 2^64 - 1 (sum of geometric series)
    return UINT64_MAX;  // This is equal to 2^64 - 1
}
