# -----------------------------
# 1224. Maximum Equal Frequency
# -----------------------------

# Problem: https://leetcode.com/problems/maximum-equal-frequency
#
# Given an array nums of positive integers, return the longest possible length of
# an array prefix of nums, such that it is possible to remove exactly one element
# from this prefix so that every number that has appeared in it will have the same
# number of occurrences.
# 
# If after removing one element there are no remaining elements, it's still
# considered that every appeared number has the same number of ocurrences (0).
# 
# Example 1:
# 
# Input: nums = [2,2,1,1,5,3,3,5]
# Output: 7
# 
# Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]
# = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
# 
# Example 2:
# 
# Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# Output: 13
# 
# 
# Constraints:
#         2 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/1224
# Credit: AlgoMonster
def max_equal_freq(nums):
    # freq_count: maps each number to its frequency
    freq_count = {}
    
    # freq_freq_count: maps each frequency to how many numbers have that frequency
    freq_freq_count = {}
    
    max_length = 0
    max_frequency = 0
    
    for index, num in enumerate(nums, 1):
        # If number already exists, update frequency of frequencies
        if num in freq_count:
            old_freq = freq_count[num]
            freq_freq_count[old_freq] -= 1
            if freq_freq_count[old_freq] == 0:
                del freq_freq_count[old_freq]
        
        # Increment frequency of current number
        freq_count[num] = freq_count.get(num, 0) + 1
        new_freq = freq_count[num]
        
        # Update maximum frequency seen
        max_frequency = max(max_frequency, new_freq)
        
        # Update frequency of frequencies
        freq_freq_count[new_freq] = freq_freq_count.get(new_freq, 0) + 1
        
        # Check if current prefix is valid for removal of one element
        
        # Case 1: All elements appear exactly once (can remove any)
        if max_frequency == 1:
            max_length = index
        
        # Case 2: All elements have frequency max_frequency except one has (max_frequency - 1)
        # Remove one occurrence from the element with max_frequency
        elif (freq_freq_count.get(max_frequency, 0) * max_frequency + 
                freq_freq_count.get(max_frequency - 1, 0) * (max_frequency - 1) == index and 
                freq_freq_count.get(max_frequency, 0) == 1):
            max_length = index
        
        # Case 3: All elements have frequency max_frequency except one element appears once
        # Remove the element that appears once
        elif (freq_freq_count.get(max_frequency, 0) * max_frequency + 1 == index and 
                freq_freq_count.get(1, 0) == 1):
            max_length = index
        
        # Case 4: All elements have same frequency f, and one has frequency f+1
        # This is handled by Case 2 when max_frequency = f+1
        
        # Case 5: Only one unique number (all same)
        elif len(freq_count) == 1:
            max_length = index
        
        # Case 6: All have same frequency and total elements = (frequency + 1) * unique_count
        # Remove one from any element
        elif (len(freq_freq_count) == 1 and 
                (max_frequency + 1) * freq_freq_count.get(max_frequency, 0) == index):
            max_length = index
    
    return max_length
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_equal_freq(nums = [2,2,1,1,5,3,3,5])
    print(result) # 7

    result = max_equal_freq(nums = [1,1,1,2,2,2,3,3,3,4,4,4,5])
    print(result) # 13

if __name__ == "__main__":
    main()
