// Step 1 - Problem Understanding:
//
// What are the inputs?
// - An array of integers representing game scores.
// - The size or length of the array
//
// What are the outputs?
// - The latest (most recently added) score.
// - The highest score ever achieved (personal best).
// - The top three highest scores in descending order.
//
// What are the rules?
// - The functions should be able to handle arrays of varying lengths.
// - If there are fewer than three scores, the personal_top_three function should return only the available scores in descending order.
// - Ties in scores should be handled appropriately in the top three list.
//
// What is the mental model?
// - We are given a collection of game scores. We need to find the most recent score, the all-time best score, and the three best scores from this collection, keeping them sorted in descending order.

// Step 2 - Examples:
//
// Example 1: Basic Scenario
// Scores: [100, 85, 92, 78]
// Latest: 78
// Personal Best: 100
// Top Three: [100, 92, 85]
//
// Example 2: Tie
// Scores: [80, 100, 80, 90]
// Latest: 90
// Personal Best: 100
// Top Three: [100, 90, 80]
//
// Example 3: Edge Case - Fewer than 3 scores
// Scores: [50, 60]
// Latest: 60
// Personal Best: 60
// Top Three: [60, 50]

// Step 3 - Algorithm Design:
//
// Helper Functions:
//
// 1. swap(a, b):
//  - Swap the values of two integers using a temporary variable.
//
// 2. sort_descending(arr, size):
//  - Implement bubble sort to sort the array in descending order.
//  - Iterate through the array multiple times, swapping adjacent elements if they're in the wrong order.
//
// Main Functions:
//
// 1. latest(scores, scores_len):
//  - If the array is empty, return 0.
//  - Otherwise, return the last element of the array
//
// 2. personal_best(scores, scores_len):
//  - If the array is empty, return 0.
//  - Initialize max_score with the first score
//  - Iterate through the array
//  - If current score > max_score, update max_score
//  - Return max_score
//
// 3. personal_top_three(scores, scores_len, output):
// - If scores_len <= 3:
//      a. Copy all scores to the output array.
//      b. Sort the output array in descending order using sort_descending().
//      c. Return scores_len.
// - If scores_len > 3:
//      a. Initialize top_three array with INT32_MIN values.
//      b. Iterate through the scores array once:
//          - If current score > top_three[0], shift values and insert at top_three[0].
//          - Else if current score > top_three[1], shift and insert at top_three[1].
//          - Else if current score > top_three[2], insert at top_three[2].
//      c. Copy top_three to the output array.
//      d. Return 3 (MAX_TOP_SCORES).

// Step 4 - Implementation:

#include "high_scores.h"
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#define MAX_TOP_SCORES 3

// Helper function to swap two integers
static void swap(int32_t *a, int32_t *b) {
    int32_t temp = *a;
    *a = *b;
    *b = temp;
}

// Helper function to sort array in descending order
static void sort_descending(int32_t *arr, size_t size) {
    for (size_t i = 0; i < size - 1; i++) {
        for (size_t j = 0; j < size - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

// Helper function to insert a score into the top three if it's high enough
static void update_top_three(int32_t *top_three, int32_t score) {
    if (score > top_three[0]) {
        top_three[2] = top_three[1];
        top_three[1] = top_three[0];
        top_three[0] = score;
    } else if (score > top_three[1]) {
        top_three[2] = top_three[1];
        top_three[1] = score;
    } else if (score > top_three[2]) {
        top_three[2] = score;
    }
}

// Return the latest score.
int32_t latest(const int32_t *scores, size_t scores_len) {
    return (scores_len > 0) ? scores[scores_len - 1] : 0;
}

// Return the highest score.
int32_t personal_best(const int32_t *scores, size_t scores_len) {
    if (scores_len == 0) {
        return 0;
    }

    int32_t max_score = scores[0];
    for (size_t i = 1; i < scores_len; i++) {
        if (scores[i] > max_score) {
            max_score = scores[i];
        }
    }
    return max_score;
}

// Write the highest scores to `output` (in non-ascending order).
// Return the number of scores written.
size_t personal_top_three(const int32_t *scores, size_t scores_len, int32_t *output) {
    if (scores_len == 0) {
        return 0;
    }

    // If we have 3 or fewer scores, copy and sort them
    if (scores_len <= MAX_TOP_SCORES) {
        memcpy(output, scores, scores_len * sizeof(int32_t));
        sort_descending(output, scores_len);
        return scores_len;
    }

    // For more than 3 scores, find the top 3 in one pass
    int32_t top_three[MAX_TOP_SCORES] = {INT32_MIN, INT32_MIN, INT32_MIN};

    for (size_t i = 0; i < scores_len; i++) {
        update_top_three(top_three, scores[i]);
    }

    // Copy the top 3 scores to the output array
    memcpy(output, top_three, MAX_TOP_SCORES * sizeof(int32_t));
    return MAX_TOP_SCORES;
}
