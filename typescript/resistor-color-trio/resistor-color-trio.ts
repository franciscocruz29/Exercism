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
type Unit = typeof Units[number];

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
