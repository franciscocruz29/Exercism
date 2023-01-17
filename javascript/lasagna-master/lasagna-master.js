/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(remainingTimeInMinutes) {
  switch (remainingTimeInMinutes) {
    case undefined:
      return 'You forgot to set the timer.';
    case 0:
      return 'Lasagna is done.';
    default:
      return 'Not done, please wait.';
  }
}

export function preparationTime(layers, avgPrepTimePerLayer) {
  avgPrepTimePerLayer ??= 2;
  return layers.length * avgPrepTimePerLayer;
}

export function quantities(layers) {
  return {
    noodles: layers.filter(layer => layer === 'noodles').length * 50,
    sauce: layers.filter(layer => layer === 'sauce').length * 0.2
  }
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList.at(-1))
}

export function scaleRecipe(amounts, numberOfPortions) {
  let recipe = {};
  for (const [ingredient, quantity] of Object.entries(amounts)) {
    recipe[ingredient] = quantity * numberOfPortions / 2;
  }
  return recipe;
}
