// Step 1: Understand the problem

// What are the inputs?
// A string representing the DNA strand

// What are the outputs?
// A string representing the RNA strand

// What are the rules?
// Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
//   G -> C
//   C -> G
//   T -> A
//   A -> U

// What is the mental model?
// Iterate through each nucleotide in the DNA strand, replace it with the corresponding RNA nucleotide, and concatenate these to form the RNA strand.

// Step 2: Examples

// Input: ''
// OUtput: ''

// Input: 'G'
// Output: 'C'

// Input: 'ACGTGGTCTTAA'
// Output: 'UGCACCAGAAUU'

// Step 3: Convert the input to the output

// 1. Initialize an empty string to store the resulting RNA strand.
// 2. Iterate through each character in the DNA strand.
// 3. For each character, determine its complementary RNA base:
//      If the DNA character is 'G', replace it with 'C'.
//      If the DNA character is 'C', replace it with 'G'.
//      If the DNA character is 'T', replace it with 'A'.
//      If the DNA character is 'A', replace it with 'U'.
// 4. Append the complementary RNA base to the initialized string.
// 5. After processing all characters, the resulting string will be the RNA strand.

// Step 4: Implementation
#include "rna_transcription.h"
#include <string.h>
#include <stdlib.h>

/* char *to_rna(const char *dna)
{
  char *rna = (char *)malloc(sizeof(char) * (strlen(dna) + 1)); // creates a new string named rna with enough space to store a copy of the dna string, including a null terminator.

  for (size_t i = 0; i < strlen(dna); i++)
  {
    switch (dna[i])
    {
    case 'G':
      rna[i] = 'C';
      break;
    case 'C':
      rna[i] = 'G';
      break;
    case 'T':
      rna[i] = 'A';
      break;
    case 'A':
      rna[i] = 'U';
      break;
    default:
      rna[i] = dna[i];
      break;
    }
  }
  return rna;
} */

// Step 5: Refactor the code
static char map_dna_to_rna(char nucleotide)
{
  switch (nucleotide)
  {
  case 'G':
    return 'C';
  case 'C':
    return 'G';
  case 'T':
    return 'A';
  case 'A':
    return 'U';
  default:
    return nucleotide; // This should handle unexpected characters
  }
}

char *to_rna(const char *dna)
{
  if (dna == NULL)
  {
    return NULL; // Handle null input
  }

  size_t length = strlen(dna);
  char *rna = (char *)malloc(length + 1); // Allocate memory, including space for null terminator

  if (rna == NULL)
  {
    return NULL; // Handle memory allocation failure
  }

  for (size_t i = 0; i < length; i++)
  {
    rna[i] = map_dna_to_rna(dna[i]);
  }

  rna[length] = '\0'; // Add null terminator
  return rna;
}
