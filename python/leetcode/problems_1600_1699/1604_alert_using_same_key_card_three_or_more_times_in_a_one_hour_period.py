# ------------------------------------------------------------------------
# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
# ------------------------------------------------------------------------

# Problem: https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
#
# LeetCode company workers use key-cards to unlock office doors. Each time a
# worker uses their key-card, the security system saves the worker's name and the
# time when it was used. The system emits an alert if any worker uses the key-card
# three or more times in a one-hour period.
# 
# You are given a list of strings keyName and keyTime where [keyName[i],
# keyTime[i]] corresponds to a person's name and the time when their key-card was
# used in a single day.
# 
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and
# "09:49".
# 
# Return a list of unique worker names who received an alert for frequent keycard
# use. Sort the names in ascending order alphabetically.
# 
# Notice that "10:00" - "11:00" is considered to be within a one-hour period,
# while "22:51" - "23:52" is not considered to be within a one-hour period.
# 
# Example 1:
# 
# Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"],
# keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# Output: ["daniel"]
# Explanation: "daniel" used the keycard 3 times in a one-hour period
# ("10:00","10:40", "11:00").
# 
# Example 2:
# 
# Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime =
# ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# Output: ["bob"]
# Explanation: "bob" used the keycard 3 times in a one-hour period
# ("21:00","21:20", "21:30").
# 
# 
# Constraints:
#         1 <= keyName.length, keyTime.length <= 10⁵
#         keyName.length == keyTime.length
#         keyTime[i] is in the format "HH:MM".
#         [keyName[i], keyTime[i]] is unique.
#         1 <= keyName[i].length <= 10
#         keyName[i] contains only lowercase English letters.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1604
# Credit: AlgoMonster
def alert_names(keyName, keyTime):
    # Dictionary to store each person's access times
    name_to_times = defaultdict(list)
    
    # Convert time strings to minutes and group by name
    for name, time_str in zip(keyName, keyTime):
        # Convert "HH:MM" format to total minutes since midnight
        hours = int(time_str[:2])
        minutes = int(time_str[3:])
        total_minutes = hours * 60 + minutes
        name_to_times[name].append(total_minutes)
    
    # List to store names that triggered alerts
    alert_names = []
    
    # Check each person's access times
    for name, times in name_to_times.items():
        num_times = len(times)
        
        # Only check if person has 3 or more access times
        if num_times > 2:
            # Sort times in ascending order
            times.sort()
            
            # Check if any 3 consecutive times are within 60 minutes
            for i in range(num_times - 2):
                # If the time difference between i and i+2 is <= 60 minutes
                if times[i + 2] - times[i] <= 60:
                    alert_names.append(name)
                    break  # Found an alert, no need to check further
    
    # Sort names alphabetically before returning
    alert_names.sort()
    return alert_names
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = alert_names(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], 
                         keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"])
    print(result) # ['daniel']

    result = alert_names(keyName = ["alice","alice","alice","bob","bob","bob","bob"], 
                         keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"])
    print(result) # ['bob']

if __name__ == "__main__":
    main()
