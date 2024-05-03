// 1. Understand the problem:

// What is the input ?
//  A number between 1 and 31.

// What is the output ?
//   A sequential actions comprising the secret handshake, presented in the form of a list of strings.

// What are the rules ?
//   The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary.
//   Start at the right - most digit and move left.

//     The actions for each number place are:

//     00001 = wink
//     00010 = double blink
//     00100 = close your eyes
//     01000 = jump;
//     10000 = Reverse the order of the operations in the secret handshake.

// 2. Examples:

// 9 in binary is 1001.

// The digit that is farthest to the right is 1, so the first action is wink.
// Going left, the next digit is 0, so there is no double - blink.
// Going left again, the next digit is 0, so you leave your eyes open.
// Going left again, the next digit is 1, so you jump.

// That was the last digit, so the final code is:
// ["wink", "jump"]

// Given the number 26, which is 11010 in binary, we get the following actions:

// double blink;
// jump
// reverse actions

// That was the last digit, so the final code is:
// ["jump", "double blink"];

// 3. Algorithm:

// 1. Create a empty list to store the actions;
// 2. Convert the number to binary and store it in a string.
// 3. For each digit in the binary string,
//      3.1 Check the rightmost digit of the binary string. If it is '1', append the string "wink" to the actions list.
//      3.2 Check the second rightmost digit of the binary string. If it is '1', append the string "double blink" to the actions list.
//      3.3 Check the third rightmost digit of the binary string. If it is '1', append the string "close your eyes" to the actions list.
//      3.4 Check the fourth rightmost digit of the binary string. If it is '1', append the string "jump" to the actions list.
//      3.5 Check the leftmost digit of the binary string. If it is '1', reverse the order of the elements in the actions list using the reverse() method.
// 4. Return the actions list.

// 4. Implementation:
export function commands(num: number): string[] {
  const actions: string[] = [];
  const binary = num.toString(2).padStart(5, "0");

  if (binary[4] === "1") {
    actions.push("wink");
  }
  if (binary[3] === "1") {
    actions.push("double blink");
  }
  if (binary[2] === "1") {
    actions.push("close your eyes");
  }
  if (binary[1] === "1") {
    actions.push("jump");
  }
  if (binary[0] === "1") {
    actions.reverse();
  }
  return actions;
}
