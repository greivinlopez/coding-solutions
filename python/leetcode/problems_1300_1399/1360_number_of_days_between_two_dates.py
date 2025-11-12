# -----------------------------------------
# 1360. Number of Days Between Two Dates 📅
# -----------------------------------------

# Problem: https://leetcode.com/problems/number-of-days-between-two-dates
#
# Write a program to count the number of days between two dates.
# 
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the
# examples.
# 
# Example 1:
# 
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# 
# Example 2:
# 
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
# 
# 
# Constraints:
#         The given dates are valid dates between the years 1971 and 2100.


# Solution: https://algo.monster/liteproblems/1360
# Credit: AlgoMonster
def days_between_dates(date1, date2):

    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def days_in_month(year, month):
        # Days in each month (index 0 = January, index 11 = December)
        days_per_month = [
            31,  # January
            28 + int(is_leap_year(year)),  # February (28 or 29 days)
            31,  # March
            30,  # April
            31,  # May
            30,  # June
            31,  # July
            31,  # August
            30,  # September
            31,  # October
            30,  # November
            31   # December
        ]
        return days_per_month[month - 1]
    
    def calculate_days_since_epoch(date):
        # Parse the date string
        year, month, day = map(int, date.split("-"))
        
        total_days = 0
        
        # Add days for all complete years from 1971 to (year - 1)
        for y in range(1971, year):
            total_days += 365 + int(is_leap_year(y))
        
        # Add days for all complete months in the current year
        for m in range(1, month):
            total_days += days_in_month(year, m)
        
        # Add the days in the current month
        total_days += day
        
        return total_days
    
    # Calculate the absolute difference between the two dates
    return abs(calculate_days_since_epoch(date1) - calculate_days_since_epoch(date2))
    # Time: O(y + m)
    # Space: O(1)
    # y = represents the number of years between the given date and the base year 1971
    # m = he month value of the given date (ranging from 1 to 12).


def main():
    result = days_between_dates(date1 = "2019-06-29", date2 = "2019-06-30")
    print(result) # 1

    result = days_between_dates(date1 = "2020-01-15", date2 = "2019-12-31")
    print(result) # 15

if __name__ == "__main__":
    main()
