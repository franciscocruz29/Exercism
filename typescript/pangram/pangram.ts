// 1. Problem Understanding:
//
// * What are the expected inputs?
//   - Data type: string
//   - A string representing the sentence to be checked.
//
// * What are the expected outputs?
//   - Data type: boolean
//   - true if the sentence is a pangram, false otherwise.
//
// * What are the key rules or constraints?
//   - Case Insensitivity: The comparison of letters should be case-insensitive, meaning that 'a' and 'A' are considered the same letter.
//   - Alphabet Letters Only: Only the 26 letters of the English alphabet ('a' to 'z') matter. Any other characters, such as digits, punctuation, or spaces, should be ignored.
//   - Presence of All Letters: A sentence must contain at least one occurrence of each letter of the alphabet. If any letter is missing, the sentence is not a pangram.
//
// * What is the mental model?
//   - We need to verify if every letter of the alphabet appears at least once in the sentence.

// 2. Examples and Test Cases:
//
// Input: "The quick brown fox jumps over the lazy dog"
// Output: true
//
// Input: "The quick brown fox jumps over the lazy cat"
// Output: false
//
// Input: "AbCdEfGhIjKlMnOpQrStUvWxYz"
// Output: true
//
// Input: "Hello, World!"
// Output: false

// 3. Data Structure Selection:
// * What data structure(s) would best suit this problem?
//   - We'll use a set to store unique alphabetic characters. This ensures that each letter is counted only once

// 4. Algorithm Design:
//
// 1. Normalize the input sentence to lower-case
// 2. Initialize a set to keep track of unique alphabetic characters
// 3. Loop through each character in the sentence:
//    - if the character is a letter, add it to the set
// 4. After the loop, check if the size of the set is 26
// 5. Return true if the set contains 26 letters, otherwise return false

// 5. Implementation Considerations:

// Time Complexity: O(n), where n is the length of the sentence. We iterate through each character once.
// Space Complexity: O(1). The Set will store at most 26 elements (the letters of the alphabet).

// export function isPangram(sentence: string): boolean {
//   const letters = new Set<string>();

//   const lowerCaseSentence = sentence.toLowerCase();

//   for (let char of lowerCaseSentence) {
//     if (char >= "a" && char <= "z") {
//       letters.add(char);
//     }
//   }

//   return letters.size === 26;
// }

// 6. Refactoring:

export function isPangram(sentence: string): boolean {
  const lowerCaseSentence = sentence.toLowerCase();
  const uniqueLetters = new Set(lowerCaseSentence.match(/[a-z]/g));
  return uniqueLetters.size === 26;
}
