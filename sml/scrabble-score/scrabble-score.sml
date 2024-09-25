(* Step 1 - Problem Understanding

What is the input?
- A word consisting of alphabetic characters (in uppercase or lowercase).

What is the output?
- A positive integer that represents the score for that word.

What are the rules?
- The total Scrabble score for a word is the sum of the individual letter scores.
- Each letter has a pre-defined score:
    1 point: A, E, I, O, U, L, N, R, S, T
    2 points: D, G
    3 points: B, C, M, P
    4 points: F, H, V, W, Y
    5 points: K
    8 points: J, X
    10 points: Q, Z
- Words can be composed of both uppercase and lowercase letters, but the score remains the same regardless of case.
- Non-alphabetic characters are not considered, and we can assume valid input consists of alphabetic characters only.

What is the mental model?
- We need to map each letter in a word to its respective Scrabble score and sum these scores to get the total.

*)

(* Step 2 - Examples

Input: ""
Output: 0

Input: "A"
Output: 1

Input: "a"
Output: 1

Input: "quirky"
Output: 22

*)

(* Step 3 - Data structure selection

For this problem, we can use two main data structures:

- An association list (a key-value mapping as a list of key-value pairs) to store letter-score pairs.
- A list to represent the input word as a sequence of characters.

*)

(* Step 4 - Algorithm design

1. Create an association list mapping each letter to its score.
2. Convert the input word to a list of uppercase characters.
3. Map each character in the word to its score using the association list.
4. Sum up all the scores.

*)

(* Step 5 - Implementation *)

(* Define the letter-score mapping *)
(* (char * int) list *)
val letterScores = [
  (#"A", 1), (#"E", 1), (#"I", 1), (#"O", 1), (#"U", 1), (#"L", 1), (#"N", 1), (#"R", 1), (#"S", 1), (#"T", 1),
  (#"D", 2), (#"G", 2),
  (#"B", 3), (#"C", 3), (#"M", 3), (#"P", 3),
  (#"F", 4), (#"H", 4), (#"V", 4), (#"W", 4), (#"Y", 4),
  (#"K", 5),
  (#"J", 8), (#"X", 8),
  (#"Q", 10), (#"Z", 10)
]

(* Function to look up a letter's score *)
(* char -> int *)
(* letterScore #"Q"  (* Returns 10 because 'Q' has a score of 10 *) *)
fun letterScore letter =
  case List.find (fn (c, _) => c = letter) letterScores of
    SOME (_, score) => score
  | NONE => 0  (* Handle unknown characters *)

(* Main scoring function *)
(* string -> int *)
fun score word =
  let
    val chars = explode (String.map Char.toUpper word)   (* Convert word to list of uppercase characters *)
    fun sumScores (char, acc) = acc + letterScore char   (* Helper function to sum character scores *)
  in
    List.foldl sumScores 0 chars   (* Use foldl to sum up scores from the list of characters *)
  end
