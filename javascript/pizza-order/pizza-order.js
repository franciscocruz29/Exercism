/// <reference path="./global.d.ts" />
//
// @ts-check

const PIZZA_PRICES = { Margherita: 7, Caprese: 9, Formaggio: 10 };
const EXTRA_PRICES = { ExtraSauce: 1, ExtraToppings: 2 };
/**
 * Determine the prize of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
  // Base case: no extras provided
  if (extras.length === 0) {
    return PIZZA_PRICES[pizza];
  }

  // Recursive case: calculate the price of the pizza with extras
  const extra = extras[0];
  const remainingExtras = extras.slice(1);
  const extraPrice = EXTRA_PRICES[extra] || 0;
  return extraPrice + pizzaPrice(pizza, ...remainingExtras);
}

/**
 * Calculate the prize of the total order, given individual orders
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  let totalPrice = 0;

  for (const order of pizzaOrders) {
    const { pizza, extras } = order;
    const currentPrice = pizzaPrice(pizza, ...extras);
    totalPrice += currentPrice;
  }

  return totalPrice;
}
