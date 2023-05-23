// Implement basic list operations.

// append -> given two lists, add all items in the second list to the end of the first list
// concatenate -> given a series of lists, combine all items in all lists into one flattened list
// filter -> given a predicate and a list, return the list of all items for which predicate(item) is True
// length -> given a list, return the total number of items within it


export class List {
  constructor(elements = []) {
    this.values = elements;
  }

  append(otherList) {
    // Create a new array that contains all elements from both lists.
    const combinedValues = [...this.values, ...otherList.values];

    // Return a new List that uses the combined array.
    return new List(combinedValues);
  }

  concat(listOfLists) {
    let newList = new List([...this.values]);

    for (let list of listOfLists.values) {
      // If the element is a List, unpack its values recursively.
      if (list instanceof List) {
        newList = newList.concat(list);
      } else {
        // If the element is not a List, add it directly to newList.
        newList.values = [...newList.values, list];
      }
    }

    return newList;
  }

  filter(predicate) {
    // Initialize an empty array to store the values for the new list.
    let filteredListValues = [];

    // Iterate over each value in the original list.
    for (let i = 0; i < this.values.length; i++) {
      // Apply the predicate to the current value. 
      // If the predicate returns true, add the current value to the new list.
      if (predicate(this.values[i])) {
        // Use the spread operator to create a new array that includes 
        // all previous elements from filteredListValues and the current value.
        filteredListValues = [...filteredListValues, this.values[i]];
      }
    }

    // Create and return a new List that uses the filtered values.
    return new List(filteredListValues);
  }

  map() {
    throw new Error('Remove this statement and implement this function');
  }

  length() {
    let length = 0;

    // Iterate over each value in the list.
    for (let i = 0; i < this.values.length; i++) {
      length += 1;
    }

    return length;
  }

  foldl() {
    throw new Error('Remove this statement and implement this function');
  }

  foldr() {
    throw new Error('Remove this statement and implement this function');
  }

  reverse() {
    throw new Error('Remove this statement and implement this function');
  }
}
