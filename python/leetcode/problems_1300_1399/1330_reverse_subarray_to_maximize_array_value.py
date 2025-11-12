# ----------------------------------------------
# 1330. Reverse Subarray To Maximize Array Value
# ----------------------------------------------

# Problem: https://leetcode.com/problems/reverse-subarray-to-maximize-array-value
#
# You are given an integer array nums. The value of this array is defined as the
# sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.
# 
# You are allowed to select any subarray of the given array and reverse it. You
# can perform this operation only once.
# 
# Find maximum possible value of the final array.
# 
# Example 1:
# 
# Input: nums = [2,3,1,5,4]
# Output: 10
# 
# Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4]
# whose value is 10.
# 
# Example 2:
# 
# Input: nums = [2,4,9,24,2,1,10]
# Output: 68
# 
# 
# Constraints:
#         2 <= nums.length <= 3 * 10⁴
#         -10⁵ <= nums[i] <= 10⁵
#         The answer is guaranteed to fit in a 32-bit integer.


# Solution: https://algo.monster/liteproblems/1330
# Credit: AlgoMonster
def max_value_after_reverse(nums):
    # Calculate the initial sum of absolute differences between adjacent elements
    initial_sum = sum(abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1))
    max_sum = initial_sum
    
    # Strategy 1: Try reversing subarrays that start at index 0
    # When we reverse [0, j], the edge at position j changes
    for i in range(len(nums) - 1):
        current_diff = abs(nums[i] - nums[i + 1])
        new_diff = abs(nums[0] - nums[i + 1])
        max_sum = max(max_sum, initial_sum + new_diff - current_diff)
    
    # Strategy 2: Try reversing subarrays that end at the last index
    # When we reverse [i, n-1], the edge at position i-1 changes
    for i in range(len(nums) - 1):
        current_diff = abs(nums[i] - nums[i + 1])
        new_diff = abs(nums[-1] - nums[i])
        max_sum = max(max_sum, initial_sum + new_diff - current_diff)
    
    # Strategy 3: Try reversing middle subarrays [i+1, j]
    # This changes edges at positions i and j
    # We use a mathematical optimization to find the best gain
    sign_patterns = [(1, -1), (-1, 1), (1, 1)]
    
    for sign1, sign2 in sign_patterns:
        max_value = float('-inf')
        min_value = float('inf')
        
        # For each adjacent pair, calculate potential gains
        for i in range(len(nums) - 1):
            x, y = nums[i], nums[i + 1]
            
            # Calculate the linear combination based on sign pattern
            linear_combination = sign1 * x + sign2 * y
            current_diff = abs(x - y)
            
            # Track maximum and minimum values for optimization
            max_value = max(max_value, linear_combination - current_diff)
            min_value = min(min_value, linear_combination + current_diff)
        
        # Calculate the maximum possible gain from this pattern
        gain = max(0, max_value - min_value)
        max_sum = max(max_sum, initial_sum + gain)
    
    return max_sum
    # Time: O(n)
    # Space: O(1)

# Alternative Solution: https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/solutions/6752984/super-easy-for-beginners-by-vigneshvaran-ekka
# Credit: VigneshS -> https://leetcode.com/u/vigneshvaran0101/
def max_value_after_reverse_alt(nums):
    maxMin = float('-inf')
    minMin = float('inf')
    s = 0
    boundary = float('-inf')
    for a,b in zip(nums[:-1], nums[1:]):
        distance = abs(a-b)
        boundary = max(boundary, max(abs(nums[-1]-a),abs(nums[0]-b))-distance)
        s += distance
        minMin = min(max(a,b), minMin)
        maxMin = max(min(a,b), maxMin)
    return s + max(2*(maxMin-minMin),boundary)
    # Time: O(n)
    # Space: O(1)


def main():
    result = max_value_after_reverse(nums = [2,3,1,5,4])
    print(result) # 10

    result = max_value_after_reverse(nums = [2,4,9,24,2,1,10])
    print(result) # 68

if __name__ == "__main__":
    main()
