// Step 1: Understand the problem

// What are the inputs? 
// An integer representing the age of a person in seconds, and a string representing the planet name.

// What are the outputs?
// A float representing the age of a person on the specified planet in years, rounded to 2 decimal places.

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

// 1. Define a constant object with orbital ratios for each planet relative to Earth.
// 2. Define a constant for the number of seconds in an Earth year.
// 3. Create a function that takes the planet name and age in seconds as parameters.
// 4. Calculate the orbital period of the specified planet in seconds.
// 5. Divide the input seconds by the planet's orbital period to get the age on that planet.
// 6. Round the result to 2 decimal places.
// 7. Return the calculated age as a number.


// Step 4: Implementation

// Constants
const EARTH_YEARS_IN_SECONDS = 31_557_600;

const ORBITAL_PERIODS = {
  mercury: 0.2408467,
  venus: 0.61519726,
  earth: 1,
  mars: 1.8808158,
  jupiter: 11.862615,
  saturn: 29.447498,
  uranus: 84.016846,
  neptune: 164.79132
};

// Helper function to calculate age on a planet
const calculateAgeOnPlanet = (seconds, orbitalPeriod) => {
  return seconds / (orbitalPeriod * EARTH_YEARS_IN_SECONDS);
};

// Main function
export const age = (planet, seconds) => {

  const orbitalPeriod = ORBITAL_PERIODS[planet.toLowerCase()];
  const ageOnPlanet = calculateAgeOnPlanet(seconds, orbitalPeriod);

  return Number(ageOnPlanet.toFixed(2));
};
