(*

Step 1 - Problem Understanding:

* What are the expected inputs?
 - f: A predicate function (fn x => bool) that takes an element of the list and returns a boolean
 - l: A list of elements of any type (could be numbers, strings, or lists)

* What are the expected outputs?
 - A new list containing elements from the input list, filtered according to the predicate

* What are the key rules or constraints?
 - The functions should not modify the original list.
 - The predicate function should match the type of the elements in the list.
 - The functions should not use the built-in functions.

* What is the mental model?
 - Both functions iterate through the list and apply the predicate.
 One function retains elements where the predicate holds (keep), while the other retains elements where the predicate fails (discard)

*)

(*

Step 2 - Examples:

(* keep *)
keep (fn x => x mod 2 = 0) [1, 2, 3, 4, 5] = [2, 4]
keep (fn s => String.size s > 3) ["a", "ab", "abc", "abcd"] = ["abcd"]

(* discard *)
discard (fn x => x mod 2 = 0) [1, 2, 3, 4, 5] = [1, 3, 5]
discard (fn s => String.size s > 3) ["a", "ab", "abc", "abcd"] = ["a", "ab", "abc"]

*)

(*

Step 3 - Algorithm Design:

- We can use recursion to iterate through the list and build the new lists.
- Prepending ensures that the elements in the final result maintain the same relative order they had in the original list.

keep(f , l):
1. If l is empty, return an empty list.
2. Otherwise, let x be the head of l and xs be the tail.
3. If f(x) is true, return x prepended to the result of keep(f, xs).
4. Otherwise, return the result of keep(f, xs).

discard(f, l):

1. If l is empty, return an empty list.
2. Otherwise, let x be the head of l and xs be the tail.
3. If f(x) is false, return x prepended to the result of discard(f, xs).
4. Otherwise, return the result of discard(f, xs).

*)

(* Step 5 - Implementation:

fun keep f [] = []
  | keep f (x::xs) =
    let
      val rest = keep f xs
    in
      if f x then x :: rest else rest  (* Include x if f(x) is true, otherwise skip it *)
    end

fun discard f [] = []
  | discard f (x::xs) =
    let
      val rest = discard f xs
    in
      if f x then rest else x :: rest  (* Exclude x if f(x) is true, otherwise include it *)
    end

*)

(* Step 6 - Refactoring: *)

fun keep f [] = []
  | keep f (x::xs) =
    let
      val rest = keep f xs
    in
      if f x then x :: rest else rest  (* Include x if f(x) is true, otherwise skip it *)
    end

fun discard f l = keep (fn x => not (f x)) l
