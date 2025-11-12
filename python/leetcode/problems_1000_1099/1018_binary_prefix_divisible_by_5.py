# ----------------------------------
# 1018. Binary Prefix Divisible By 5
# ----------------------------------

# Problem: https://leetcode.com/problems/binary-prefix-divisible-by-5
#
# You are given a binary array nums (0-indexed).
# 
# We define xi as the number whose binary representation is the subarray
# nums[0..i] (from most-significant-bit to least-significant-bit).
#         
#   * For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# 
# Return an array of booleans answer where answer[i] is true if xi is divisible by
# 5.
# 
# Example 1:
# 
# Input: nums = [0,1,1]
# Output: [true,false,false]
# 
# Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3
# in base-10.
# Only the first number is divisible by 5, so answer[0] is true.
# 
# Example 2:
# 
# Input: nums = [1,1,1]
# Output: [false,false,false]
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         nums[i] is either 0 or 1.


# Solution: https://algo.monster/liteproblems/1018
# Credit: AlgoMonster
def prefixes_div_by_5(nums):
    result = []
    current_value = 0
    
    for bit in nums:
        # Build the binary number incrementally:
        # - Left shift current value by 1 position (multiply by 2)
        # - Add the new bit using bitwise OR
        # - Take modulo 5 to prevent overflow and keep only remainder
        current_value = (current_value << 1 | bit) % 5
        
        # Check if current prefix forms a number divisible by 5
        # (remainder equals 0 means divisible by 5)
        result.append(current_value == 0)
    
    return result
    # Time: O(n)
    # Space: O(1)


def main():
    result = prefixes_div_by_5(nums = [0,1,1])
    print(result) # [True, False, False]

    result = prefixes_div_by_5(nums = [1,1,1])
    print(result) # [False, False, False]

if __name__ == "__main__":
    main()
