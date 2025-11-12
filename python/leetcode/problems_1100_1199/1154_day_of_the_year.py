# ---------------------
# 1154. Day of the Year
# ---------------------

# Problem: https://leetcode.com/problems/day-of-the-year
#
# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-
# DD, return the day number of the year.
# 
# Example 1:
# 
# Input: date = "2019-01-09"
# Output: 9
# 
# Explanation: Given date is the 9th day of the year in 2019.
# 
# Example 2:
# 
# Input: date = "2019-02-10"
# Output: 41
# 
# 
# Constraints:
#         date.length == 10
#         date[4] == date[7] == '-', and all other date[i]'s are digits
#         date represents a calendar date between Jan 1ˢᵗ, 1900 and Dec 31ˢᵗ, 2019.


# Solution: https://algo.monster/liteproblems/1154
# Credit: AlgoMonster
def day_of_year(date):
    # Parse the date string into year, month, and day components
    year, month, day = (int(s) for s in date.split('-'))
    
    # Determine if it's a leap year and set February days accordingly
    # Leap year conditions: divisible by 400 OR (divisible by 4 AND NOT divisible by 100)
    february_days = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
    
    # Days in each month (index 0 = January, index 1 = February, etc.)
    days_in_months = [31, february_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Calculate the day of year by summing all days in previous months plus current day
    return sum(days_in_months[:month - 1]) + day
    # Time: O(1)
    # Space: O(1)


def main():
    result = day_of_year(date = "2019-01-09")
    print(result) # 9

    result = day_of_year(date = "2019-02-10")
    print(result) # 41

if __name__ == "__main__":
    main()
