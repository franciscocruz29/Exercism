// Step 1 - Problem Understanding:

// * What are the expected inputs?
//    * Data type: Object
//    * Description: An object where keys are numerical scores (points) and values are arrays of uppercase letters representing letters that share the same score.

// * What are the expected outputs?
//    * Data type: Object
//    * Description: An object where keys are individual letters (lowercase) and values are numerical scores.

// * What are the key rules or constraints?
//    * The transformation involves changing from a score-to-letters mapping (one-to-many) to a letter-to-score mapping (one-to-one).
//      - {1: ["A", "E"], 2: ["D", "G"]} -> {"a": 1, "d": 2, "e": 1, "g": 2}
//    * Letters should be stored in lowercase in the new format
//    * The goal is to transform the legacy data format to the new format. The transformation must preserve accuracy—each letter retains its original score.

// * What is the mental model?
//    * A reorganization of data that maintains the same information but in a format better suited for the game's expanded language support.

// Step 2 - Examples:

// Input: { 1: ["A"] }
// Output: { a: 1 }

// Input: {
//    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
//    2: ["D", "G"],
//    3: ["B", "C", "M", "P"],
//    4: ["F", "H", "V", "W", "Y"],
//    5: ["K"],
//    8: ["J", "X"],
//    10: ["Q", "Z"],
//  };
// Output: {
//    a: 1,
//    b: 3,
//    c: 3,
//    d: 2,
//    e: 1,
//    f: 4,
//    g: 2,
//    h: 4,
//    i: 1,
//    j: 8,
//    k: 5,
//    l: 1,
//    m: 3,
//    n: 1,
//    o: 1,
//    p: 3,
//    q: 10,
//    r: 1,
//    s: 1,
//    t: 1,
//    u: 1,
//    v: 4,
//    w: 4,
//    x: 8,
//    y: 4,
//    z: 10,
//  };

// Step 3 - Strategies:

// 1. Direct iteration approach
// This involves directly iterating through the original data structure, processing each key-value pair, and building the new data structure.

// 2. Functional programming approach
// Using higher-order functions like reduce, map, and flatMap to transform the data structure in a more declarative way.

// Step 4 - Algorithm design for the Direct iteration approach:

// 1. Initialze an empty object called letterScores to store our results
// 2. For each key-value pair in the input object:
//    a. Extract the score (key) and the array of letters (value)
//    b. For each letter in the array:
//       i. Convert the letter to lowercase
//       ii. Add a new entry to letterScores with the lowercase letter as the key and the scores as the values
// 3. Return the letterScores object

// Step 5 - Implementation:

export const transform = (legacyScores) => {
  let letterScores = {};

  for (const [score, letters] of Object.entries(legacyScores)) {
    for (const letter of letters) {
      letterScores[letter.toLowerCase()] = Number(score);
    }
  }

  return letterScores;
};
