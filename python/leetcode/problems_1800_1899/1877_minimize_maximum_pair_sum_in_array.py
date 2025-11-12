# ----------------------------------------
# 1877. Minimize Maximum Pair Sum in Array
# ----------------------------------------

# Problem: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array
#
# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the
# largest pair sum in a list of pairs.
# 
#   * For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair
#     sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# 
# Given an array nums of even length n, pair up the elements of nums into n / 2
# pairs such that:
#         Each element of nums is in exactly one pair, and
#         The maximum pair sum is minimized.
# 
# Return the minimized maximum pair sum after optimally pairing up the elements.
# 
# Example 1:
# 
# Input: nums = [3,5,2,3]
# Output: 7
# 
# Explanation: The elements can be paired up into pairs (3,3) and (5,2).
# The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
# 
# Example 2:
# 
# Input: nums = [3,5,4,2,4,6]
# Output: 8
# 
# Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
# The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
# 
# 
# Constraints:
#         n == nums.length
#         2 <= n <= 10⁵
#         n is even.
#         1 <= nums[i] <= 10⁵


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def min_pair_sum(nums):
    max_val = float('-inf')
    min_val = float('inf')
    hash_map = [0] * 100001

    for num in nums:
        hash_map[num] += 1
        max_val = max(max_val, num)
        min_val = min(min_val, num)

    low = min_val
    high = max_val
    max_val = float('-inf')
    while low <= high:
        if hash_map[low] == 0:
            low += 1
        elif hash_map[high] == 0:
            high -= 1
        else:
            max_val = max(max_val, low + high)
            hash_map[low] -= 1
            hash_map[high] -= 1

    return max_val
    # Time: O(n + m)
    # Space: O(m)
    # n = length of the input array
    # m = maximum possible value an element in nums


def main():
    result = min_pair_sum([3,5,2,3])
    print(result) # 7

    result = min_pair_sum([3,5,4,2,4,6])
    print(result) # 8

if __name__ == "__main__":
    main()
