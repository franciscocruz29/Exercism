// Understand the problem:

// What are the inputs?
// Array of integers, that represents a popular 5 book series

// What are the outputs?
// Integer, that represents the total cost of the series after applying the discount

//What are the rules for applying the discount?
// One copy of any of the five books costs $8
// If, you buy two different books, you get a 5% discount on those two books.
// If, you buy three different books, you get a 10% discount on those three books.
// If you buy 4 different books, you get a 20% discount.
// If you buy 5 different books, you get a 25% discount.

// if you buy four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set,
// but the fourth book still costs $8.

// Goal:
// Write a function that calculates the price of any conceivable shopping basket (containing only books of the same series),
// giving as big a discount as possible.

// Rules:
// The cost will return the total cost (after discounts) in cents.
// For example, for a single book, the cost is 800 cents, which equals $8.00.

// Examples:
// cost([1]) === 800
// cost([2, 2]) === 1600
// cost([1, 2]) === 1520 (5% discount => 1600*(1-(5/100)) = 1520)

// cost([1, 1, 2, 2, 3, 3, 4, 5])

// One way of grouping these 8 books is:
// 1 group of 5 --> 25% discount(1st, 2nd, 3rd, 4th, 5th)
// +1 group of 3 --> 10% discount(1st, 2nd, 3rd)
// This would give a total cost of:
// 5 books at a 25% discount
// 3 books at a 10% discount
// 5 * 800 = 4000*(1-(25/100)) = 3000
// 3 * 800 = 2400*(1-(10/100)) = 2160
// The total cost is: 3000 + 2160 = 5160

// However, a different way to group these 8 books is:
// 1 group of 4 books --> 20% discount (1st,2nd,3rd,4th)
// +1 group of 4 books --> 20% discount (1st,2nd,3rd,5th)
// This would give a total cost of:
// 4 books at a 20% discount
// 4 books at a 20% discount

// 4 * 800 = 3200*(1-(20/100)) = 2560
// 4 * 800 = 3200*(1-(20/100)) = 2560
// The total cost is: 2560 + 2560 = 5120

// And 5120 is the price with the biggest discount.

// What is the pseudo-code for the problem?:

// The cost function accepts a books array as an input, which represents the basket of books.
// Calculate the baseCost by multiplying the total number of books by 800(the price of one book).
// Define the discounts object to store the discount percentages for different unique book sets(2 to 5).
// Initialize an empty array uniqueBooksSets to store the sizes of unique book sets found in the basket.
// In a while loop, continue processing the books array until it is empty.
//   a.Create a uniqueBooks Set to store the unique book numbers in the current iteration.
//     b.Add the size of uniqueBooks to the uniqueBooksSets array.
//       c.Remove the unique books found in the current iteration from the books array.
// In a while loop, optimize the discount by checking if there are sets of 3 and 5 unique books.If found, replace them with two sets of 4 unique books.
// Calculate the totalDiscount by iterating through the uniqueBooksSets array and summing up the discounts applied for each unique book set.
// Return the final cost after applying the total discount to the base cost.

export const cost = (books) => {
  let baseCost = books.length * 800;
  const discounts = { 5: 0.25, 4: 0.2, 3: 0.1, 2: 0.05 };
  const uniqueBooksSets = [];
  // Step 5
  while (books.length > 0) {
    const uniqueBooks = new Set(books);
    uniqueBooksSets.push(uniqueBooks.size);
    for (let b of uniqueBooks) {
      books.splice(books.indexOf(b), 1);
    }
  }
  // Step 6
  while (uniqueBooksSets.includes(3) && uniqueBooksSets.includes(5)) {
    uniqueBooksSets.splice(uniqueBooksSets.indexOf(3), 1);
    uniqueBooksSets.splice(uniqueBooksSets.indexOf(5), 1);
    uniqueBooksSets.push(4, 4);
  }
  // Step 7
  const totalDiscount = uniqueBooksSets.reduce((prev, curr) => {
    return prev + (discounts[curr] || 0) * 800 * curr;
  }, 0);
  // Step 8
  return baseCost - totalDiscount;
};

/* This code calculates the total cost of the basket of books by applying the maximum possible discount.
It optimizes the discount by replacing sets of 3 and 5 unique books with two sets of 4 unique books, which results in a higher discount. */


