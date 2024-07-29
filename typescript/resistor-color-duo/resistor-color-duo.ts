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
// - The mental model is to map the first and second color names to their respective digits and then combine these digits to form a two-digit number representing the resistor's value.
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
// 1. Create a map (object) that associates each color name with its corresponding digit.
// 2. Define a function that takes an array of color names as input.
// 3. Extract the first two color names from the input array using array destructuring.
// 4. Use the color map to get the numeric values for the first and second colors.
// 5. Combine these two numeric values into a single two-digit number:
//    - Convert the first color's value to a string and concatenate it with the second color's value.
//    - Convert the resulting string back to a number.
// 6. Return the final two-digit number.
//
//
// Step 4. Implementation
interface Color {
  [c: string]: number;
}

const colorsMap: Color = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
};

export function decodedValue(colors: string[]): number {
  const [first, second] = colors;
  return Number(`${colorsMap[first]}${colorsMap[second]}`);
}
