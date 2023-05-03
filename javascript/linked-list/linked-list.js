// 1. Understand the problem:

/* A project to develop a train scheduling system for a busy railway network. 
You've been asked to develop a prototype for the train routes in the scheduling system. 
Each route consists of a sequence of train stations that a given train stops at. */

/* 
- The team has decided to use a --doubly linked list-- to represent each train route in the schedule. Each station along the train's route will be represented by a node in the linked list.

- You don't need to worry about arrival and departure times at the stations. Each station will simply be represented by a number.

- Routes can be extended, adding stations to the beginning or end of a route. They can also be shortened by removing stations from the beginning or the end of a route.

- Sometimes a station gets closed down, and in that case the station needs to be removed from the route, even if it is not at the beginning or end of the route.

- The size of a route is measured not by how far the train travels, but by how many stations it stops at. 
*/

// 1.1 Concepts:

/* The basic idea behind a --linked list-- is that it consists of a series of "nodes," 
where each node contains both the data to be stored and a reference (or "pointer") to the next node in the list. 

For example, imagine you have three numbers you want to store in a linked list: 5, 10, and 15. 
You would create three nodes, each containing one of the numbers and a reference to the next node:

Node 1: 5 --> Node 2
Node 2: 10 --> Node 3
Node 3: 15 --> Null (because there is no next node)
*/

/* A --doubly linked list-- is a type of linked list data structure where each node has two references or pointers instead of one.
So, if we continue with the example of the linked list containing the numbers 5, 10, and 15, a doubly linked list would look like this:

Node 1: null <-- 5 --> Node 2
Node 2: Node 1 <-- 10 --> Node 3
Node 3: Node 2 <-- 15 --> null
 */

// 2. Design the data structure and implementation:

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

export class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  // Add a new node to the end of the list
  push(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.prev = this.tail;
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
  }

  // Remove the last node from the list and return its value
  pop() {
    if (!this.tail) return null;
    const poppedNode = this.tail;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = poppedNode.prev;
      this.tail.next = null;
      poppedNode.prev = null;
    }
    this.length--;
    return poppedNode.value;
  }

  // Remove the first node from the list and return its value
  shift() {
    if (!this.head) return null;
    const shiftedNode = this.head;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = shiftedNode.next;
      this.head.prev = null;
      shiftedNode.next = null;
    }
    this.length--;
    return shiftedNode.value;
  }

  // Add a new node to the beginning of the list
  unshift(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head.prev = newNode;
      this.head = newNode;
    }
    this.length++;
  }

  // Remove the first node from the list that matches the given value
  delete(value) {
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.value === value) {
        if (this.length === 1) {
          this.head = null;
          this.tail = null;
        } else if (currentNode === this.head) {
          this.head = currentNode.next;
          this.head.prev = null;
        } else if (currentNode === this.tail) {
          this.tail = currentNode.prev;
          this.tail.next = null;
        } else {
          currentNode.prev.next = currentNode.next;
          currentNode.next.prev = currentNode.prev;
        }
        this.length--;
        return;
      }
      currentNode = currentNode.next;
    }
  }

  // Return the number of nodes in the list
  count() {
    return this.length;
  }
}

