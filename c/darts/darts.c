// Step 1: Understand the problem

// What are the inputs?
// A point in the target -- defined by its Cartesian coordinates x and y (real numbers)

// What are the outputs?
// The correct amount earned by a dart landing at that point (an integer)

// What are the rules?
// The target rewards 4 different amounts of points, depending on where the dart lands:
// 1. If the dart lands outside the target, player earns no points(0 points).
// 2. If the dart lands in the outer circle of the target, player earns 1 point.
// 3. If the dart lands in the middle circle of the target, player earns 5 points.
// 4. If the dart lands in the inner circle of the target, player earns 10 points.
//
// The outer circle has a radius of 10 units,
// the middle circle a radius of 5 units,
// and the inner circle a radius of 1.
// The center of the target is at (0,0).

// Step 2: Examples

// score(-9, 9) == 0
// score(7.1, -7.1) == 0
// score(0, 10) == 1
// score(-3.6, -3.6) == 1
// score(-5, 0) == 5
// score(0.8, -0.8) == 5
// score(0.7, 0.7) == 10
// score(-0.1, -0.1) == 10

// Step 3: Algorithm: Steps for converting the input to output

// Calculate the distance between the point and the center of the target
// If the distance is less than or equal to the radius of the inner circle, return 10
// If the distance is less than or equal to the radius of the middle circle, return 5
// If the distance is less than or equal to the radius of the outer circle, return 1
// Otherwise, return 0

// Step 4: Implementation

#include <math.h>
#include <stdint.h>
#include "darts.h"

#define INNER_CIRCLE_RADIUS 1.0F
#define MIDDLE_CIRCLE_RADIUS 5.0F
#define OUTER_CIRCLE_RADIUS 10.0F

uint8_t score(coordinate_t landing_position) {
    float distance = sqrtf(landing_position.x * landing_position.x +
                           landing_position.y * landing_position.y);

    if (distance <= INNER_CIRCLE_RADIUS) return 10;
    if (distance <= MIDDLE_CIRCLE_RADIUS) return 5;
    if (distance <= OUTER_CIRCLE_RADIUS) return 1;
    return 0;
}
