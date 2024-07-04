/**
 * @brief Checks if a given year is a leap year or not
 *
 * @param year a positive integer representing the year to check
 *
 * @return true if the year is a leap year, false otherwise
 *
 * @details A leap year (in the Gregorian calendar) occurs:
 *          - The year must be divisible by 4.
 *          - If the year is divisible by 100, it must also be divisible by 400.
 *
 * @example leap_year(2015) -> False
 * @example leap_year(1996) -> True
 * @example leap_year(1800) -> False
 * @example leap_year(2400) -> True
 */
#include "leap.h"
bool leap_year(int year)
{
  return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}
