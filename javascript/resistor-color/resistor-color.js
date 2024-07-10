// Step 1: Understand the problem
// What is the input?
// The input is a color band (a string) which represents one of the resistor colors.

// What is the output?
// The output is the numerical value associated with the given color band.

// What are the rules?
// Each color band maps to a specific number as defined:
// Black: 0, Brown: 1, Red: 2, Orange: 3, Yellow: 4,
// Green: 5, Blue: 6, Violet: 7, Grey: 8, White: 9

// Step 2: Examples
// colorCode('orange') => 3
// colorCode('white') => 9
// colorCode('black') => 0

// Step 3: Write the algorithm
// 1. Define an array `COLORS` that lists all the colors in the correct order.
// 2. Create a function `colorCode` that takes a color as input.
// 3. The function should return the index of the color in the `COLORS` array.

// Step 4: Implementation
/**
 * Array of colors representing resistor color bands in order.
 * @const {string[]}
 */
export const COLORS = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white",
];

/**
 * Function to get the numerical value associated with a color band.
 * @param {string} color - The color band to look up.
 * @returns {number} - The numerical value associated with the color band.
 */
export function colorCode(color) {
  return COLORS.indexOf(color);
}
