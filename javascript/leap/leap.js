// Step 1: Understand the problem

// What are the inputs ?
// A postive integer that represents the year

// What are the outputs ?
// A boolean; True if the year is leap, false if the year is not leap

// What are the rules ?
// A leap year(in the Gregorian calendar) occurs:
// - The year must be divisible by 4.
// - If the year is divisible by 100, it must also be divisible by 400.

// Step 2: Examples;

// leap_year(2015) -> False;
// leap_year(1996) -> True;
// leap_year(1800) -> False;
// leap_year(2400) -> True

// Step 3: The algorithm;

// 1. Take the input year.
// 2. Check if the year is divisible by 4:
//  - If not divisible by 4, it's not a leap year. Return False.
//  - If divisible by 4, continue to step 3.;
// 3. Check if the year is divisible by 100:
//  - If not divisible by 100, it is a leap year.Return True.
//  - If divisible by 100, continue to step 4.;
// 4. Check if the year is divisible by 400:
//  - If divisible by 400, it is a leap year.Return True.
//  - If not divisible by 400, it is not a leap year.Return False.

// Step 4: The implementation

/* export const isLeap = (year) => {
  // Check divisibility by 4
  if (year % 4 !== 0) {
    return false;
  }

  // Check divisibility by 100 (except multiples of 400)
  if (year % 100 === 0 && year % 400 !== 0) {
    return false;
  }

  // If all conditions passed, it's a leap year
  return true;
}; */

// Step 5: The refactored version

/**
 * Determines if a given year is a leap year.
 * 
 * @param {number} year - The year to be checked.
 * @returns {boolean} - True if the year is a leap year, false otherwise.
 */
export const isLeap = (year) => {
  if (!Number.isInteger(year) || year < 1) {
    throw new Error('Year must be a positive integer');
  }

  return (year % 4 === 0) && (year % 100 !== 0 || year % 400 === 0);
};
