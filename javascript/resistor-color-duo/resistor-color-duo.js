// Step 1. Understand the problem:
//
// What is the input?
// - An array of color names (strings) representing the resistor bands
//
// What is the output?
// - A two-digit number representing the resistance value
//
// What are the rules?
// - Each color corresponds to a specific digit (black: 0, brown: 1, red: 2, etc.).
// - Only the first two colors are used to calculate the output value.
// - The output is formed by concatenating the digits of the first and second color bands.
//
// What is the mental model?
// - We are mapping colors to numbers to calculate a resistance value based on the first two bands of a resistor.
//
//
// Step 2. Examples:
// Input: ['brown', 'black']
// Output: 10
//
// Input: ['orange', 'orange'])
// Output: 33
//
// Input: ['green', 'brown', 'orange']
// Output: 51
//
//
// Step 3. Write the algorithm - steps for converting the input to output
//
// 1. Define a constant array with the color names in order, each corresponding to its numeric value.
// 2. Take the first two colors from the input array
// 3. Find the index of the first color in the color array and multiply it by 10
// 4. Find the index of the second color in the color array
// 5. Combine the two numeric values to form the final two-digit number.
//
//
// Step 4. Implementation

const COLOR = [
  `black`,
  `brown`,
  `red`,
  `orange`,
  `yellow`,
  `green`,
  `blue`,
  `violet`,
  `grey`,
  `white`,
];

export const decodedValue = ([firstColor, secondColor]) =>
  COLOR.indexOf(firstColor) * 10 + COLOR.indexOf(secondColor);
