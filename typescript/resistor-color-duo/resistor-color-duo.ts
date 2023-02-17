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
