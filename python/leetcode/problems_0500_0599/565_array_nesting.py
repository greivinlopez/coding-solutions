# ------------------
# 565. Array Nesting
# ------------------

# Problem: https://leetcode.com/problems/array-nesting
#
# You are given an integer array nums of length n where nums is a permutation of
# the numbers in the range [0, n - 1].
# 
# You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ...} 
# subjected to the following rule:
#         
#   * The first element in s[k] starts with the selection of the element
#     nums[k] of index = k.
#   * The next element in s[k] should be nums[nums[k]], and then
#     nums[nums[nums[k]]], and so on.
#   * We stop adding right before a duplicate element occurs in s[k].
# 
# Return the longest length of a set s[k].
# 
# Example 1:
# 
# Input: nums = [5,4,0,3,1,6,2]
# Output: 4
# 
# Explanation:
# nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6,
# nums[6] = 2.
# One of the longest sets s[k]:
# s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
# 
# Example 2:
# 
# Input: nums = [0,1,2]
# Output: 1
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] < nums.length
#         All the values of nums are unique.


# Solution: https://algo.monster/liteproblems/565
# Credit: AlgoMonster
def array_nesting(nums):
    n = len(nums)
    visited = [False] * n  # Track which indices have been visited
    max_length = 0
    
    # Try starting from each unvisited index
    for start_index in range(n):
        if visited[start_index]:
            continue
        
        # Explore the cycle starting from current index
        current_index = nums[start_index]
        cycle_length = 1
        visited[current_index] = True
        
        # Follow the chain until we return to the starting element
        while nums[current_index] != nums[start_index]:
            current_index = nums[current_index]
            cycle_length += 1
            visited[current_index] = True
        
        # Update maximum length found so far
        max_length = max(max_length, cycle_length)
    
    return max_length
    # Time: O(n)
    # Space: O(n)


def main():
    result = array_nesting([5,4,0,3,1,6,2])
    print(result) # 4

    result = array_nesting([0,1,2])
    print(result) # 1

if __name__ == "__main__":
    main()
