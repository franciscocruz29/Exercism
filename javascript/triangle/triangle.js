// 1. Understand the problem:

// What is the input? 
// A triangle object with three properties: side1, side2, and side3

// What is the output? 
// True if a triangle is equilateral, isosceles, or scalene otherwise False

// What are the rules?
// A triangle is equilateral if all three sides are equal
// A triangle is isosceles if two sides are equal
// A triangle is scalene if all three sides are different
// For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side:
//  a + b ≥ c
//  b + c ≥ a
//  a + c ≥ b

// 2. Examples:

// Equilateral triangle:

// Input: new Triangle(2, 2, 2)
// Output: true

// Input: new Triangle(0, 0, 0);
// Output: false

// Isosceles triangle:

// Input: new Triangle(3, 4, 4);
// Output: true

// Input: new Triangle(3, 1, 1);
// Output: false

// Scalene triangle:

// Input: new Triangle(5, 4, 6);
// Output: true

// Input: new Triangle(7, 3, 2);
// Output: false

// 3. Algorithm:

// 1. Validate Triangle:
//    1.1 Verify that all sides of the triangle have lengths greater than 0.
//    1.2 Ensure that the sum of the lengths of any two sides is greater than the length of the third side.
//    1.3 If any of these conditions fail, return false.

// 2. Identify Triangle Type:
//    2.1 If all sides are equal, the triangle is equilateral.
//    2.2 If exactly two sides are equal, the triangle is isosceles.
//    2.3 If all sides are different, the triangle is scalene.

// 3. Not a Triangle:
//    3.1 If the validation step fails (step 1), or none of the triangle type conditions are met (step 2), the provided input doesn't represent a valid triangle. Return False.


// 4. Implementation:
/* export class Triangle {
  constructor(...sides) {
    this.sides = sides;
  }

  isValidTriangle() {
    const [a, b, c] = this.sides;
    return (
      a > 0 &&
      b > 0 &&
      c > 0 &&
      a + b > c &&
      b + c > a &&
      a + c > b
    );
  }
  get isEquilateral() {
    const [a, b, c] = this.sides;
    return this.isValidTriangle() && a === b && b === c;
  }

  get isIsosceles() {
    const [a, b, c] = this.sides;
    return this.isValidTriangle() && (a === b || b === c || a === c);
  }

  get isScalene() {
    const [a, b, c] = this.sides;
    return this.isValidTriangle() && a !== b && b !== c && a !== c;
  }
} */

// 5. Refactor:

export class Triangle {
  constructor(...sides) {
    this.sides = sides;
  }

  isValidTriangle() {
    const [a, b, c] = this.sides;
    const isPositive = (side) => side > 0;
    const satisfiesTriangleInequality = (x, y, z) => x + y > z;

    return (
      this.sides.every(isPositive) &&
      satisfiesTriangleInequality(a, b, c) &&
      satisfiesTriangleInequality(b, c, a) &&
      satisfiesTriangleInequality(a, c, b)
    );
  }

  get isEquilateral() {
    const [a, b, c] = this.sides;
    return this.isValidTriangle() && a === b && b === c;
  }

  get isIsosceles() {
    const [a, b, c] = this.sides;
    return this.isValidTriangle() && (a === b || b === c || a === c);
  }

  get isScalene() {
    const [a, b, c] = this.sides;
    return this.isValidTriangle() && a !== b && b !== c && a !== c;
  }
}
