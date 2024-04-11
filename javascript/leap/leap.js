// Algorithm to Determine Leap Year

//  Input: A positive integer representing the year
//  Output: A boolean indicating whether the year is a leap year or not

// 1. Check if the year is a positive integer.
//    a.If not, return an error indicating that the input is invalid.
//    b.If yes, proceed to the next step.

// 2. Check if the year is divisible by 4.
//    a.If not, the year is not a leap year.
//      i.Return False.
//    b.If yes, proceed to the next step.

// 3. Check if the year is divisible by 100.
//    a.If yes, check if the year is also divisible by 400.
//      i.If yes, the year is a leap year.
//        - Return True.
//      ii.If not, the year is not a leap year.
//        - Return False.
//     b.If no, the year is a leap year.
//      i.Return True.

export const isLeap = (year) => {
  if (!Number.isInteger(year) || year <= 0) {
    throw new Error('Invalid input: Year must be a positive integer.');
  }

  const isDivisibleBy = (divisor) => year % divisor === 0;

  const isDivisibleBy400 = isDivisibleBy(400);
  const isDivisibleBy100 = isDivisibleBy(100);
  const isDivisibleBy4 = isDivisibleBy(4);

  if (isDivisibleBy100) {
    return isDivisibleBy400;
  }

  return isDivisibleBy4;
};
