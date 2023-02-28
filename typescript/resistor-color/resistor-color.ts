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
] as const;

type Colors = typeof COLORS[number];

export const colorCode = (color: Colors) => COLORS.indexOf(color);
