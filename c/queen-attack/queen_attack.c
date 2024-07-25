// Step 1: Understand the problem
// What are the inputs?
// - The positions of a black queen and a white queen, each specified as a pair of row and column coordinates.
// What is the output?
// - The attack status, which can be one of the following: CAN_NOT_ATTACK, CAN_ATTACK, or INVALID_POSITION
// What are the rules?
// - A chessboard can be represented by an 8 by 8 array (zero-indexed at column)
// - A queen can attack pieces which are on the same row, column, or diagonal.

// Step 2: Examples
// 1. If the position of the white queen is column 2 and row 5, and the position of the black queen is the same, the result is INVALID_POSITION because they occupy the same position.
// 2. If the white queen is at column 2, row 8, and the black queen is at column 0, row 0, the result is INVALID_POSITION because the white queen's row is off the board.
// 3. If the white queen is at column 8, row 2, and the black queen is at column 0, row 0, the result is INVALID_POSITION because the white queen's column is off the board.
// 4. If the white queen is at column 0, row 0, and the black queen is at column 2, row 10, the result is INVALID_POSITION because the black queen's row is off the board.
// 5. If the white queen is at column 0, row 0, and the black queen is at column 9, row 4, the result is INVALID_POSITION because the black queen's column is off the board.

// 6. If the white queen is at column 4, row 2, and the black queen is at column 6, row 6, the result is CAN_NOT_ATTACK because they are not on the same row, column, or diagonal.
// 7. If the white queen is at column 1, row 4, and the black queen is at column 5, row 2, the result is CAN_NOT_ATTACK because they are not on the same row, column, or diagonal, even though their positions might seem related when reflected across the longest falling diagonal.

// 8. If the white queen is at column 4, row 2, and the black queen is at column 6, row 2, the result is CAN_ATTACK because they are on the same row.
// 9. If the white queen is at column 5, row 4, and the black queen is at column 5, row 2, the result is CAN_ATTACK because they are on the same column.
// 10. If the white queen is at column 2, row 2, and the black queen is at column 4, row 0, the result is CAN_ATTACK because they are on the same diagonal (first diagonal).
// 11. If the white queen is at column 2, row 2, and the black queen is at column 1, row 3, the result is CAN_ATTACK because they are on the same diagonal (second diagonal).
// 12. If the white queen is at column 2, row 2, and the black queen is at column 1, row 1, the result is CAN_ATTACK because they are on the same diagonal (third diagonal).
// 13. If the white queen is at column 7, row 1, and the black queen is at column 6, row 0, the result is CAN_ATTACK because they are on the same diagonal (fourth diagonal).

// Step 3: Algorithm: Steps for converting the input to output
// 1. Check if either queen's position is invalid:
//  - Ensure both queens' row and column values are between 0 and 7 (inclusive).
//  - If any position is outside this range, return INVALID_POSITION.
//  - If both queens occupy the same position, return INVALID_POSITION.
// 2. Check if the queens can attack each other:
//  - If they are in the same row (queen_1.row == queen_2.row), return CAN_ATTACK.
//  - If they are in the same column (queen_1.column == queen_2.column), return CAN_ATTACK.
//  - If they are on the same diagonal:
//      - Calculate the absolute difference between their rows and columns.
//      - If these differences are equal, they are on a diagonal, so return CAN_ATTACK.
// 3. If none of the above conditions are met, return CAN_NOT_ATTACK.

// Step 4: Code: Implementation

#include "queen_attack.h"
#include <stdlib.h>
#include <stdbool.h>

static bool is_valid_position(position_t pos)
{
   return pos.row < 8 && pos.column < 8;
}

static bool has_valid_positions(position_t pos_1, position_t pos_2)
{
   if (!is_valid_position(pos_1) || !is_valid_position(pos_2))
      return false;
   return !(pos_1.row == pos_2.row && pos_1.column == pos_2.column);
}

static bool is_on_straight_or_diagonal(position_t pos_1, position_t pos_2)
{
   return pos_1.row == pos_2.row || pos_1.column == pos_2.column ||
          abs(pos_2.row - pos_1.row) == abs(pos_2.column - pos_1.column);
}

attack_status_t can_attack(position_t queen_1, position_t queen_2)
{
   return (!has_valid_positions(queen_1, queen_2))       ? INVALID_POSITION
          : is_on_straight_or_diagonal(queen_1, queen_2) ? CAN_ATTACK
                                                         : CAN_NOT_ATTACK;
}
