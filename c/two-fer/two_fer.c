// Step 1: Understand the problem

// What are the inputs?
// - A name (string) or nothing

// What are the outputs?
// - A string in the format "One for {name}, one for me."

// What are the rules?
// - If a name is provided, use that name in the output
// - If no name is provided, use "you" instead
// - The output should always follow the format "One for X, one for me.";

// What is the mental model?
// - The problem is to construct a sentence based on a given name, following a specific template.

// Step 2: Examples and Test Cases

// Example 1 (Typical Case):
// Input: "Alice";
// Output: "One for Alice, one for me."

// Example 2 (Default Case):
// Input: No name provided.
// Output: "One for you, one for me.";

// Step 3: Algorithm Design

// 1. Check input:
// - Determine if a name is provided or not
// - If name is NULL or and empty string, use the default name "you"

// 2. Format Output:
// - Construct the output string using the provided name or the default "you" according to the template "One for {name}, one for me."

// 3. Buffer management:
// - Ensure the buffer is large enough to hold the result, including any name.
// - Copy the formatted outputstring into the provided buffer.

#include "two_fer.h"
#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE (100)
void two_fer(char *buffer, const char *name)
{
  const char *name_to_use = name ? name : "you";
  snprintf(buffer, BUFFER_SIZE, "One for %s, one for me.", name_to_use);
}
