// Step 1: Understand the problem

// What are the inputs?
// - An integer

// What are the outputs?
// - A string that represents the raindrop sounds

// What are the rules?
// - if a given number has 3 as a factor, add 'Pling' to the result.
// - if a given number has 5 as a factor, add 'Plang' to the result.
// - if a given number has 7 as a factor, add 'Plong' to the result.
// - if a given number does not have 3, 5, or 7 as a factor, the result should be the number as a string.

// What is the mental model?
// - The task is to convert a number into a string containing specific raindrop sounds depending on whether it has 3, 5, or 7 as factors.If none of these conditions apply, the output is simply the number as a string.

// Step 2: Examples

// Input: 1;
// Output: '1'
// (Edge case: No factors of 3, 5, or 7);

// Input: 6;
// Output: 'Pling'
// (Divisible by 3, but not by 5 or 7);

// Input: 14;
// Output: 'Plong'
// (Divisible by 7, but not by 3 or 5);

// Input: 15;
// Output: 'PlingPlang'
// (Divisible by 3 and 5, but not by 7);

// Input: 105;
// Output: 'PlingPlangPlong'
// (Divisible by 3, 5, and 7)

// Step 3: Algorithm design

// 1. Initialize an empty string to build the result.
// 2. Define a list of factor - sound pairs as an array of objects or arrays. Each pair will contain a divisor and the corresponding raindrop sound:
//   - If the number is divisible by 3, append "Pling" to the result.
//   - If the number is divisible by 5, append "Plang" to the result.
//   - If the number is divisible by 7, append "Plong" to the result.
// 3. Iterate over the factor-sound pairs:
//   - For each factor, check if the number is divisible by it.
//   - If so, append the associated sound to the result string.
// 4. Check the result after the iteration:
//   - If the result string is still empty, return the number itself as a string.
// 5. Return the result (either the raindrop sounds or the number as a string).

// Step 4: Implementation
export const convert = (number) => {
  let result = "";
  const factors = [
    { factor: 3, sound: "Pling" },
    { factor: 5, sound: "Plang" },
    { factor: 7, sound: "Plong" }
  ];

  factors.forEach(pair => {
    if (number % pair.factor === 0) {
      result += pair.sound;
    }
  });

  return result || number.toString();
};
