//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const COLOR = [`black`,
  `brown`,
  `red`,
  `orange`,
  `yellow`,
  `green`,
  `blue`,
  `violet`,
  `grey`,
  `white`,];

export const decodedValue = ([firstColor, secondColor]) => COLOR.indexOf(firstColor) * 10 + COLOR.indexOf(secondColor);
