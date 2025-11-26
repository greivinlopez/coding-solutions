# ------------------------------------
# 1646. Get Maximum in Generated Array
# ------------------------------------

# Problem: https://leetcode.com/problems/get-maximum-in-generated-array
#
# You are given an integer n. A 0-indexed integer array nums of length n + 1 is
# generated in the following way:
#         
#   * nums[0] = 0
#   * nums[1] = 1
#   * nums[2 * i] = nums[i] when 2 <= 2 * i <= n
#   * nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# 
# Return the maximum integer in the array nums​​​.
# 
# Example 1:
# 
# Input: n = 7
# Output: 3
# 
# Explanation: According to the given rules:
#   nums[0] = 0
#   nums[1] = 1
#   nums[(1 * 2) = 2] = nums[1] = 1
#   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
#   nums[(2 * 2) = 4] = nums[2] = 1
#   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
#   nums[(3 * 2) = 6] = nums[3] = 2
#   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
# Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.
# 
# Example 2:
# 
# Input: n = 2
# Output: 1
# 
# Explanation: According to the given rules, nums = [0,1,1]. The maximum is
# max(0,1,1) = 1.
# 
# Example 3:
# 
# Input: n = 3
# Output: 2
# 
# Explanation: According to the given rules, nums = [0,1,1,2]. The maximum is
# max(0,1,1,2) = 2.
# 
# 
# Constraints:
#         0 <= n <= 100


# Solution: https://algo.monster/liteproblems/1646
# Credit: AlgoMonster
def get_maximum_generated(n):
    # Handle base cases where n is 0 or 1
    if n < 2:
        return n
    
    # Initialize array to store generated sequence
    nums = [0] * (n + 1)
    nums[1] = 1
    
    # Generate the sequence according to the rules:
    # - If index i is even: nums[i] = nums[i/2]
    # - If index i is odd: nums[i] = nums[i/2] + nums[i/2 + 1]
    for i in range(2, n + 1):
        if i % 2 == 0:
            # Even index: value equals the value at half the index
            nums[i] = nums[i >> 1]
        else:
            # Odd index: value equals sum of values at floor(i/2) and floor(i/2) + 1
            nums[i] = nums[i >> 1] + nums[(i >> 1) + 1]
    
    # Return the maximum value in the generated array
    return max(nums)
    # Time: O(n)
    # Space: O(n)


def main():
    result = get_maximum_generated(n = 7)
    print(result) # 3

    result = get_maximum_generated(n = 2)
    print(result) # 1

    result = get_maximum_generated(n = 3)
    print(result) # 2

if __name__ == "__main__":
    main()
