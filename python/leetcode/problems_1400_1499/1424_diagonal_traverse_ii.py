# --------------------------
# 1424. Diagonal Traverse II
# --------------------------

# Problem: https://leetcode.com/problems/diagonal-traverse-ii
#
# Given a 2D integer array nums, return all elements of nums in diagonal order as
# shown in the below images.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png
# 
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# 
# Example 2:
# 
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i].length <= 10⁵
#         1 <= sum(nums[i].length) <= 10⁵
#         1 <= nums[i][j] <= 10⁵

from collections import deque

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_diagonal_order(nums):
    queue = deque([(0, 0)])
    ans = []
    
    while queue:
        row, col = queue.popleft()
        ans.append(nums[row][col])
        
        if col == 0 and row + 1 < len(nums):
            queue.append((row + 1, col))
        
        if col + 1 < len(nums[row]):
            queue.append((row, col + 1))
    
    return ans
    # Time: O(n)
    # Space: O(n)


def main():
    result = find_diagonal_order([[1,2,3],[4,5,6],[7,8,9]])
    print(result) # [1,4,2,7,5,3,8,6,9]

    result = find_diagonal_order([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    print(result) # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

if __name__ == "__main__":
    main()
