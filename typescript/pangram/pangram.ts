const ALPHABET = Array.from("abcdefghijklmnopqrstuvwxyz");

export function isPangram(sentence: string): boolean {
  const normalized = sentence.toLowerCase();
  return ALPHABET.every((letter) => normalized.includes(letter));
}
