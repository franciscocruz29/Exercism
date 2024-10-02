// Step 1 - Problem Understanding:

// - What is the input?
//   - A list of three strings. Each string represents a color

// - What is the output?
//   - We need to produce a string that describes the resistor's value in a human-readable format, including the correct units (e.g., "33 ohms").

// - What are the rules?
//   - The first two colors represent digits of a two-digit number
//   - The third color represents the number of zeros to add
//   - Use metric prefixes for larger values (e.g., kiloohms)

// - What is the mental model?
//   - You have a list of three colors representing a resistor. The first two colors form the base number, and the third color determines how many zeros are added. If the resulting number is large enough use metric prefixes

// Step 2 - Examples:

// Input: ["orange", "orange", "black"]
// Output: "33 ohms"

// Input: ["blue", "grey", "brown"],
// Output: "680 ohms"

// Input: ["orange", "orange", "orange"]
// Output: "33 kiloohms"

// Input: ["blue", "green", "yellow", "orange"])
// Output: "650 kiloohms"

// Step 3 - Data Structure Selection:

// Dictionary: For mapping colors to their numeric values (e.g., "orange" -> 3). This is optimal because a dictionary provides fast lookups by color name, making the program efficient.
// List: To store units like "ohms", "kiloohms". Using a list keeps the units in order and allows us to easily pick the appropriate unit as needed.

// Step 4 - Algorithm Design:

// 1. Create a color-to-value mapping:
//       - Define a dictionary where the keys are color names, and the values are the corresponding numeric values (e.g., "black" → 0, "brown" → 1, etc.)
// 2. Create a list of metric prefixes in ascending order:
//       - Define a list of metric prefixes starting with the base unit ("ohms") and moving to higher orders of magnitude ("kilo", "mega", "giga").
// 3. Extract the numeric values for the first two colors
// 4. Calculate the base resistance: (first_digit * 10 + second_digit) * (10 ^ third_digit)
// 5. Determine the appropriate metric prefix:
//       - Start with the base unit (ohms)
//       - While the resistance value is greater than or equal to 1000, divide it by 1000 and move to the next prefix in the list (e.g., from "ohms" to "kilo", from "kilo" to "mega").
//       - Continue dividing until the resistance value is less than 1000, which ensures the value is represented in the most appropriate scale.
// 6. Format the result as a string with the value and unit

// Step 5 - Implementation:

enum Colors {
  black,
  brown,
  red,
  orange,
  yellow,
  green,
  blue,
  violet,
  grey,
  white,
}
type Color = keyof typeof Colors;

const Units = ["ohms", "kiloohms", "megaohms", "gigaohms"];
type Unit = (typeof Units)[number];

interface Resistance {
  value: number;
  unit: Unit;
}

function toResistance(x: number): Resistance {
  let value = x;
  let unit = "ohms";
  for (let i = 1; i <= 3 && value >= 1000; i++) {
    value /= 1000;
    unit = Units[i];
  }
  return { value, unit };
}

export function decodedResistorValue([x1, x2, x3]: Color[]): string {
  const raw = (Colors[x1] * 10 + Colors[x2]) * 10 ** Colors[x3];
  const { value, unit } = toResistance(raw);
  return `${value} ${unit}`;
}
