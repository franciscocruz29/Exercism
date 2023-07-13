// 1. Understand the problem:

// What are the inputs?
// A point in the target -- defined by its cartesian coordinates x and y (Real number)

// What are the outputs?
// The correct amount earned by a dart landing at that point (integer)

// What are the rules?
// The target rewards 4 different amounts of points, depending on where the dart lands:

//     If the dart lands outside the target, player earns no points(0 points).
//     If the dart lands in the outer circle of the target, player earns 1 point.
//     If the dart lands in the middle circle of the target, player earns 5 points.
//     If the dart lands in the inner circle of the target, player earns 10 points.

//     The outer circle has a radius of 10 units,
//     the middle circle a radius of 5 units,
//     and the inner circle a radius of 1.
//     The center of the target is at (0,0).

// 2. Examples:

// score(-9, 9) == 0
// score(7.1, -7.1) == 0
// score(0, 10) == 1
// score(-3.6, -3.6) == 1
// score(-5, 0) == 5
// score(0.8, -0.8) == 5
// score(0.7, 0.7) == 10
// score(-0.1, -0.1) == 10

// 3. What is the algorithm?

// Calculate the distance between the point and the center of the target
// If the distance is less than or equal to the radius of the inner circle, return 10
// If the distance is less than or equal to the radius of the middle circle, return 5
// If the distance is less than or equal to the radius of the outer circle, return 1
// Otherwise, return 0

export function score(x: number, y: number): number {
  const distance = Math.sqrt(x * x + y * y);

  if (distance <= 1) {
    return 10;
  } else if (distance <= 5) {
    return 5;
  } else if (distance <= 10) {
    return 1;
  }

  return 0;
}
