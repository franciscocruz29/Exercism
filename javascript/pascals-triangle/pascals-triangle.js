// 1. Understand the problem:

// What are the inputs?
// An integer, representing the number of rows to generate.

// What are the outputs?
// An array of arrays, representing the rows.

// What are the rules?
// Compute Pascal's triangle up to a given number of rows.

// 2. Examples:

// rows(0) -> []
// rows(1) -> [[1]]
// rows(3) -> [[1], [1, 1], [1, 2, 1]]
/* rows(10) -> [
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1],
  [1, 5, 10, 10, 5, 1],
  [1, 6, 15, 20, 15, 6, 1],
  [1, 7, 21, 35, 35, 21, 7, 1],
  [1, 8, 28, 56, 70, 56, 28, 8, 1],
  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
  ] */

// 3. Steps for converting input to output (Algorithm):

// 1. Create an empty list called pascals_triangle.
// 2. Loop from 0 to the given number of rows(exclusive) using a variable, say i.
// 3. In each iteration, create a new list called row with a length of i + 1.
// 4. Set the first and last elements of the row list to 1.
// 5. If i is greater than 1, loop through the elements of the previous row, and add the current element and the next element together. 
// Assign the sum to the corresponding element of the current row.
// 6. Append the row to the pascals_triangle list.
// 7. Repeat steps 3 - 6 for each row until the given number of rows is reached.
// 8. Return the pascals_triangle list.

// 4. Implementation:

/* export const rows = (rowsTriangle) => {
  const pascals_triangle = [];

  for (let i = 0; i < rowsTriangle; i++) {
    const row = new Array(i + 1).fill(1);
    if (i > 1) {
      for (let j = 1; j < pascals_triangle[i - 1].length; j++) {
        row[j] = pascals_triangle[i - 1][j - 1] + pascals_triangle[i - 1][j];
      }
    }
    pascals_triangle.push(row);
  }

  return pascals_triangle;
}; */

// 5. Refactored solution:

// This refactored code separates the concerns of generating a single row and constructing the entire Pascal's Triangle,
// making the code more modular and easier to understand.

// Helper function to generate a single row of Pascal's Triangle
function generateRow(prevRow) {
  const newRow = [1];

  for (let i = 1; i < prevRow.length; i++) {
    newRow.push(prevRow[i - 1] + prevRow[i]);
  }

  newRow.push(1);

  return newRow;
}

// Function to generate Pascal's Triangle with the given number of rows
export const rows = (rowsTriangle) => {
  const pascalsTriangle = [];

  for (let i = 0; i < rowsTriangle; i++) {
    const newRow = i === 0 ? [1] : generateRow(pascalsTriangle[i - 1]);
    pascalsTriangle.push(newRow);
  }

  return pascalsTriangle;
};
