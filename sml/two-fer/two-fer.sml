(*
   name : string option -> string
   Input: An optional name (string option). The input can either be:
          - SOME "name" (where "name" is the provided string), or
          - NONE (if no name is provided).
   Output: A string in the format "One for {name}, one for me."

   Description:
   - If a name is provided (SOME "name"), use that name in the output.
   - If no name is provided (NONE), use "you" in place of the name.
   - The output always follows the format "One for {name}, one for me."

   Examples:
   - name (SOME "Do-yun") => "One for Do-yun, one for me."
   - name NONE => "One for you, one for me."
*)

(* Version 1
fun name (input: string option) =
  "One for " ^ (if isSome input then valOf input else "you") ^ ", one for me."
*)

(* Version 2: Using pattern matching *)
fun name (input: string option) =
  case input of
    SOME n => "One for " ^ n ^ ", one for me."
  | NONE => "One for you, one for me."
