// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */

const menuMixTime = { 'Pure Strawberry Joy': 0.5, 'Energizer': 1.5, 'Green Garden': 1.5, 'Tropical Island': 3, 'All or Nothing': 5 }

export function timeToMixJuice(name) {
  return menuMixTime[name] || 2.5
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
const limeWedgesSize = { 'small': 6, 'medium': 8, 'large': 10 }

export function limesToCut(wedgesNeeded, limes) {
  let limesNeeded = 0
  let totalWedges = 0
  let index = 0
  while (totalWedges < wedgesNeeded && index < limes.length) {
    totalWedges += limeWedgesSize[limes[index]]
    limesNeeded += 1
    index += 1
  }
  return limesNeeded
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  while (timeLeft > 0 && orders.length > 0) {
    timeLeft -= timeToMixJuice(orders.shift())
  }
  return orders
}
