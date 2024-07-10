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
// color_code('orange') => 3
// color_code('white') => 9
// color_code('black') => 0

// Step 3: Write the algorithm
// 1. Define a mapping: Create a dictionary where each color (as a string) maps to its corresponding numerical value.
// 2. Get the input: Take the color band as input.
// 3. Lookup the value: Use the dictionary to find the numerical value associated with the given color band.
// 4. Return the result: Output the numerical value.
#include "resistor_color.h"

const resistor_band_t* colors(void)
{
    static const resistor_band_t colors[] =
    {
        BLACK, BROWN, RED, ORANGE, YELLOW,
        GREEN, BLUE, VIOLET, GREY, WHITE
    };
    return colors;
}

uint16_t color_code(resistor_band_t color) {
    // Since the enum values are automatically assigned starting from 0, we can directly return the color value
    return color;
}
