# ----------------------------------
# 949. Largest Time for Given Digits
# ----------------------------------

# Problem: https://leetcode.com/problems/largest-time-for-given-digits
#
# Given an array arr of 4 digits, find the latest 24-hour time that can be made
# using each digit exactly once.
# 
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is
# between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# 
# Return the latest 24-hour time in "HH:MM" format. If no valid time can be made,
# return an empty string.
# 
# Example 1:
# 
# Input: arr = [1,2,3,4]
# Output: "23:41"
# 
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42",
# "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times,
# "23:41" is the latest.
# 
# Example 2:
# 
# Input: arr = [5,5,5,5]
# Output: ""
# 
# Explanation: There are no valid 24-hour times as "55:55" is not valid.
# 
# 
# Constraints:
#         arr.length == 4
#         0 <= arr[i] <= 9


# Solution: https://algo.monster/liteproblems/949
# Credit: AlgoMonster
def largest_time_from_digits(arr):
    # Count frequency of each digit in the input array
    digit_count = [0] * 10
    for digit in arr:
        digit_count[digit] += 1
    
    # Iterate through all possible times from 23:59 down to 00:00
    for hour in range(23, -1, -1):
        for minute in range(59, -1, -1):
            # Create frequency array for current time's digits
            time_digits = [0] * 10
            
            # Extract and count digits from hour (two digits)
            time_digits[hour // 10] += 1  # First digit of hour
            time_digits[hour % 10] += 1   # Second digit of hour
            
            # Extract and count digits from minute (two digits)
            time_digits[minute // 10] += 1  # First digit of minute
            time_digits[minute % 10] += 1   # Second digit of minute
            
            # Check if current time uses exactly the same digits as input
            if digit_count == time_digits:
                # Return the time in HH:MM format with leading zeros
                return f'{hour:02d}:{minute:02d}'
    
    # No valid time can be formed from the given digits
    return ''
    # Time: O(1)
    # Space: O(1)


def main():
    result = largest_time_from_digits(arr = [1,2,3,4])
    print(result) # "23:41"

    result = largest_time_from_digits(arr = [5,5,5,5])
    print(result) # ""

if __name__ == "__main__":
    main()
