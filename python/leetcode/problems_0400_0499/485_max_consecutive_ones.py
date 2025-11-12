# -------------------------
# 485. Max Consecutive Ones
# -------------------------

# Problem: https://leetcode.com/problems/max-consecutive-ones
#
# Given a binary array nums, return the maximum number of consecutive 1's in the
# array.
# 
# Example 1:
# 
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# 
# Explanation: The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.
# 
# Example 2:
# 
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         nums[i] is either 0 or 1.


# Solution: https://algo.monster/liteproblems/485
# Credit: AlgoMonster
def find_max_consecutive_ones(nums):
    max_consecutive = 0  # Track the maximum consecutive 1s found so far
    current_consecutive = 0  # Track the current consecutive 1s count
    
    # Iterate through each number in the array
    for num in nums:
        if num == 1:
            # If current number is 1, increment the consecutive counter
            current_consecutive += 1
            # Update maximum if current consecutive count is larger
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            # If current number is 0, reset the consecutive counter
            current_consecutive = 0
    
    return max_consecutive


def main():
    result = find_max_consecutive_ones([1,1,0,1,1,1])
    print(result) # 3

    result = find_max_consecutive_ones([1,0,1,1,0,1])
    print(result) # 2

if __name__ == "__main__":
    main()
