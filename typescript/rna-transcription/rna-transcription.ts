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
// Iterate through each character in the input DNA strand. For each character, replace it with its RNA complement according to the given rules.
// Concatenate these complements to form the final RNA strand.

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
//      Otherwise, throw an error.
// 4. Append the complementary RNA base to the initialized string.
// 5. After processing all characters, the resulting string will be the RNA strand.

// Step 4: Implementation

export const toRna = (dnaStrand: string): string => {
  let rnaStrand = "";

  for (let i = 0; i < dnaStrand.length; i++) {
    switch (dnaStrand[i]) {
      case "G":
        rnaStrand += "C";
        break;
      case "C":
        rnaStrand += "G";
        break;
      case "T":
        rnaStrand += "A";
        break;
      case "A":
        rnaStrand += "U";
        break;

      default:
        throw new Error("Invalid input DNA.");
    }
  }

  return rnaStrand;
};
