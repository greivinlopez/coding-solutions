# -------------------------
# 414. Third Maximum Number
# -------------------------

# Problem: https://leetcode.com/problems/third-maximum-number
#
# Given an integer array nums, return the third distinct maximum number in this
# array. If the third maximum does not exist, return the maximum number.
# 
# Example 1:
# 
# Input: nums = [3,2,1]
# Output: 1
# 
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# 
# Example 2:
# 
# Input: nums = [1,2]
# Output: 2
# 
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned
# instead.
# 
# Example 3:
# 
# Input: nums = [2,2,3,1]
# Output: 1
# 
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have
# the same value).
# The third distinct maximum is 1.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁴
#         -2³¹ <= nums[i] <= 2³¹ - 1
# 
# Follow up: Can you find an O(n) solution?


# Solution: https://leetcode.com/problems/third-maximum-number/solutions/352011/solution-in-python-3-beats-99-o-n
# Credit: Junaid Mansuri -> https://leetcode.com/u/junaidmansuri/
def third_max(nums):
    n, T = list(set(nums)), [float('-inf')]*3
    for i in n:
        if i > T[0]:
            T = [i,T[0],T[1]]
            continue
        if i > T[1]:
            T = [T[0],i,T[1]]
            continue
        if i > T[2]:
            T = [T[0],T[1],i]
    return T[2] if T[2] != float('-inf') else T[0]
    # Time: O(n)
    # Space: O(n)


def main():
    result = third_max([3,2,1])
    print(result) # 1

    result = third_max([1,2])
    print(result) # 2

    result = third_max([2,2,3,1])
    print(result) # 1

if __name__ == "__main__":
    main()
