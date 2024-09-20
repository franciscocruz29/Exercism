(*
   isLeapYear : int -> bool
   Input: A positive integer representing the year to check.
   Output: A boolean value, true if the year is a leap year, false otherwise.

   Description:
   - A leap year occurs under the following conditions in the Gregorian calendar:
     1. The year must be divisible by 4.
     2. If the year is divisible by 100, it must also be divisible by 400.

   Examples:
   - isLeapYear 2020 => true
   - isLeapYear 1900 => false
   - isLeapYear 2000 => true
*)

(* Traditional approach
fun isLeapYear year =
  let
    val divBy4 = year mod 4 = 0
    val divBy100 = year mod 100 = 0
    val divBy400 = year mod 400 = 0
  in
    divBy4 andalso (not divBy100 orelse divBy400)
  end
*)

(* Pattern matching *)
fun isLeapYear year =
  case (year mod 4, year mod 100, year mod 400) of
      (0, 0, 0) => true   (* Divisible by 4, 100, and 400 => leap year *)
    | (0, 0, _) => false  (* Divisible by 4 and 100 but not 400 => not a leap year *)
    | (0, _, _) => true   (* Divisible by 4 but not 100 => leap year *)
    | _ => false          (* Not divisible by 4 => not a leap year *)
