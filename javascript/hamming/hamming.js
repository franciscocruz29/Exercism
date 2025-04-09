// Step 1 - Problem Understanding
//
// * What are the expected inputs?
//     * Data type: string
//     * Description: DNA strands, using the letters 'A', 'C', 'G', and 'T'
//
// * What are the expected outputs?
//     * Data type: number
//     * Description: The number of differing positions (non-negative integer)
//
// * What are the key rules or constraints?
//    - The DNA strands must be of equal length
//    - The comparison is position-by-position (index-based)
//
// * What is the mental model?
//    - Compare each character in the two strands and count the number of mismatches
//
// Step 2 - Examples
//
// Input:
//   - strand_a: ''
//   - strand_b: ''
// Output: 0
//
// Input:
//   - strand_a: 'G'
//   - strand_b: 'C'
// Output: 1
//
// Input:
//   - strand_a: 'GGACGGATTCTG'
//   - strand_b: 'AGGACGGATTCT'
// Output: 9
//
// Input:
//   - strand_a: 'AATG'
//   - strand_b: 'AAA'
// Output: Error('strands must be of equal length'),
//
// Step 3 - Algorithm design
// 1. Check that the strands are the same length, if not throw an Error
// 2. Initialize a counter for differences
// 3. Loop through each position in both strands simultaneously
//    3.1 Compare characters at current position
//    3.2 Increment counter when characters differ
// 4. Return the total number of differences
//
// Step 4 - Implementation
//
export const compute = (strand_a, strand_b) => {
  throw new Error("Remove this statement and implement this function");
};
