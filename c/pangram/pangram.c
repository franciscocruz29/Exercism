// Step 1 - Problem Understanding:
//
// What is the expected input?
// - Data type: Character array, Strings in C are arrays of characters terminated by a null character
// - Description: The input is a sentence that may contain letters, numbers, spaces, and punctuation
//
// What is the expected output?
// - Data type: boolean value
// - Description: true if the input sentence is a pangram (contains all 26 letters of the alphabet), false otherwise.
//
// What are the key rules or constraints?
// - The sentence must contain every letter of the alphabet (26 letters) at least once.
// - Case Insensitivity: The case of letters doesn't matter (e.g., 'a' and 'A' are considered the same letter).
// - Non-Letter Characters: Non-letter characters (numbers, punctuation, spaces, etc.) should be ignored.
// - Empty/Null Input: An empty string or a null pointer should result in false.
//
// What is the mental model?
// We need to determine if a given sentence contains all the letters of the alphabet at least once,
// ignoring case and disregarding any non-alphabetical characters.


// Step 2 - Examples:
//
// Input: "the quick brown fox jumps over the lazy dog"
// Output: true
//
// Input: "abcdefghijklm ABCDEFGHIJKLM"
// Output: false
//
// Input: "7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"
// Output: false
//
// Input: NULL or ""
// Output: false


// Step 3 - Data structure selection:
//
// - A suitable data structure for this problem is an array of 26 booleans (or an integer where each bit represents a letter) to keep track of encountered letters.


// Step 4 - Algorithm design:
//
// 1. Handle edge cases:
// - If the input is NULL, return false
// 2. Initialize letter tracking:
// - Create an array seen_letters of 26 booleans, all initialized to false. This array will track which letters of the alphabet we've seen in the sentence.
// 3. Process each character:
// - Iterate through each character c in the input sentence:
//      * If c is a letter (either lowercase or uppercase):
//      * Convert c to lowercase.
//      * Calculate the index corresponding to this letter in the alphabet. Each index corresponds to a letter ('a' = 0, 'b' = 1, ..., 'z' = 25).
//          For example:
//              'a' - 'a' = 0 (the index for 'a'),
//              'b' - 'a' = 1 (the index for 'b'),
//              'z' - 'a' = 25 (the index for 'z').
//      * Mark the corresponding element in seen_letters as true.
// 4. Check if All Letters Seen:
// - Iterate through the seen_letters array.
// - If any element is still false, it means we haven't seen that letter, so return false.
// 5. Return True:
// - If we've reached this point, it means all 26 letters have been seen, so return true.


// Step 5 - Implementation Considerations
//
// - Character Conversion: Use the tolower function from the ctype.h library to convert characters to lowercase for case-insensitive comparison.
// - Index Calculation: Subtract the ASCII value of 'a' from the lowercase letter to get its corresponding index in the alphabet.

#include "pangram.h"
#include <ctype.h>
#include <stdbool.h>

bool is_pangram(const char *sentence) {
    if (!sentence) return false;

    bool seen_letters[26] = {false}; // Track seen letters

    for (const char *c = sentence; *c != '\0'; c++) {
        if (isalpha(*c)) { // Check if it's a letter
            char lower_c = tolower(*c);
            int index = lower_c - 'a';
            seen_letters[index] = true;
        }
    }

    for (int i = 0; i < 26; i++) {
        if(!seen_letters[i]) {
            return false; // A letter is missing
        }
    }

    return true;
}
