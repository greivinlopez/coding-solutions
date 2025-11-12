# ----------------------
# 398. Random Pick Index
# ----------------------

# Problem: https://leetcode.com/problems/random-pick-index
#
# Given an integer array nums with possible duplicates, randomly output the index
# of a given target number. You can assume that the given target number must exist
# in the array.
# 
# Implement the Solution class:
#         
#   * Solution(int[] nums) Initializes the object with the array nums.
#   * int pick(int target) Picks a random index i from nums where nums[i] ==
#     target. If there are multiple valid i's, then each index should have an equal
#     probability of returning.
# 
# Example 1:
# 
# Input
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# Output
# [null, 4, 0, 2]
# 
# Explanation
# Solution solution = new Solution([1, 2, 3, 3, 3]);
# solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each
# index should have equal probability of returning.
# solution.pick(1); // It should return 0. Since in the array only nums[0] is
# equal to 1.
# solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each
# index should have equal probability of returning.
# 
# 
# Constraints:
#         1 <= nums.length <= 2 * 10⁴
#         -2³¹ <= nums[i] <= 2³¹ - 1
#         target is an integer from nums.
#         At most 10⁴ calls will be made to pick.

from collections import defaultdict
import random

# Solution: https://leetcode.com/problems/random-pick-index/solutions/4042503/97-87-python3-c-c-c-java-randomized-index-selection-for-target-values-in-an-array
# Credit: https://leetcode.com/u/MrAke/
class Solution:
    def __init__(self, nums):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target):
        return random.choice(self.indices[target])


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
