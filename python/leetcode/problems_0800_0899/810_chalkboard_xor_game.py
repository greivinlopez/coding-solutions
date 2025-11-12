# ------------------------
# 810. Chalkboard XOR Game
# ------------------------

# Problem: https://leetcode.com/problems/chalkboard-xor-game
#
# You are given an array of integers nums represents the numbers written on a
# chalkboard.
# 
# Alice and Bob take turns erasing exactly one number from the chalkboard, with
# Alice starting first. If erasing a number causes the bitwise XOR of all the
# elements of the chalkboard to become 0, then that player loses. The bitwise XOR
# of one element is that element itself, and the bitwise XOR of no elements is 0.
# 
# Also, if any player starts their turn with the bitwise XOR of all the elements
# of the chalkboard equal to 0, then that player wins.
# 
# Return true if and only if Alice wins the game, assuming both players play
# optimally.
# 
# Example 1:
# 
# Input: nums = [1,1,2]
# Output: false
# 
# Explanation:
# Alice has two choices: erase 1 or erase 2.
# If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the
# elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he
# wants, because Alice will be the one to erase the last element and she will
# lose.
# If Alice erases 2 first, now nums become [1, 1]. The bitwise XOR of all the
# elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
# 
# Example 2:
# 
# Input: nums = [0,1]
# Output: true
# 
# Example 3:
# 
# Input: nums = [1,2,3]
# Output: true
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         0 <= nums[i] < 2¹⁶

from functools import reduce
from operator import xor

# Solution: https://algo.monster/liteproblems/810
# Credit: AlgoMonster
def xor_game(nums):
    # Calculate the XOR of all elements in the array
    total_xor = reduce(xor, nums)
    
    # Alice wins if array length is even OR if XOR of all elements is 0
    return len(nums) % 2 == 0 or total_xor == 0
    # Time: O(n)
    # Space: O(1)


def main():
    result = xor_game([1,1,2])
    print(result) # False

    result = xor_game([0,1])
    print(result) # True

    result = xor_game([1,2,3])
    print(result) # True

if __name__ == "__main__":
    main()
