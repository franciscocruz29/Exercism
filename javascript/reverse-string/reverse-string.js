// 1. Understand the problem:
// What is the input? A string 
// What is the output? A reversed string, reading them from right to left, rather than from left to right

// 2. Examples:
// "stressed" --> "desserts"
// "strops" --> "sports"
// "racecar" --> "racecar"

// 3. Algorithm: 

// 1. Initialize an empty string called reversedString to store the reversed string.
// 2. Start a loop that iterates through the input string from the last character to the first character.
// 3. In each iteration, append the current character from the input string to the reversedString.
// 4. After the loop completes, return the reversedString as the final result.

// 4. Implementation:

/* export const reverseString = (inputString) => {
  let reversedString = "";

  for (let i = inputString.length - 1; i >= 0; i--) {
    reversedString += inputString[i];
  }

  return reversedString;
}; */

// 5. Refactoring:

export const reverseString = (inputString) => {
  // Check if the input is a valid string
  if (typeof inputString !== 'string') {
    throw new Error('Input must be a string');
  }

  // Convert the input string to an array of characters
  const charArray = Array.from(inputString);

  // Reverse the array of characters
  charArray.reverse();

  // Convert the array of characters back to a string
  const reversedString = charArray.join('');

  return reversedString;
};
