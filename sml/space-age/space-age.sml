(*

Step 1 - Problem Understanding:

* What are the expected inputs?
    * Data type: planet (Custom datatype)
    * Description: The planet for which the person's age is being calculated.

    * Data type: Integer
    * Description: The person’s age in seconds, which will be converted into years on the specified planet.

* What is the expected output?
    * Data type: real (Floating-point number)
    * Description: The calculated age of the person on the specified planet, expressed in that planet's years.

* What are the explicit requirements and rules?
- Calculate age based on the orbital periods provided for each planet.
- Earth's orbital period is defined as 365.25 days or 31557600 seconds.
- Output should be rounded to two decimal places.
- No input validation is required (we can assume valid inputs).

* What is the mental model?
- Convert a person’s age in seconds into planetary years by dividing their age in Earth years by the orbital period of the specified planet.

*)

(*

Step 2 - Examples:

Input: Planet = Earth, Seconds = 1,000,000,000
Expected Output: 31.69 Earth years (because 1,000,000,000 / 31,557,600 = 31.69)

Input: Planet = Mercury, Seconds = 2,134,835,688
Expected Output: 280.88 Mercury years (because 2,134,835,688 seconds equals 67.65 Earth years, and dividing by Mercury's orbital period of 0.2408467 gives 280.88)

Input: Planet = Neptune, Seconds = 8,210,123,456
Expected Output: 1.58 Neptune years

*)

(*

Step 3 - Algorithm Design:

1. Convert Seconds to Earth Years: The number of Earth years can be calculated by dividing the number of seconds by the number of seconds in an Earth year (31,557,600 seconds).
2. Adjust for Planetary Orbital Period: For each planet, divide the Earth years by the planet’s orbital period (a constant given for each planet).
3. Return the Result: Return the age on the given planet, which is the age in Earth years divided by the planet's orbital period.

*)

(* Step 4 - Implementation: *)

datatype planet = Mercury | Venus | Earth | Mars
                | Jupiter | Saturn | Uranus | Neptune

fun seconds_to_earth_years seconds =
    Real.fromInt seconds / 31557600.0

fun planet_to_orbital_period planet =
    case planet of
        Mercury => 0.2408467
      | Venus => 0.61519726
      | Earth => 1.0
      | Mars => 1.8808158
      | Jupiter => 11.862615
      | Saturn => 29.447498
      | Uranus => 84.016846
      | Neptune => 164.79132

fun age_on planet seconds =
    let
        val earth_years = seconds_to_earth_years seconds
        val orbital_period = planet_to_orbital_period planet
        val age = earth_years / orbital_period
    in
        age
    end
