(* Step 1 - Problem Understanding:
    
  - What are the expected inputs?
    - Data type: An integer
    - Description: A positive integer n
  
  - What are the expected outputs?
    - Data type: An integer
    - Description: The number of steps required to reduce n to 1.
  
  - What are the key rules or constraints?
    - If n is even: n → n/2
    - If n is odd: n → 3n + 1
    - Process repeats until n = 1

  - What is the mental model?
    - Given a number n, we keep applying transformations (based on whether n is odd or even) until n becomes 1. The goal is to count how many transformations (steps) are needed.

*)

(* Step 2 - Examples:

Input: 1
Output: 0

Input: 16
Output: 4

Input: 0
Output: None

*)

(* Step 3 - Algorithm Design:

Step 1 - Base Case: If the current number n is 1, the function returns SOME steps, where steps is the accumulated number of steps. 
Step 2 - Recursive Case: 
          - If the current number n is even, the function calls itself with n / 2 as input and increments steps by 1.
          - If the current number n is odd, the function calls itself with 3n + 1 as input and increments steps by 1.
Step 3 - Error Handling: If the input n is less than or equal to 0, the function returns NONE to indicate an invalid input.

*)

(* Step 4 - Implementation: *)

fun collatz n =
  let
    fun collatz_helper(1, steps) = SOME steps
      | collatz_helper(n, steps) =
          if n mod 2 = 0 then
            collatz_helper(n div 2, steps + 1)
          else
            collatz_helper(3 * n + 1, steps + 1)
  in
    if n <= 0 then NONE
    else collatz_helper(n, 0)
  end
