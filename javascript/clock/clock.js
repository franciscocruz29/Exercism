// Step 1 - Problem Understanding:

// Inputs: Hours and minutes (integers, can be positive or negative)
// Outputs: String representation of time, Clock objects for addition/subtraction, boolean for equality comparison

// Explicit Requirements and Rules:
// - The clock must handle time in a 24-hour format (00:00 to 23:59).
// - Ability to add and subtract minutes
// - Equal representation for the same time
// - Handle time rollover (past midnight or before midnight)
// - The clock must handle negative values for both hours and minutes, adjusting accordingly.
// - No use of built-in Date class

// Mental model:
// A clock face that operates on a 24-hour cycle.
// You can add or subtract minutes to adjust the time.
// If you exceed 24 hours or drop below 0, the time wraps around.
// You also need a way to check if two clocks show the same time, regardless of how the time was reached.

// Step 2 - Examples and Test Cases:

// a) Basic time representation:
// new Clock(8).toString() => "08:00"
// new Clock(11, 9).toString() => "11:09"

// b) Time rollover:
// new Clock(25, 0).toString() => "01:00"
// new Clock(0, 160).toString() => "02:40"

// c) Negative time handling:
// new Clock(-25, -160).toString() => "20:20"
// new Clock(1, -4820).toString() => "16:40"

// Step 3 - Algorithm Design:

// 1. Normalize Time Input:
//    - When the Clock is initialized with hours and minutes, ensure both values are within valid bounds.
//    - The constructor takes in hours and minutes, converts them to total minutes, and then uses modulus to get the equivalent minute within a day. If the total minutes is negative, it adds 24*60 to get the positive equivalent. It then calculates the actual hour and minute by dividing total minutes by 60.
// 2. String Representation:
//    - Ensure that the toString method returns the time in "HH:MM" format, padding hours and minutes as necessary.
// 3. Handle Addition and Subtraction:
//    - Create a method to add minutes (plus) by converting hours and minutes into total minutes, adjusting for the addition, and then recalculating hours and minutes from the total.
//    - Similarly, for subtraction (minus), convert the clock time into total minutes, subtract, and then adjust back to valid hour/minute values.
// 4. Equality Check:
//    - Define an equals method that compares two Clock instances by checking if their hours and minutes are the same after normalizing them.

// Step 4 - Implementation:

export class Clock {
  constructor(hour, minute = 0) {
    // Normalize the time during initialization
    const totalMinutes = hour * 60 + minute;
    this.hour = Math.floor((((totalMinutes / 60) % 24) + 24) % 24);
    this.minute = ((totalMinutes % 60) + 60) % 60;
  }

  // Method to return the time in "HH:MM" format
  toString() {
    const paddedHour = this.hour.toString().padStart(2, "0");
    const paddedMinute = this.minute.toString().padStart(2, "0");
    return `${paddedHour}:${paddedMinute}`;
  }

  // Method to add minutes to the clock
  plus(minutes) {
    return new Clock(this.hour, this.minute + minutes);
  }

  // Method to subtract minutes from the clock
  minus(minutes) {
    return new Clock(this.hour, this.minute - minutes);
  }

  // Method to compare if two clocks are equal
  equals(other) {
    return this.hour === other.hour && this.minute === other.minute;
  }
}
