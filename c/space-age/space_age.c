// Step 1: Understand the problem

// What are the inputs?
// An integer representing the age of a person in seconds, and a string representing the planet name.

// What are the outputs?
// A float representing the age of a person on the specified planet in years.

// What are the rules?
// - Each planet has a specific orbital period relative to Earth years.
// - Earth's orbital period is 1 year, which is equal to 31,557,600 seconds.
// - The age on a planet is calculated by dividing the input seconds by the planet's orbital period in seconds.

// What is the mental model?
// Convert the input seconds to years on the specified planet by using the planet's orbital period relative to Earth.

// Step 2: Examples and test cases

// Input: 1000000000, "earth"
// Output: 31.69

// Input: 2134835688, "mercury"
// Output: 280.88

// Input: 189839836, "venus"
// Output: 9.78

// Input: 1821023456, "neptune"
// Output: 0.35

// Step 3: Algorithm - steps for converting the input to the output

// 1. Define a constant for the number of seconds in an Earth year (31,557,600).
// 2. Create an array of orbital period ratios for each planet relative to Earth, indexed to match the planet_t enum.
// 3. Define a function 'age' that takes a planet enum and age in seconds as parameters:
//    a. Check if the input planet is valid(within the enum range).
//    b. If invalid, return -1.0 to indicate an error.
//    c. If valid, proceed with the calculation.
// 4. Calculate the orbital period of the specified planet in seconds:
//    a. Look up the planet's orbital ratio from the array.
//    b. Multiply this ratio by the number of seconds in an Earth year.
// 5. Calculate the age on the specified planet:
//    a. Divide the input seconds by the planet's orbital period in seconds.
// 6. Return the calculated age as a float.

// Step 4: Implementation
#include "space_age.h"

/* #define SECONDS_IN_EARTH_YEAR 31557600.0

static const float ORBITAL_PERIOD_RATIOS[] = {
    [MERCURY] = 0.2408467,
    [VENUS] = 0.61519726,
    [EARTH] = 1.0,
    [MARS] = 1.8808158,
    [JUPITER] = 11.862615,
    [SATURN] = 29.447498,
    [URANUS] = 84.016846,
    [NEPTUNE] = 164.79132,
};
float age(planet_t planet, int64_t seconds)
{
  if (planet < MERCURY || planet > NEPTUNE)
  {
    return -1.0; // Invalid planet
  }

  float orbital_period_seconds = ORBITAL_PERIOD_RATIOS[planet] * SECONDS_IN_EARTH_YEAR;
  return seconds / orbital_period_seconds;
} */

// Step 5: Refactor
static const int EARTH_YEAR_SECONDS = 31557600;
static const double RATIOS[] = {
    0.2408467, 0.61519726, 1.0, 1.8808158,     // inner planets
    11.862615, 29.447498, 84.016846, 164.79132 // outer planets
};

float age(planet_t planet, int64_t seconds)
{
  return planet >= 0 && planet <= 7 ? seconds / EARTH_YEAR_SECONDS / RATIOS[planet] : -1;
}
