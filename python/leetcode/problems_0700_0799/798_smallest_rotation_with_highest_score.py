# -----------------------------------------
# 798. Smallest Rotation with Highest Score
# -----------------------------------------

# Problem: https://leetcode.com/problems/smallest-rotation-with-highest-score
#
# You are given an array nums. You can rotate it by a non-negative integer k so
# that the array becomes [nums[k], nums[k + 1], ... nums[nums.length - 1],
# nums[0], nums[1], ..., nums[k-1]]. Afterward, any entries that are less than or
# equal to their index are worth one point.
#         
#   * For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it
#     becomes [1,3,0,2,4]. This is worth 3 points because 1 > 0 [no points], 3 > 1 
#     [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
# 
# Return the rotation index k that corresponds to the highest score we can achieve
# if we rotated nums by it. If there are multiple answers, return the smallest
# such index k.
# 
# Example 1:
# 
# Input: nums = [2,3,1,4,0]
# Output: 3
# 
# Explanation: Scores for each k are listed below:
# k = 0,  nums = [2,3,1,4,0],    score 2
# k = 1,  nums = [3,1,4,0,2],    score 3
# k = 2,  nums = [1,4,0,2,3],    score 3
# k = 3,  nums = [4,0,2,3,1],    score 4
# k = 4,  nums = [0,2,3,1,4],    score 3
# So we should choose k = 3, which has the highest score.
# 
# Example 2:
# 
# Input: nums = [1,3,0,2,4]
# Output: 0
# 
# Explanation: nums will always have 3 points no matter how it shifts.
# So we will choose the smallest k, which is 0.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] < nums.length


# Solution: https://algo.monster/liteproblems/798
# Credit: AlgoMonster
def best_rotation(nums):
    n = len(nums)
    
    # Initialize variables to track the best rotation
    max_score = -1
    best_rotation = n
    
    # Use difference array to efficiently track score changes
    # diff[k] represents the change in score when rotating by k positions
    diff = [0] * n
    
    # For each element, calculate the range of rotations where it contributes to the score
    for index, value in enumerate(nums):
        # Calculate the rotation range where nums[index] contributes 1 point
        # After k rotations, element at index i moves to position (i - k + n) % n
        # We need: value <= (index - k + n) % n, which means k is in range [left, right)
        
        # Start of valid rotation range (inclusive)
        left = (index + 1) % n
        
        # End of valid rotation range (exclusive)
        # Derived from: value <= (index - k + n) % n
        right = (n + index + 1 - value) % n
        
        # Mark the range in the difference array
        diff[left] += 1
        diff[right] -= 1
    
    # Use prefix sum to calculate actual scores for each rotation
    current_score = 0
    for rotation_k, delta in enumerate(diff):
        current_score += delta
        
        # Update the best rotation if current score is better
        if current_score > max_score:
            max_score = current_score
            best_rotation = rotation_k
    
    return best_rotation
    # Time: O(n)
    # Space: O(n)


def main():
    result = best_rotation(nums = [2,3,1,4,0])
    print(result) # 3

    result = best_rotation(nums = [1,3,0,2,4])
    print(result) # 0

if __name__ == "__main__":
    main()
