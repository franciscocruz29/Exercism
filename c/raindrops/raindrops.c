// Step 1: Understand the problem

// What are the inputs?
// - An integer

// What are the outputs?
// - A string that represents the raindrop sounds

// What are the rules?
// - if a given number has 3 as a factor, add 'Pling' to the result.
// - if a given number has 5 as a factor, add 'Plang' to the result.
// - if a given number has 7 as a factor, add 'Plong' to the result.
// - if a given number does not have 3, 5, or 7 as a factor, the result should be the number as a string.

// What is the mental model?
// - The task is to convert a number into a string containing specific raindrop sounds depending on whether it has 3, 5, or 7 as factors.
// If none of these conditions apply, the output is simply the number as a string.

// Step 2: Examples

// Input: 1;
// Output: '1'
// (Edge case: No factors of 3, 5, or 7);

// Input: 6;
// Output: 'Pling'
// (Divisible by 3, but not by 5 or 7);

// Input: 14;
// Output: 'Plong'
// (Divisible by 7, but not by 3 or 5);

// Input: 15;
// Output: 'PlingPlang'
// (Divisible by 3 and 5, but not by 7);

// Input: 105;
// Output: 'PlingPlangPlong'
// (Divisible by 3, 5, and 7)

// Step 3: Algorithm design

// Assumptions:

// 1. drops is a non-negative, 32-bit integer (from 0 to 2,147,483,647)
// 2. result has enough space to hold the largest output string, meaning 16 bytes:
//    - 15 bytes for "PlingPlangPlong", plus one for the null terminating character;
//    - 10 bytes for the largest possible value of drops, plus one for '\0'.
// 3. result has been initialized as an empty string (that is, result[0] is '\0')

// Data-driven design: https://cdn.nakamotoinstitute.org/docs/taoup.pdf

/* When doing data - driven programming, one clearly distinguishes code from the data structures on which it acts,
and designs both so that one can make changes to the logic of the program by editing not the code but the data structure.

This approach allows for extensible code: for example, new sounds could be added (or removed) without modifying the convert function.
*/

// 1. Create a function that takes a character array result for output and an integer drops as input
// 2. Define an array of structs, each containing a factor and its corresponding sound
// 3. Iterate through the factor-sound pairs:
//    - For each pair, check if drops is divisible by the factor
//    - If divisible, concatenate the sound to the result string
// 4. If the result string is still empty after checking all factors, convert drops to a string
// 5. Ensure the result string is null-terminated

// Step 4: Implementation
#include "raindrops.h"
#include <stdio.h>
#include <string.h>

typedef struct
{
  int factor;
  const char *sound;
} FactorSound;

static const FactorSound factorSounds[] = {
    {3, "Pling"},
    {5, "Plang"},
    {7, "Plong"}};
void convert(char result[], int drops)
{

  int numFactors = sizeof(factorSounds) / sizeof(factorSounds[0]);
  size_t max_size = 16; // Maximum buffer size for the result string

  // Safely append sounds for divisible factors
  for (int i = 0; i < numFactors; i++)
  {
    if (drops % factorSounds[i].factor == 0)
    {
      // Ensure we don't overflow the result buffer
      strncat(result, factorSounds[i].sound, max_size - strlen(result) - 1);
    }
  }

  // If no factors were found, convert the number to a string
  if (strlen(result) == 0)
  {
    snprintf(result, max_size, "%d", drops);
  }
}
