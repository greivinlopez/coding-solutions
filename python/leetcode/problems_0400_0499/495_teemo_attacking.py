# --------------------
# 495. Teemo Attacking
# --------------------

# Problem: https://leetcode.com/problems/teemo-attacking
#
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo
# attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally,
# an attack at second t will mean Ashe is poisoned during the inclusive time
# interval [t, t + duration - 1]. If Teemo attacks again before the poison effect
# ends, the timer for it is reset, and the poison effect will end duration seconds
# after the new attack.
# 
# You are given a non-decreasing integer array timeSeries, where timeSeries[i]
# denotes that Teemo attacks Ashe at second timeSeries[i], and an integer
# duration.
# 
# Return the total number of seconds that Ashe is poisoned.
# 
# Example 1:
# 
# Input: timeSeries = [1,4], duration = 2
# Output: 4
# 
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
# 
# Example 2:
# 
# Input: timeSeries = [1,2], duration = 2
# Output: 3
# 
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is
# poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
# 
# 
# Constraints:
#         1 <= timeSeries.length <= 10⁴
#         0 <= timeSeries[i], duration <= 10⁷
#         timeSeries is sorted in non-decreasing order.


# Solution: https://algo.monster/liteproblems/495
# Credit: AlgoMonster
def find_poisoned_duration(timeSeries, duration):
    # If the time series is empty, return 0
    if not timeSeries:
        return 0
    
    # Initialize total poisoned time with the duration of the last attack
    total_poisoned_time = duration
    
    # Iterate through consecutive pairs of attack times
    for i in range(len(timeSeries) - 1):
        current_time = timeSeries[i]
        next_time = timeSeries[i + 1]
        
        # Calculate the actual poison duration between two attacks
        # If the next attack happens before the current poison effect ends,
        # the poison duration is limited by the time difference
        # Otherwise, the full duration is counted
        actual_duration = min(duration, next_time - current_time)
        
        # Add the actual duration to the total poisoned time
        total_poisoned_time += actual_duration
    
    return total_poisoned_time
    # Time: O(n)
    # Space: O(1)


def main():
    result = find_poisoned_duration(timeSeries = [1,4], duration = 2)
    print(result) # 4

    result = find_poisoned_duration(timeSeries = [1,2], duration = 2)
    print(result) # 3

if __name__ == "__main__":
    main()
