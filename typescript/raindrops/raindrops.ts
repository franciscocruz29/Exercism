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

// 1. Create a function that accepts a number (integer) as input.
// 2. Initialize an empty string to accumulate the raindrop sounds.
// 3. Define an array of objects that maps factors to their corresponding raindrop sounds.
//    - Each object will contain a factor (number) and a sound (string).
// 4. Iterate over the array:
//    - For each object, check if the number is divisible by the factor.
//    - If the number is divisible by the factor, append the corresponding sound to the result string.
// 5. Check the result:
//    - If no sounds were added (i.e., the result string is empty), return the number itself as a string.
// 6. Return the result, which will either be the raindrop sounds or the number as a string.

// Step 4: Implementation

/* export function convert(number: number): string {
  let result = "";

  const factors: { factor: number; sound: string }[] = [
    { factor: 3, sound: "Pling" },
    { factor: 5, sound: "Plang" },
    { factor: 7, sound: "Plong" },
  ];

  factors.forEach((pair) => {
    if (number % pair.factor === 0) {
      result += pair.sound;
    }
  });

  return result || number.toString();
} */

// Step 5: Refactor
export function convert(num: number): string {
  return (
    (num % 3 === 0 ? "Pling" : "") +
      (num % 5 === 0 ? "Plang" : "") +
      (num % 7 === 0 ? "Plong" : "") || `${num}`
  );
}
