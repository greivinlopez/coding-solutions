# --------------------------------------------
# 1736. Latest Time by Replacing Hidden Digits
# --------------------------------------------

# Problem: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits
#
# You are given a string time in the form of  hh:mm, where some of the digits in
# the string are hidden (represented by ?).
# 
# The valid times are those inclusively between 00:00 and 23:59.
# 
# Return the latest valid time you can get from time by replacing the hidden
# digits.
# 
# Example 1:
# 
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest
# minute ending with the digit '0' is 50.
# 
# Example 2:
# 
# Input: time = "0?:3?"
# Output: "09:39"
# 
# Example 3:
# 
# Input: time = "1?:22"
# Output: "19:22"
# 
# Constraints:
#         time is in the format hh:mm.
#         It is guaranteed that you can produce a valid time from the given string.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def maximum_time(time):
    hours, minutes = time.split(":")
    
    latest_hour = ""
    latest_min = ""
    
    if hours == "??":
        latest_hour = "23"
    
    elif hours[0] == "?":
        if int(hours[1]) <= 3:
            latest_hour = "2" + hours[1]
        else:
            latest_hour = "1" + hours[1]
    
    elif hours[1] == "?":
        if int(hours[0]) < 2:
            latest_hour = hours[0] + "9"
        else:
            latest_hour = hours[0] + "3"
    else:
        latest_hour = hours
    
    if minutes == "??":
        latest_min = "59"
    
    elif minutes[0] == "?":
        latest_min = "5" + minutes[1]
    
    elif minutes[1] == "?":
        latest_min = minutes[0] + "9"
    
    else:
        latest_min = minutes
    
    return latest_hour + ":" + latest_min
    # Time: O(1)
    # Space: O(1)


def main():
    result = maximum_time("2?:?0")
    print(result) # "23:50"

    result = maximum_time("0?:3?")
    print(result) # "09:39"

    result = maximum_time("1?:22")
    print(result) # "19:22"

if __name__ == "__main__":
    main()
