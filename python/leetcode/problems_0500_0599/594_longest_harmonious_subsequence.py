# -----------------------------------
# 594. Longest Harmonious Subsequence
# -----------------------------------

# Problem: https://leetcode.com/problems/longest-harmonious-subsequence
#
# We define a harmonious array as an array where the difference between its
# maximum value and its minimum value is exactly 1.
# 
# Given an integer array nums, return the length of its longest harmonious
# subsequence among all its possible subsequences.
# 
# Example 1:
# 
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# 
# Explanation:
# The longest harmonious subsequence is [3,2,2,2,3].
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: 2
# 
# Explanation:
# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which
# have a length of 2.
# 
# Example 3:
# 
# Input: nums = [1,1,1,1]
# Output: 0
# 
# Explanation:
# No harmonic subsequence exists.
# 
# 
# Constraints:
#         1 <= nums.length <= 2 * 10⁴
#         -10⁹ <= nums[i] <= 10⁹

# Credit: Jeel Gajera -> https://github.com/JeelGajera
def find_LHS_alt(nums):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    max_length = 0
    for num in freq_map:
        if num+1 in freq_map:
            max_length = max(max_length, freq_map[num]+freq_map[num+1])
    return max_length
    # Time: O(n)
    # Space: O(k)
    # n = the number of elements in the input list.
    # k = the number of unique elements in the input list.

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_LHS(nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    ans = 0
    
    for num in dic:
        if num+1 in dic:
            ans = max(ans, dic[num]+dic[num+1])
    
    return ans
    # Time: O(n)
    # Space: O(k)
    # n = the number of elements in the input list.
    # k = the number of unique elements in the input list.


def main():
    result = find_LHS(nums = [1,3,2,2,5,2,3,7])
    print(result) # 5

    result = find_LHS(nums = [1,2,3,4])
    print(result) # 2

    result = find_LHS(nums = [1,1,1,1])
    print(result) # 0

if __name__ == "__main__":
    main()
