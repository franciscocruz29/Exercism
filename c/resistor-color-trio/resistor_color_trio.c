// Step 1 - Problem Understanding:

// - What is the input?
//   - A pointer to an array of resistor_band_t elements.

// - What is the output?
//   - resistor_value_t struct. It contains:
//       value: A uint16_t representing the numerical value of the resistor.
//       unit: A unit_t enum indicating the unit (OHMS, KILOOHMS, etc.).

// - What are the rules?
//   - The first two colors represent digits of a two-digit number
//   - The third color represents the number of zeros to add
//   - Use metric prefixes for larger values (e.g., kiloohms)

// - What is the mental model?
//   - You have a list of three colors representing a resistor. The first two colors form the base number, and the third color determines how many zeros are added.
//     If the resulting number is large enough use metric prefixes

// Step 2 - Examples:

// Input: ["orange", "orange", "black"]
// Output: "33 ohms"

// Input: ["blue", "grey", "brown"],
// Output: "680 ohms"

// Input: ["orange", "orange", "orange"]
// Output: "33 kiloohms"

// Input: ["blue", "green", "yellow", "orange"])
// Output: "650 kiloohms"

// Step 3 - Algorithm Design:

// 1. Color Interpretation:
// - Each color corresponds to a numerical value.
// - The first two colors represent the significant digits of the resistor's value.
// - The third color represents the multiplier (the power of 10).
//
// 2. Value Calculation:
// - Multiply the first color's value by 10 and add the second color's value to get the base value.
// - Calculate the multiplier based on the third color.
// - Multiply the base value by the multiplier to get the resistor's value.
//
// 3. Unit Determination:
// - Based on the magnitude of the resistor's value, determine the appropriate unit (ohms, kilohms, megaohms, or gigaohms).
// - Divide the resistor's value by the appropriate power of 10 to get the final value in the chosen unit.

// Step 4 - Implementation:

#include "resistor_color_trio.h"
#include <stdint.h>
#include <math.h> // For pow()

resistor_value_t color_code(const resistor_band_t *colors) {
    // Extract the significant digits from the first two colors
    uint32_t digit1 = colors[0]; // First color band (10's place)
    uint32_t digit2 = colors[1]; // Second color band (1's place)

    // Calculate the base value
    uint32_t base_value = (digit1 * 10) + digit2;

    // The third color is the multiplier
    uint32_t multiplier = pow(10, colors[2]); // 10 raised to the power of third band

    // Calculate the resistor value
    uint64_t resistor_value = (uint64_t)base_value * multiplier;

    // Determine the unit based on the resistor value
    resistor_value_t result;
    if (resistor_value >= 1000000000) {
        result.value = resistor_value / 1000000000;
        result.unit = GIGAOHMS;
    } else if (resistor_value >= 1000000) {
        result.value = resistor_value / 1000000;
        result.unit = MEGAOHMS;
    } else if (resistor_value >= 1000) {
        result.value = resistor_value / 1000;
        result.unit = KILOOHMS;
    } else {
        result.value = resistor_value;
        result.unit = OHMS;
    }

    return result;
}
