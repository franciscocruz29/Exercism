// Step 1: Understand the problem

// What are the inputs?
// Two strings representing DNA strands (strand_a and strand_b)

// What is the output?
// An integer representing the Hamming distance between the two DNA strands.
// Return -1 if the strands are of different lengths.

// What are the rules?
// The Hamming distance is the number of positions at which the corresponding nucleotides are different.
// The two input strands must be of equal length.

// What is the mental model?
// Compare each nucleotide at the same position in both DNA strands. Count the number of positions where the nucleotides differ and return this count as the Hamming distance.


// Step 2: Examples

// Input: strand_a = "", strand_b = ""
// Output: 0

// Input: strand_a = "G", strand_b =  "T"
// Output: 1

// Input: strand_a = "GGACGGATTCTG", strand_b =  "AGGACGGATTCT"
// Output: 9

// Input: strand_a = "ATA", strand_b = "AGTG"
// Output: -1

// Input: strand_a = "G", strand_b = ""
// Output: -1


// Step 3: Algorithm - Steps for converting the input to output

// 1. Check if either input strand is null. If yes, return -1.
// 2. Initialize a variable to keep track of the Hamming distance.
// 3. Iterate through the characters of both strands simultaneously.
// 4. Compare the current characters of both strands.
// 5. If the characters are different, increment the distance counter.
// 6. Move to the next character in both strands.
// 7. After the loop, check if either strand has remaining characters.
// 8. If one strand is longer than the other, return -1.
// 9. If both strands are of equal length, return the computed Hamming distance.


// Step 4: Implementation
#include "hamming.h"

// int compute(const char* lhs, const char* rhs) {
//     if (!lhs || !rhs) return -1;

//     int distance = 0;

//     while (*lhs && *rhs) {
//         if (*lhs != *rhs) distance++;
//         lhs++;
//         rhs++;
//     }

//     return (*lhs || *rhs) ? -1 : distance;
// }


// Step 5: Refactoring
#include <stddef.h> // For NULL

int compute(const char* lhs, const char* rhs) {
    // 1. Ensure both input strands are not null.
    if (lhs == NULL || rhs == NULL) return -1;

    // 2. Initialize the Hamming distance counter.
    int distance = 0;

    // 3. Iterate through both strands simultaneously.
    //                      This checks if the current character pointed to is not the null character ('\0')
    for (; *lhs != '\0' && *rhs != '\0'; lhs++, rhs++) {
        // 4. Increment the distance counter if characters differ.
        if (*lhs != *rhs) distance++;
    }

    // 5. Check if both strands are of equal length.
    if (*lhs != '\0' || *rhs != '\0') {
        return -1;
    }

    // 6. Return the computed Hamming distance.
    return distance;
}
