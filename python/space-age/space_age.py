# 1. Understand the problem

# What are the inputs? An integer representing the age of a person in seconds.
# What are the outputs? A float representing the age of a person in a planet in years.

# What are the rules?

# Given an age in seconds, calculate how old someone would be on:

    # Mercury: orbital period 0.2408467 Earth years
    # Venus: orbital period 0.61519726 Earth years
    # Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
    # Mars: orbital period 1.8808158 Earth years
    # Jupiter: orbital period 11.862615 Earth years
    # Saturn: orbital period 29.447498 Earth years
    # Uranus: orbital period 84.016846 Earth years
    # Neptune: orbital period 164.79132 Earth years

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

# 3. Implementation

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

class SpaceAge:
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
        self.seconds = seconds

    def __getattr__(self, name):
        if name.startswith('on_'):
            planet = name[3:]  # Extract planet name from method
            if planet in self.PLANET_ORBITAL_PERIODS_IN_EARTH_YEARS:
                return lambda: self.calculate_age(planet)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def calculate_age(self, planet):
        orbital_period_in_seconds = self.PLANET_ORBITAL_PERIODS_IN_EARTH_YEARS[planet] * self.SECONDS_IN_EARTH_YEAR
        age_on_planet = self.seconds / orbital_period_in_seconds
        return round(age_on_planet, 2)
