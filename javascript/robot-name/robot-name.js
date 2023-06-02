// Understand the problem:

// You need to create a system for managing robot factory settings. Each robot is initially unnamed when it is manufactured.
// When a robot is turned on for the first time, it gets a randomly generated name.
// This name consists of two uppercase letters followed by three digits, like "AB123" or "XY789".

// Sometimes, a robot needs to be reset to its factory settings, which erases its current name.
// After the reset, when you ask for the robot's name, it should generate and respond with a new random name.

// It's important that the robot names are random and not predictable.
// However, using random names means that sometimes two robots might end up with the same name (a collision).
// The solution must ensure that every robot has a unique name at any given time.

export class Robot {
  // Static variable to store used names
  static names = new Set();

  constructor() {
    // Generate a name and assign it to the robot
    this._name = this.generateUniqueName();
  }

  // Getter for the name
  get name() {
    // Ensuring internal name cannot be modified by returning a new string
    return String(this._name);
  }

  // Generate unique name
  generateUniqueName() {
    let newName = '';

    do {
      newName = this.generateRandomName();
    } while (Robot.names.has(newName));  // Keep generating until a unique name is found

    Robot.names.add(newName);  // Store the unique name

    return newName;
  }

  // Generate random name in the format of two uppercase letters followed by three digits
  generateRandomName() {
    return (
      String.fromCharCode(65 + Math.floor(Math.random() * 26)) + // A-Z
      String.fromCharCode(65 + Math.floor(Math.random() * 26)) + // A-Z
      String(Math.floor(Math.random() * 10)) + // 0-9
      String(Math.floor(Math.random() * 10)) + // 0-9
      String(Math.floor(Math.random() * 10))   // 0-9
    );
  }

  // Reset name
  reset() {
    // Generate and assign a new name
    this._name = this.generateUniqueName();
  }

  // Release all names
  static releaseNames() {
    Robot.names.clear();
  }
}

