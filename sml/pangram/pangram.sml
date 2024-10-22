(* Step 1 - Problem Understanding:
  
  - What are the expected inputs?
    - Data type: string
    - Description: A sentence which could contain upper and lower case letters, numbers, spaces, punctuation, etc.
  
  - What are the expected outputs?
    - Data type: boolean
    - Description: true if the sentence is a pangram, false otherwise.
  
  - What are the key rules or constraints?
    - The input string must contain every letter of the English alphabet (a-z), regardless of case.
    - The sentence may contain other characters (numbers, spaces, punctuation), but they do not matter for checking if the sentence is a pangram.
    - It is case-insensitive.

  - What is the mental model?
    - We need to check if a given string contains at least one occurrence of each of the 26 letters (ignoring case). If it does, it's a pangram; otherwise, it’s not.
*)

(* Step 2 - Examples:

Input: "abcdefghijklmnopqrstuvwxyz"
Output: true

Input: "a quick movement of the enemy will jeopardize five gunboats"
Output: false

Input: "the_quick_brown_fox_jumps_over_the_lazy_dog"
Output: true

Input: "7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"
Output: false

Input: "\"Five quacking Zephyrs jolt my wax bed.\""
Output: true

Input: ""
Output: false

*)

(* Step 3 - Design and Implementation *)

(* isPangram: string -> boolean *)
fun isPangram sentence =
    let 
        (* Convert the input sentence to lowercase for case-insensitive comparison *)
        val lowercaseSentence = String.map Char.toLower sentence

        (* Define the alphabet as a list of characters for reference *)
        val alphabet = explode "abcdefghijklmnopqrstuvwxyz"

        (* Function to check if every letter of the alphabet exists in the sentence *)
        val hasAllLetters = List.all 
            (fn letter => String.isSubstring (String.str letter) lowercaseSentence) 
            alphabet
    in
        (* Return true if the sentence contains all letters of the alphabet, false otherwise *)
        hasAllLetters
    end
