# ----------------
# 456. 132 Pattern
# ----------------

# Problem: https://leetcode.com/problems/132-pattern/
# 
# Given an array of n integers nums, a 132 pattern is a subsequence of three 
# integers nums[i], nums[j] and nums[k] such that i < j < k and 
# nums[i] < nums[k] < nums[j].
# 
# Return true if there is a 132 pattern in nums, otherwise, return false.
#  
# Example 1:
# 
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
# 
# 
# Example 2:
# 
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# 
# 
# Example 3:
# 
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
# 
# 
# Constraints:
# 
# 	n == nums.length
# 	1 <= n <= 2 * 10^5
# 	-10^9 <= nums[i] <= 10^9


# Solution: https://youtu.be/q5ANAl8Z458
# Credit: Navdeep Singh founder of NeetCode
def find_132_pattern(nums):
    stack = [] # pair [num, curLeftMin], mono-decreasing stack
    curMin = nums[0]

    for n in nums:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n < stack[-1][0] and n > stack[-1][1]:
            return True

        stack.append([n, curMin]) 
        curMin = min(n, curMin)

    return False


def main():
    result = find_132_pattern([1,2,3,4])
    print(result) # False

    result = find_132_pattern([3,1,4,2])
    print(result) # True

    result = find_132_pattern([-1,3,2,0])
    print(result) # True

if __name__ == "__main__":
    main()
