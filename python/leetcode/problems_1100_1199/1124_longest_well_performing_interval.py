# --------------------------------------
# 1124. Longest Well-Performing Interval
# --------------------------------------

# Problem: https://leetcode.com/problems/longest-well-performing-interval
#
# We are given hours, a list of the number of hours worked per day for a given
# employee.
# 
# A day is considered to be a tiring day if and only if the number of hours worked
# is (strictly) greater than 8.
# 
# A well-performing interval is an interval of days for which the number of tiring
# days is strictly larger than the number of non-tiring days.
# 
# Return the length of the longest well-performing interval.
# 
# Example 1:
# 
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# 
# Explanation: The longest well-performing interval is [9,9,6].
# 
# Example 2:
# 
# Input: hours = [6,6,6]
# Output: 0
# 
# 
# Constraints:
#         1 <= hours.length <= 10⁴
#         0 <= hours[i] <= 16


# Solution: https://algo.monster/liteproblems/1124
# Credit: AlgoMonster
def longest_wpi(hours):
    # Initialize the maximum length of well-performing interval
    max_length = 0
    
    # Running prefix sum: +1 for tiring days (>8 hours), -1 for non-tiring days
    prefix_sum = 0
    
    # Dictionary to store the first occurrence index of each prefix sum value
    # Key: prefix sum value, Value: first index where this sum appears
    first_occurrence = {}
    
    # Iterate through each day's working hours
    for current_index, work_hours in enumerate(hours):
        # Update prefix sum: increment for tiring day, decrement for non-tiring day
        if work_hours > 8:
            prefix_sum += 1
        else:
            prefix_sum -= 1
        
        # Case 1: If prefix sum is positive, the entire interval [0, current_index] is well-performing
        # This means more tiring days than non-tiring days from the start
        if prefix_sum > 0:
            max_length = current_index + 1
        
        # Case 2: Check if we can find a valid subarray ending at current_index
        # We look for (prefix_sum - 1) because we want the subarray sum to be positive
        # If subarray [j+1, i] has sum > 0, then prefix_sum[i] - prefix_sum[j] > 0
        # So we need prefix_sum[j] < prefix_sum[i], and (prefix_sum - 1) is the largest such value
        elif prefix_sum - 1 in first_occurrence:
            max_length = max(max_length, current_index - first_occurrence[prefix_sum - 1])
        
        # Store the first occurrence of this prefix sum value
        # We only store the first occurrence because we want the longest possible interval
        if prefix_sum not in first_occurrence:
            first_occurrence[prefix_sum] = current_index
    
    return max_length
    # Time: O(n)
    # Space: O(n)


def main():
    result = longest_wpi(hours = [9,9,6,0,6,6,9])
    print(result) # 3

    result = longest_wpi(hours = [6,6,6])
    print(result) # 0

if __name__ == "__main__":
    main()
