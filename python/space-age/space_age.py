# Step 1: Understand the problem

# What are the inputs?
# An integer representing the age of a person in seconds.

# What are the outputs?
# A float representing the age of a person on the specified planet in years, rounded to 2 decimal places.

# What is the mental model?
# Convert the input seconds to years on the specified planet by using the planet's orbital period relative to Earth.

# What are the rules?
# - Each planet has a specific orbital period relative to Earth years.
# - Earth's orbital period is 1 year, which is equal to 31, 557, 600 seconds.
# - The age on a planet is calculated by dividing the input seconds by the planet's orbital period in seconds.

# 2. Examples/Test cases

# Input: SpaceAge(1000000000).on_earth()
# seconds = 1000000000
# orbitalRatio = 1
# orbitalPeriodSeconds = orbitalRatio * 31557600
# ageOnPlanet = seconds / 31557600
# round(ageOnPlanet, 2) = 31.69
# Output: 31.69

# Input: SpaceAge(2134835688).on_mercury()
# seconds = 2134835688
# orbitalRatio = 0.2408467
# orbitalPeriodSeconds = orbitalRatio * 31557600
# ageOnPlanet = seconds / orbitalPeriodSeconds
# round(ageOnPlanet, 2) = 280.88
# Output: 280.88

# Input: SpaceAge(1821023456).on_neptune()
# seconds = 1821023456
# orbitalRatio = 164.79132
# orbitalPeriodSeconds = orbitalRatio * 31557600
# ageOnPlanet = seconds / orbitalPeriodSeconds
# round(ageOnPlanet, 2) = 0.35
# Output: 0.35

# Step 3: Algorithm - steps for converting the input to the output

# 1. Create a SpaceAge object with the given age in seconds.
# 2. Define a method for each planet(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune).
# 3. In each planet-specific method:
#    a. Retrieve the orbital period ratio for the planet from a predefined dictionary.
#    b. Calculate the planet's orbital period in seconds by multiplying its ratio with Earth's year in seconds.
#    c. Divide the input age in seconds by the planet's orbital period in seconds.
#    d. Round the result to two decimal places.
#    e. Return this value as the age on that planet.
# 4. When a specific planet's method is called, it will return the calculated age for that planet.

# Step 4: Implementation

""" class SpaceAge:
    # Constants defined for Earth's seconds in a year and orbital periods of different planets in Earth years
    SECONDS_IN_EARTH_YEAR = 31557600

    PLANET_ORBITAL_PERIODS_IN_EARTH_YEARS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        # Initializes the SpaceAge object with the given seconds
        self.seconds = seconds

    def age_on_planet(self, planet):
        # Helper method to calculate age on a given planet

        # Convert the orbital period from Earth years to seconds
        orbital_period_in_seconds = self.PLANET_ORBITAL_PERIODS_IN_EARTH_YEARS[planet] * self.SECONDS_IN_EARTH_YEAR

        # Calculate the age on the given planet by dividing total seconds by the orbital period in seconds
        age_on_planet = self.seconds / orbital_period_in_seconds

        # Round the result to two decimal places and return it
        return round(age_on_planet, 2)

    # Methods to calculate age on each planet.
    # They simply call the helper method with the appropriate planet name

    def on_mercury(self):
        return self.age_on_planet('mercury')

    def on_venus(self):
        return self.age_on_planet('venus')

    def on_earth(self):
        return self.age_on_planet('earth')

    def on_mars(self):
        return self.age_on_planet('mars')

    def on_jupiter(self):
        return self.age_on_planet('jupiter')

    def on_saturn(self):
        return self.age_on_planet('saturn')

    def on_uranus(self):
        return self.age_on_planet('uranus')

    def on_neptune(self):
        return self.age_on_planet('neptune') """

# 4. Refactor

from typing import Dict, Callable


class SpaceAge:
    SECONDS_IN_EARTH_YEAR: int = 31_557_600
    ORBITAL_PERIODS: Dict[str, float] = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds: int):
        self.seconds: int = seconds

# Dynamic Method Generation: Used getattr to dynamically generate methods for each planet, reducing code duplication
    def __getattr__(self, name: str) -> Callable[[], float]:
        planet = name[3:]  # Remove 'on_' prefix
        if planet in self.ORBITAL_PERIODS:
            return lambda: self._age_on_planet(planet)
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def _age_on_planet(self, planet: str) -> float:
        orbital_period_seconds = self.ORBITAL_PERIODS[planet] * \
            self.SECONDS_IN_EARTH_YEAR
        return round(self.seconds / orbital_period_seconds, 2)
