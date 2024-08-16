// Step 1: Understand the problem

// What are the inputs?
// A string representing the planet name, and a number representing the age of a person in seconds.

// What are the outputs?
// A number representing the age of a person on the specified planet in years, rounded to 2 decimal places.

// What are the rules?
// - Each planet has a specific orbital period ratio relative to Earth years.
// - Earth's orbital period is 1 year, which is equal to 31,557,600 seconds.
// - The age on a planet is calculated by dividing the input seconds by the planet's orbital period in seconds.

// What is the mental model?
// Convert the input seconds to years on the specified planet by using the planet's orbital period ratio relative to Earth.

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

// 1. Define an interface 'Planets' to type the orbital ratios object.
// 2. Define a constant object 'RATIOS' with orbital ratios for each planet relative to Earth.
// 3. Create a function 'age' that takes the planet name (string) and age in seconds (number) as parameters.
// 4. Calculate the orbital period of the specified planet in seconds by multiplying its ratio by 31,557,600.
// 5. Divide the input seconds by the planet's orbital period to get the age on that planet.
// 6. Round the result to 2 decimal places using toFixed(2).
// 7. Return the calculated age as a number using Number() conversion.

// Step 4: Implementation
interface Planets {
  [key: string]: number;
}

const RATIOS: Planets = {
  mercury: 0.2408467,
  venus: 0.61519726,
  earth: 1,
  mars: 1.8808158,
  jupiter: 11.862615,
  saturn: 29.447498,
  uranus: 84.016846,
  neptune: 164.79132,
};

export function age(planet: string, seconds: number): number {
  const orbitalPeriodSeconds: number = RATIOS[planet] * 31557600;
  const ageOnPlanet: number = seconds / orbitalPeriodSeconds;
  return Number(ageOnPlanet.toFixed(2));
}
