// 1. Understand the problem:

//  What is the input ?
//    A string that contains a simple math word problem

//  What is the output ?
//    A integer that represents the answer to the math problem

//  What are the rules ?
//  1. Problems with no operations simply evaluate to the number given.

//  2. Addition, Subtraction, Multiplication and Division
//      They have the following structure: "What is X operation Y?"
//      Where X is the first number, Y is the second number, and operation is the operation to be performed.

//  3. Multiple Operations:
//      Handle a set of operations, in sequence.
//      Since these are verbal word problems, evaluate the expression from left - to - right, ignoring the typical order of operations.

//  4. The parser should reject:
//      Unsupported operations("What is 52 cubed?");
//      Non - math questions("Who is the President of the United States")
//      Word problems with invalid syntax("What is 1 plus plus 2?")

//  What are the requirements?
//    - Parse and evaluate simple math word problems returning the answer as an integer

//    - This exercise requires that you use the raise statement to "throw" a ValueError 
//      if the question passed to answer() is malformed / invalid, or contains an unknown operation.
//      The tests will only pass if you both raise the exception and include a message with it.


//  2. Test cases and examples:

//  Rule 1:
//    Input: "What is 5?";
//    Output: 5

//  Rule 2:
//    Input: "What is 5 plus 5?";
//    Output: 10;

//    Input: "What is 4 minus -12?";
//    Output: 16;

//    Input: "What is -3 multiplied by 25?";
//    Output: -75;

//    Input: "What is 33 divided by -3?";
//    Output: -11

//  Rule 3:
//    Input: "What is 1 plus 1 plus 1?";
//    Output: 3;

//    Input: "What is 2 multiplied by -2 multiplied by 3?";
//    Output: -12;

//    Input: "What is -3 plus 7 multiplied by -2?";
//    Output: -8

//  Rule 4:
//    Input: "What is 52 cubed?";
//    Output: ValueError("Unknown operation");

//    Input: "What is?";
//    Output: ValueError("Syntax error");

//    Input: "What is 1 plus plus 2?";
//    Output: ValueError("Syntax error")

// 3. Algorithm and Implementation:

// Define the operations that are supported
const OPERATIONS = {
  'plus': (a, b) => a + b,
  'minus': (a, b) => a - b,
  'multiplied': (a, b) => a * b,
  'divided': (a, b) => a / b
};

// Function to check if a string is a number
function isNumber(token) {
  return !isNaN(token);
}

// Main function to process the question and return the answer
export function answer(question) {
  // Remove the question mark from the question and split it into words
  const tokens = question.replace('?', '').split(' ');

  // If the question has less than 3 words, throw a Syntax Error
  if (tokens.length < 3) {
    throw new Error('Syntax error');
  }

  // Initialize an empty array to store the expression
  let expression = [];

  // Iterate over each word in the question
  for (let token of tokens) {
    // If the word is a number or an operation, add it to the beginning of the expression array
    if (isNumber(token) || OPERATIONS[token]) {
      expression.unshift(token);
    }
    // If the word is not 'What', 'is', or 'by', throw an Unknown Operation error
    else if (!['What', 'is', 'by'].includes(token)) {
      throw new Error('Unknown operation');
    }
  }

  // Check the expression array for syntax errors
  for (let index in expression) {
    // If an index is even and the word at that index is not a number, throw a Syntax Error
    // If an index is odd and the word at that index is not an operation, throw a Syntax Error
    if ((index % 2 === 0 && !isNumber(expression[index])) || (index % 2 !== 0 && !OPERATIONS[expression[index]])) {
      throw new Error('Syntax error');
    }
  }

  // Pop the last number from the expression array and store it in the result variable
  let result = parseInt(expression.pop(), 10);

  // Loop until the expression array is empty
  while (expression.length) {
    // Pop an operation and a number from the expression array
    let operation = OPERATIONS[expression.pop()];
    let number = parseInt(expression.pop(), 10);

    // Perform the operation on the result and the number
    result = operation(result, number);
  }

  // Return the result as an integer
  return Math.floor(result);
}
