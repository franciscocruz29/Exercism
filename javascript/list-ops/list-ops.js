// Implement basic list operations.

// append -> given two lists, add all items in the second list to the end of the first list
// concatenate -> given a series of lists, combine all items in all lists into one flattened list
// filter -> given a predicate and a list, return the list of all items for which predicate(item) is True
// length -> given a list, return the total number of items within it
// map -> given a function and a list, return the list of the results of applying function(item) on all items
// oldl -> given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left using function(accumulator, item)
// foldr -> given a function, a list, and an initial accumulator, fold(reduce) each item into the accumulator from the right using function (item, accumulator)
// reverse -> given a list, return a list with all the original items, but in reversed order

export class List {
  constructor(elements = []) {
    this.values = elements;
  }

  append(otherList) {
    // Step 1: Create a new array that contains all elements from both lists.
    const combinedValues = [...this.values, ...otherList.values];

    // Step 2: Return a new List that uses the combined array.
    return new List(combinedValues);
  }

  concat(listOfLists) {
    // Step 1: Start with a new List that contains the same elements as the current List.
    let newList = new List([...this.values]);

    // Step 2: Iterate over each List in the listOfLists.
    for (let list of listOfLists.values) {
      // Step 3: Check if the current element is a List.
      if (list instanceof List) {
        // If it is, recursively append its elements to newList.
        newList = newList.concat(list);
      } else {
        // If it's not, append it directly to newList.
        newList.values = [...newList.values, list];
      }
    }

    // Step 4: Return the final List.
    return newList;
  }

  filter(predicate) {
    // Step 1: Initialize an empty array to store the values for the new list.
    let filteredListValues = [];

    // Step 2: Iterate over each value in the original list.
    for (let i = 0; i < this.values.length; i++) {
      // Step 3: Apply the predicate to the current value.
      // If the predicate returns true, add the current value to the new list.
      if (predicate(this.values[i])) {
        filteredListValues = [...filteredListValues, this.values[i]];
      }
    }

    // Step 4: Create and return a new List that uses the filtered values.
    return new List(filteredListValues);
  }

  map(func) {
    // Step 1: Initialize an empty array to hold the result.
    const result = [];

    // Step 2: Use a for loop to iterate over `this.values`.
    for (let i = 0; i < this.values.length; i++) {
      // Step 3: Apply the function `func` to the current element,
      // and append the result to the `result` array.
      result.push(func(this.values[i]));
    }

    // Step 4: Return a new `List` instance with the result.
    return new List(result);
  }

  length() {
    // Step 1: Initialize a counter variable to 0
    let length = 0;

    // Step 2: Iterate over each value in the list.
    for (let i = 0; i < this.values.length; i++) {
      // Step 3: For each value, increment the counter by 1.
      length += 1;
    }

    // Step 4: Return the counter, which represents the length of the list.
    return length;
  }

  foldl(func, initial) {
    // Step 1: Initialize the accumulator to the initial value
    let accumulator = initial;

    // Step 2: Use a for loop to iterate over `this.values`
    for (let i = 0; i < this.values.length; i++) {
      // Step 3: Apply the function `func` to the accumulator and the current element,
      // and assign the result to the accumulator
      accumulator = func(accumulator, this.values[i]);
    }

    // Step 4: Return the accumulator
    return accumulator;
  }

  foldr(func, initial) {
    // Step 1: Initialize the accumulator to the initial value
    let accumulator = initial;

    // Step 2: Use a for loop to iterate over `this.values` in reverse order
    for (let i = this.values.length - 1; i >= 0; i--) {
      // Step 3: Apply the function `func` to the accumulator and the current element,
      // and assign the result to the accumulator
      accumulator = func(accumulator, this.values[i]);
    }

    // Step 4: Return the accumulator
    return accumulator;
  }

  reverse() {
    // Step 1: Initialize an empty array for the result
    const result = [];

    // Step 2: Use a for loop to iterate over `this.values` in reverse order
    for (let i = this.values.length - 1; i >= 0; i--) {
      // Step 3: Add the current element to the `result` array
      result.push(this.values[i]);
    }

    // Step 4: Return a new `List` instance with the result
    return new List(result);
  }
}
