# --------------------
# 546. Remove Boxes 📦
# --------------------

# Problem: https://leetcode.com/problems/remove-boxes
#
# You are given several boxes with different colors represented by different
# positive numbers.
# 
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (i.e.,
# composed of k boxes, k >= 1), remove them and get k * k points.
# 
# Return the maximum points you can get.
# 
# Example 1:
# 
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# 
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
# 
# Example 2:
# 
# Input: boxes = [1,1,1]
# Output: 9
# 
# Example 3:
# 
# Input: boxes = [1]
# Output: 1
# 
# 
# Constraints:
#         1 <= boxes.length <= 100
#         1 <= boxes[i] <= 100

from functools import cache

# Solution: https://algo.monster/liteproblems/546
# Credit: AlgoMonster
def remove_boxes(boxes):
    @cache
    def dfs(left, right, extra_count):
        # Base case: no boxes left
        if left > right:
            return 0
        
        # Optimization: merge consecutive boxes of same color at the right end
        # This reduces redundant states in memoization
        while left < right and boxes[right] == boxes[right - 1]:
            right -= 1
            extra_count += 1
        
        # Option 1: Remove boxes[right] along with extra_count boxes of same color
        max_points = dfs(left, right - 1, 0) + (extra_count + 1) * (extra_count + 1)
        
        # Option 2: Try to merge boxes[right] with boxes[mid] where they have same color
        # Split the problem into two subproblems
        for mid in range(left, right):
            if boxes[mid] == boxes[right]:
                # Remove boxes between mid and right first, then merge boxes[mid] with boxes[right]
                points = (dfs(mid + 1, right - 1, 0) + 
                            dfs(left, mid, extra_count + 1))
                max_points = max(max_points, points)
        
        return max_points
    
    # Calculate result for entire array
    n = len(boxes)
    result = dfs(0, n - 1, 0)
    
    # Clear cache to free memory
    dfs.cache_clear()
    
    return result
    # Time: O(n⁴)
    # Space: O(n³)


def main():
    result = remove_boxes(boxes = [1,3,2,2,2,3,4,3,1])
    print(result) # 23

    result = remove_boxes(boxes = [1,1,1])
    print(result) # 9

    result = remove_boxes(boxes = [1])
    print(result) # 1

if __name__ == "__main__":
    main()
