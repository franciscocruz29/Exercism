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

// Step 3: Convert the input to the output - Imperative style

// 1. Initialize an empty string to store the resulting RNA strand.
// 2. Iterate through each character in the DNA strand.
// 3. For each character, determine its complementary RNA base:
//      If the DNA character is 'G', replace it with 'C'.
//      If the DNA character is 'C', replace it with 'G'.
//      If the DNA character is 'T', replace it with 'A'.
//      If the DNA character is 'A', replace it with 'U'.
// 4. Append the complementary RNA base to the initialized string.
// 5. After processing all characters, the resulting string will be the RNA strand.

// Step 4: Implementation - Imperative style

/* export const toRna = (dnaStrand) => {
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
        throw new Error("Invalid DNA character: " + dnaStrand[i]);
    }
  }

  return rnaStrand;
}; */

// Step 5: Convert the input to the output - Functional style

// 1. Define a mapping of DNA bases to their RNA complements.
// 2. Use a higher-order function (like map) to transform each character in the input string:
//    a. For each character, look up its complement in the mapping.
//    b. If the character isn't in the mapping, throw an error.
// 3. Join the resulting array of RNA bases into a single string.
// 4. Return the resulting RNA strand.

// Step 6: Implementation - Functional style

export const toRna = (dnaStrand) => {
  const dnaToRna = {
    G: "C",
    C: "G",
    T: "A",
    A: "U",
  };

  return dnaStrand
    .split('')
    .map(base => {
      if (base in dnaToRna) {
        return dnaToRna[base];
      } else {
        throw new Error(`Invalid DNA character: ${base}`);
      }
    })
    .join('');
};
