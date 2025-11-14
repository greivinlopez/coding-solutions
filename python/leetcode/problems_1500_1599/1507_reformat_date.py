# ----------------------
# 1507. Reformat Date 📅
# ----------------------

# Problem: https://leetcode.com/problems/reformat-date
#
# Given a date string in the form Day Month Year, where:
#         
#   * Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
#   * Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
#     "Aug", "Sep", "Oct", "Nov", "Dec"}.
#   * Year is in the range [1900, 2100].
# 
# Convert the date string to the format YYYY-MM-DD, where:
#   * YYYY denotes the 4 digit year.
#   * MM denotes the 2 digit month.
#   * DD denotes the 2 digit day.
# 
# Example 1:
# 
# Input: date = "20th Oct 2052"
# Output: "2052-10-20"
# 
# Example 2:
# 
# Input: date = "6th Jun 1933"
# Output: "1933-06-06"
# 
# Example 3:
# 
# Input: date = "26th May 1960"
# Output: "1960-05-26"
# 
# 
# Constraints:
#   The given dates are guaranteed to be valid, so no error handling is necessary.


# Solution: https://algo.monster/liteproblems/1507
# Credit: AlgoMonster
def reformat_date(date):
    # Split the date string into components (day, month, year)
    date_parts = date.split()
    
    # Reverse the list to get [year, month, day] order
    date_parts.reverse()
    
    # Month abbreviations lookup string (each month takes 3 characters)
    # Starting with a space to make January index 3 (position 1 * 3)
    month_lookup = " JanFebMarAprMayJunJulAugSepOctNovDec"
    
    # Convert month abbreviation to month number (01-12)
    # Find the index of the month string and divide by 3 to get month number
    month_index = month_lookup.index(date_parts[1])
    month_number = month_index // 3 + 1
    date_parts[1] = str(month_number).zfill(2)
    
    # Extract day number by removing the suffix (st, nd, rd, th)
    # and pad with zero if single digit
    day_number = date_parts[2][:-2]
    date_parts[2] = day_number.zfill(2)
    
    # Join the parts with hyphen to form YYYY-MM-DD format
    return "-".join(date_parts)
    # Time: O(1)
    # Space: O(1)


def main():
    result = reformat_date(date = "20th Oct 2052")
    print(result) # "2052-10-20"

    result = reformat_date(date = "6th Jun 1933")
    print(result) # "1933-06-06"

    result = reformat_date(date = "26th May 1960")
    print(result) # "1960-05-26"

if __name__ == "__main__":
    main()
