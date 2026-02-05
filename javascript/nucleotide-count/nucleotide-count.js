// Step 1 - Problem Understanding:
//
// * What are the expected inputs? (Data type, Description)
//   - Input: A string representing a DNA sequence. Could be empty or non-empty.
//   - Valid characters are the nucleotides 'A', 'C', 'G', and 'T' (case-insensitive; lowercase letters should be treated as their uppercase equivalents).
//
// * What are the expected outputs? (Data type, Description)
//   - Output: A string containing 4 integer numbers separated by spaces in the order: A C G T
//   - Alternative: Error/exception if input contains invalid characters
//
// * Explicit requirements: What is clearly stated?
//   - Count how many times each nucleotide (A, C, G, T) appears in the given DNA sequence.
//   - If the string contains any invalid characters, the function must signal an error.
//   - The result must always be formatted as a single space-separated string of four numbers.
//
// * Implicit requirements: What is implied through examples or logic?
//   - If the input string is empty, the output should be "0 0 0 0".
//
// * Problem domain: Define any domain-specific terms or concepts
//   - DNA sequence: A string composed of the nucleotides A, C, G, and T.
//
// * Clarifying questions: What needs confirmation or is ambiguous?
//   - Is the input case-sensitive? (Should 'a' be treated as 'A', or is 'a' invalid?)
//   - How exactly should I signal an error? Throw an exception or return a specific string?
//
// * What is the mental model — a high-level description of how you think about the problem from start to finish (without worrying yet about implementation).
// - Iterate through the input string.
// - Check if every character is one of 'A', 'C', 'G', or 'T'.
// - If an invalid character is found, immediately stop and return an error.
// - If valid, increment the count for that specific nucleotide.
// - Finally, format the four counts into a single string separated by spaces.

// Step 2 - Examples / Test Cases:
//
// Assumptions:
//  - The input is always uppercase
//  - When the input contains invalid characters, throw an error with the message "Invalid nucleotide in strand"
//
// Input: ""
// Output: "0 0 0 0"
//
// Input: "G"
// Output: "0 0 1 0"
//
// Input: "ACGT"
// Output: "1 1 1 1"
//
// Input: "GGGGGGG"
// Output: "0 0 7 0"
//
// Input: "GATTACA"
// Output: "3 1 1 2"
//
// Input: "AGXXACT"
// Output: new Error("Invalid nucleotide in strand")
//
// Input: "AC GT"
// Output: new Error("Invalid nucleotide in strand")

// Step 3 - Data Structure:
//
// Four integer counters will be used to track the number of occurrences
// of each nucleotide (A, C, G, T).
//
// This choice is appropriate because:
// - The set of nucleotides is fixed and known in advance.
// - Each nucleotide needs a simple running total.
// - This maps perfectly to my mental model: increment the right counter.

// Step 4 - Algorithm Design:
//
// * Determine a series of precise instructions (pseudocode) that will transform the input to the desired output.
// * Ensure the algorithm is detailed enough to be easily coded, but not written at the programming language level to maintain flexibility.
// * Manually test the algorithm with your examples to ensure confidence.

// Step 5 - Implementation:
//
// * Translate your algorithm into code in your chosen programming language.

// Step 6 - Refactoring:
//
// * Review your working code for clarity, efficiency, and adherence to style guides.
// * Make sure your code still handles edge cases and satisfies all test cases after refactoring.

export function countNucleotides(strand) {
  throw new Error("Remove this statement and implement this function");
}
