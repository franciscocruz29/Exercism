const orbitalRatio = {
    mercury: 0.2408467,
    venus: 0.61519726,
    earth: 1,
    mars: 1.8808158,
    jupiter: 11.862615,
    saturn: 29.447498,
    uranus: 84.016846,
    neptune: 164.79132
};

const earthSeconds = 31_557_600;

export const age = (planet, seconds) => {
  const orbitalPeriodSeconds = orbitalRatio[planet] * earthSeconds
  const ageOnPlanet = seconds / orbitalPeriodSeconds;
  return Number(ageOnPlanet.toFixed(2));
};
