// Step 1 - Problem Understanding:

// What are the inputs?
// There are no explicit inputs from the user during the random character generation,
// but you will simulate the rolls of four 6-sided dice for each of the six abilities: strength, dexterity, constitution, intelligence, wisdom, and charisma.

// What are the outputs?
// A structure representing a character with the six ability scores and the character's hitpoints.

// What are the rules?
// - For each ability score, roll four 6-sided dice, discard the lowest die, and sum the highest three dice.
// - The character’s hitpoints are calculated as: hitpoints = 10 + constitution modifier.
// - The constitution modifier is calculated as: (constitution - 10) / 2 (rounded down).

// What is the mental model?
// The problem is about creating a function that generates a character's six ability scores based on rolling dice,
// calculates the constitution modifier from the constitution score, and then uses it to determine the character's hitpoints.
// The scores are generated randomly by simulating dice rolls.


// Step 2 - Examples and Test Cases

// Example 1 (Normal case):
// Rolls: [5,3,1,6], [3,2,5,3], [4,4,4,4], [2,1,6,6], [3,5,3,4], [6,6,6,6]
// Resulting character:
//      Strength: 14 (5+3+6)
//      Dexterity: 11 (3+5+3)
//      Constitution: 12 (4+4+4)
//      Intelligence: 14 (2+6+6)
//      Wisdom: 12 (5+3+4)
//      Charisma: 18 (6+6+6)
//      Hitpoints: 11 (10 + modifier(12) = 10 + 1)

// Example 2 (Low rolls):
// Rolls: [2,2,1,3], [1,1,2,3], [1,1,1,2], [2,2,2,3], [1,2,2,3], [1,1,1,3]
// Resulting character:
//      Strength: 7 (2+2+3)
//      Dexterity: 6 (1+2+3)
//      Constitution: 4 (1+1+2)
//      Intelligence: 7 (2+2+3)
//      Wisdom: 7 (2+2+3)
//      Charisma: 5 (1+1+3)
//      Hitpoints: 7 (10 + modifier(4) = 10 - 3)

// Edge case (All minimum or maximum rolls):
// Rolls: [1,1,1,1], [1,1,1,1], [1,1,1,1], [6,6,6,6], [6,6,6,6], [6,6,6,6]
// Resulting character:
//      Strength: 3 (1+1+1)
//      Dexterity: 3 (1+1+1)
//      Constitution: 3 (1+1+1)
//      Intelligence: 18 (6+6+6)
//      Wisdom: 18 (6+6+6)
//      Charisma: 18 (6+6+6)
//      Hitpoints: 7 (10 + modifier(3) = 10 - 3)


// Step 3 - Data Structure Selection

// Array:
// - An array is suitable to hold the dice rolls (4 elements for each roll), as we need to access and sort them to find the highest three.

// Struct (for the character):
// - A structure is ideal for holding the final character attributes such as strength, dexterity, constitution, etc., along with hitpoints.
// This groups all related information in one place.


// Step 4 - Algorithm Design

// 1. Create a function to roll a single 6-sided die
// 2. Create a function to generate an ability score:
//      a. Roll four 6-sided dice
//      b. Sort the rolls in ascending order
//      c. Sum the highest three rolls
// 3. Create a function to calculate the ability modifier
// 4. Create the main character generation function:
//      a. Generate six ability scores using the ability score function
//      b. Assign each score to the corresponding ability in the character struct
//      c. Calculate hitpoints using the constitution score and modifier function
//      d. Return the completed character struct


// Step 5 - Implementation

#include "dnd_character.h"
#include <math.h>
#include <stdlib.h>
#include <time.h>

int roll_die(void) {
    return rand() % 6 + 1;
}

// Function to calculate an ability score by rolling 4 dice and summing the top 3
int ability(void) {
    int dice[4];
    int min_value = 7;  // A value higher than the maximum roll of 6
    int sum = 0;

    // Roll 4 dice and find the smallest value while summing all dice
    for (int i = 0; i < 4; i++) {
        dice[i] = roll_die();
        sum += dice[i];
        if (dice[i] < min_value) {
            min_value = dice[i];  // Track the smallest die value
        }
    }

    // Subtract the smallest value from the sum to get the top 3 dice sum
    return sum - min_value;
}

int modifier(int score) {
    return floor((score - 10) / 2.0);
}

dnd_character_t make_dnd_character(void) {
    dnd_character_t character;

    character.strength = ability();
    character.dexterity = ability();
    character.constitution = ability();
    character.intelligence = ability();
    character.wisdom = ability();
    character.charisma = ability();

    character.hitpoints = 10 + modifier(character.constitution);

    return character;
}
