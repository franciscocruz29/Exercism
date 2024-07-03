/*
Step 1: Understand the problem

What are the inputs?
A postive integer that represents the year

What are the outputs?
A boolean; True if the year is leap, false if the year is not leap

What are the rules?
A leap year (in the Gregorian calendar) occurs:
 - The year must be divisible by 4.
 - If the year is divisible by 100, it must also be divisible by 400.

Step 2: Examples

leap_year(2015) -> False
leap_year(1996) -> True
leap_year(1800) -> False
leap_year(2400) -> True

Step 3:The algorithm

1. Take the input year.
2. Check if the year is divisible by 4:
 - If not divisible by 4, it's not a leap year. Return False.
 - If divisible by 4, continue to step 3.
3. Check if the year is divisible by 100:
 - If not divisible by 100, it is a leap year. Return True.
 - If divisible by 100, continue to step 4.
4. Check if the year is divisible by 400:
 - If divisible by 400, it is a leap year. Return True.
 - If not divisible by 400, it is not a leap year. Return False.

Step 4: The implementation
*/
#include "leap.h"
bool leap_year(int year)
{
  return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}
