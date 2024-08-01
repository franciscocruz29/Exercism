// Step 1. Understand the problem:

// What is the input?
// - An array of color names (strings) representing the resistor bands

// What is the output?
// - A two-digit number representing the resistance value

// What are the rules?
// - Each color corresponds to a specific digit (black: 0, brown: 1, red: 2, etc.).
// - Only the first two colors are used to calculate the output value.
// - The output is formed by concatenating the digits of the first and second color bands.

// What is the mental model?
// - The mental model is to map the first and second color names to their respective digits and then combine these digits to form a two-digit number representing the resistor's value.


// Step 2. Examples:
// Input: ['brown', 'black']
// Output: 10

// Input: ['orange', 'orange'])
// Output: 33

// Input: ['green', 'brown', 'orange']
// Output: 51


// Step 3. Write the algorithm - steps for converting the input to output
// 1. Map color names to their corresponding digit values.
// 2. Access the first color from the input array
// 3. Multiply the value of the first color by 10
// 4. Access the second color from the input array
// 5. Add the value of the second color to the result from step 2
// 6. Return the final sum as the resistance value


// Step 4. Implementation
#include "resistor_color_duo.h"

uint16_t color_code(const resistor_band_t *colors) {
    return colors[0] * 10 + colors[1];
}
