# ---------------------
# 1185. Day of the Week
# ---------------------

# Problem: https://leetcode.com/problems/day-of-the-week
#
# Given a date, return the corresponding day of the week for that date.
# 
# The input is given as three integers representing the day, month and year
# respectively.
# 
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday",
# "Wednesday", "Thursday", "Friday", "Saturday"}.
# 
# Note: January 1, 1971 was a Friday.
# 
# Example 1:
# 
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# 
# Example 2:
# 
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# 
# Example 3:
# 
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
# 
# 
# Constraints:
#         The given dates are valid dates between the years 1971 and 2100.

import datetime

# Solution: https://algo.monster/liteproblems/1185
# Credit: AlgoMonster
def day_of_the_week_alt(day, month, year):
    # Create a date object from the given year, month, and day
    date_obj = datetime.date(year, month, day)
    
    # Format the date object to return the full weekday name
    # %A returns the full weekday name (Monday, Tuesday, etc.)
    weekday_name = date_obj.strftime('%A')
    
    return weekday_name
    # Time: O(1) 
    # Space: O(1)

# My Solution using the Zellers Congruence
def day_of_the_week(day, month, year):
    def zellers_congruence(day, month, year):
        # Adjust month and year for January and February
        if month <= 2:
            month += 12
            year -= 1

        # Calculate h using Zeller's Congruence formula
        h = (day + ((13 * (month + 1)) // 5) + year + (year // 4) - (year // 100) + (year // 400)) % 7

        return h
    
    day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return day_names[zellers_congruence(day, month, year)]
    # Time: O(1) 
    # Space: O(1)


def main():
    result = day_of_the_week(day = 31, month = 8, year = 2019)
    print(result) # "Saturday"

    result = day_of_the_week(day = 18, month = 7, year = 1999)
    print(result) # "Sunday"

    result = day_of_the_week(day = 15, month = 8, year = 1993)
    print(result) # "Sunday"

if __name__ == "__main__":
    main()
