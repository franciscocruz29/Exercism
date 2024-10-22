// Step 1 - Problem Understanding:
//
// * What are the expected inputs?
//    - year: A four-digit integer representing the year.
//    - month: An integer representing the month
//    - week: A string representing the week ("first", "second", "third", "fourth", "last", "teenth").
//    - weekday: A string representing the weekday ("Monday")
//
// * What are the expected outputs?
//    - A specific date (Date object), which corresponds to the provided week and day in that month.
//
// * What are the key rules or constraints?
//    - There are five week values to consider: first, second, third, fourth, last, teenth
//    - The teenth week refers to the seven days in a month that end in '-teenth' (13th, 14th, 15th, 16th, 17th, 18th and 19th)
//    - Months are 0-indexed in the Date object (January is 0, December is 11)
//
// * What is the mental model?
//    - Think of a calendar grid. We're finding a specific cell based on the month, year, and a set of rules for selecting the row (week) and column (day of the week).

// Step 2 - Examples:
//
// Input: (2013, 4, "first", "Monday")
// Output: new Date(2013, 3, 1)) -> Mon Apr 01 2013
//
// Input: (2013, 7, "second", "Wednesday")
// Output: new Date(2013, 6, 10) -> Wed Jul 10 2013
//
// Input: (2013, 5, "third", "Tuesday")
// Output: new Date(2013, 4, 21)) -> Tue May 21 2013
//
// Input: (2013, 9, "fourth", "Thursday")
// Output: new Date(2013, 8, 26) -> Thu Sep 26 2013
//
// Input: (2013, 11, "last", "Friday")
// Output: new Date(2013, 10, 29) -> Fri Nov 29 2013
//
// Input: (2013, 2, "teenth", "Saturday")
// Output: new Date(2013, 1, 16) -> Sat Feb 16 2013

// Step 3 - Data Structure Selection:
//
// The Date object in JavaScript is the most suitable data structure for this problem.
// It provides built-in methods for working with dates, such as setting specific components (year, month, date) and getting the day of the week.

// Step 4 - Algorithm Design:
//
// 1. Convert the day of the week to a number:
//    - Create a mapping of day names to numbers
// 2. Find the First Occurrence of the Day in the Month:
//    - Create a Date object for the first day of the target month and year
//    - Calculate how many days to add to reach the first target day of week (targetDay - firstDayOfMonth.getDay() + 7) % 7
//    - Create a new Date with this calculated first occurrence
// 3. Adjust the Date Based on the Week Descriptor
//    - For "second": Add 7 days to the first occurrence
//    - For "third": Add 14 days to the first occurrence
//    - For "fourth": Add 21 days to the first occurrence
//    - For "last":
//      - Start with first occurrence
//      - Keep adding 7 days until adding another week would put us in the next month
//      - The last valid date is our answer
//    - For "teenth" (13th through 19th):
//      - Start with first occurrence
//      - Keep adding 7 days until we reach a date between 13 and 19
//      - That date is our answer
// 4. Return the Calculated Date.

// Step 5 - Implementation:
//
export const meetup = (year, month, week, dayOfWeek) => {
  const DAYS_IN_WEEK = 7;
  const TEENTH_START = 13;

  const daysOfWeek = {
    Sunday: 0,
    Monday: 1,
    Tuesday: 2,
    Wednesday: 3,
    Thursday: 4,
    Friday: 5,
    Saturday: 6,
  };

  const findFirstDayOfMonth = (targetYear, targetMonth, targetDay) => {
    const firstDayOfMonth = new Date(targetYear, targetMonth - 1, 1);
    const daysUntilTarget =
      (targetDay - firstDayOfMonth.getDay() + DAYS_IN_WEEK) % DAYS_IN_WEEK;
    return new Date(targetYear, targetMonth - 1, 1 + daysUntilTarget);
  };

  const addWeeks = (date, numberOfWeeks) => {
    const newDate = new Date(date);
    newDate.setDate(newDate.getDate() + numberOfWeeks * DAYS_IN_WEEK);
    return newDate;
  };

  const findLastOccurrence = (date, targetMonth) => {
    let lastOccurrence = date;
    let nextWeek = addWeeks(lastOccurrence, 1);

    while (nextWeek.getMonth() === targetMonth - 1) {
      lastOccurrence = nextWeek;
      nextWeek = addWeeks(lastOccurrence, 1);
    }

    return lastOccurrence;
  };

  const findTeenth = (date) => {
    while (date.getDate() < TEENTH_START) {
      date = addWeeks(date, 1);
    }
    return date;
  };

  const targetDay = daysOfWeek[dayOfWeek];
  let result = findFirstDayOfMonth(year, month, targetDay);

  switch (week) {
    case "second":
      result = addWeeks(result, 1);
      break;
    case "third":
      result = addWeeks(result, 2);
      break;
    case "fourth":
      result = addWeeks(result, 3);
      break;
    case "last":
      result = findLastOccurrence(result, month);
      break;
    case "teenth":
      result = findTeenth(result);
      break;
  }

  return result;
};
