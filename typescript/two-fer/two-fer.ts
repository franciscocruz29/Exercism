// Step 1: Understand the problem

// What are the inputs?
// - A name (string) or nothing

// What are the outputs?
// - A string in the format "One for {name}, one for me."

// What are the rules?
// - If a name is provided, use that name in the output
// - If no name is provided, use "you" instead
// - The output should always follow the format "One for X, one for me.";

// What is the mental model?
// - The problem is to construct a sentence based on a given name, following a specific template.

// Step 2: Examples and Test Cases

// Example 1 (Typical Case):
// Input: "Alice";
// Output: "One for Alice, one for me."

// Example 2 (Default Case):
// Input: No name provided.
// Output: "One for you, one for me.";

// Step 3: Algorithm Design

// 1. Input handling:
// - If a name is provided, use the name
// - If no name is provided, use "you"

// 2. Construct the sentence:
// - Form the sentence using a template where "One for [name], one for me." is filled in with either the provided name or the default value.

// 3. Return the sentence

// Step 4: Implementation
export function twoFer(name: string = "you"): string {
  return `One for ${name}, one for me.`;
}
