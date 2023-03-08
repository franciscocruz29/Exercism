const dnaMap = new Map<string, string>([
  ["G", "C"],
  ["C", "G"],
  ["T", "A"],
  ["A", "U"],
]);

export function toRna(strand: string): string {
  let transcribed: string = "";

  const chars = [...strand].forEach((char) => {
    if (!dnaMap.has(char)) throw new Error("Invalid input DNA.");
    transcribed += dnaMap.get(char);
  });

  return transcribed;
}
