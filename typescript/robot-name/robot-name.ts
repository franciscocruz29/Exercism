// Understand the problem:

// You need to create a system for managing robot factory settings. Each robot is initially unnamed when it is manufactured.
// When a robot is turned on for the first time, it gets a randomly generated name.
// This name consists of two uppercase letters followed by three digits, like "AB123" or "XY789".

// Sometimes, a robot needs to be reset to its factory settings, which erases its current name.
// After the reset, when you ask for the robot's name, it should generate and respond with a new random name.

// It's important that the robot names are random and not predictable.
// However, using random names means that sometimes two robots might end up with the same name (a collision).
// Your solution must ensure that every robot has a unique name at any given time.

// Step by step

// The class Robot is created, and it includes some static properties and methods, as well as instance properties and methods.
// public static names: Set<string>: This is a static property that stores a set of unique robot names.
// public static readonly LETTERS: string and public static readonly NUMBERS: string: These are static properties that store the set of uppercase letters and digits as strings, respectively.
// private _name: string: This is a private instance property that holds the name of a specific robot.
// constructor(): The constructor initializes the Robot.names set and generates a random name for the robot instance using the Robot.randomName() method.
// public get name(): string: This is a getter method for the robot's name. It returns the current robot name.
// public resetName(): void: This method resets the robot's name by generating a new random name using the Robot.randomName() method.
// private static randomName(): string: This method generates a random robot name by combining two random letters and three random numbers. It checks if the generated name is unique (not in the Robot.names set) and adds it to the set before returning the name.
// private static randomChars(count: number, source: string): string: This method takes a count and a source string as input and returns a string of random characters from the source string with the specified count.
// public static releaseNames(): void: This method clears the Robot.names set, effectively releasing all robot names.

// A high-level overview of the code's logic:

// A new robot is created with the Robot class.
// The constructor generates a random name for the robot.
// The robot's name can be accessed using the name getter.
// The robot's name can be reset using the resetName() method.
// The random name generation ensures uniqueness by checking and storing names in the Robot.names set.
// You can release all robot names using the releaseNames() method.

export class Robot {
  public static names: Set<string>;
  public static readonly LETTERS: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  public static readonly NUMBERS: string = "0123456789";
  private _name: string;

  constructor() {
    Robot.names = new Set<string>();
    this._name = Robot.randomName();
  }

  public get name(): string {
    return this._name;
  }

  public resetName(): void {
    this._name = Robot.randomName();
  }

  private static randomName(): string {
    let name: string;
    do {
      const letters = Robot.randomChars(2, Robot.LETTERS);
      const numbers = Robot.randomChars(3, Robot.NUMBERS);
      name = `${letters}${numbers}`;
    } while (Robot.names.has(name));
    Robot.names.add(name);
    return name;
  }

  private static randomChars(count: number, source: string): string {
    let chars = "";
    for (let i = 0; i < count; i++) {
      const index = Math.floor(Math.random() * source.length);
      chars += source.charAt(index);
    }
    return chars;
  }

  public static releaseNames(): void {
    this.names.clear();
  }
}
