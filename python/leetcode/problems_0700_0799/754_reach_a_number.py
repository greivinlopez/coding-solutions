# -------------------
# 754. Reach a Number
# -------------------

# Problem: https://leetcode.com/problems/reach-a-number
#
# You are standing at position 0 on an infinite number line. There is a
# destination at position target.
# 
# You can make some number of moves numMoves so that:
#         
#   * On each move, you can either go left or right.
#   * During the ith move (starting from i == 1 to i == numMoves), you take i
#     steps in the chosen direction.
# 
# Given the integer target, return the minimum number of moves required (i.e., the
# minimum numMoves) to reach the destination.
# 
# Example 1:
# 
# Input: target = 2
# Output: 3
# 
# Explanation:
# On the 1ˢᵗ move, we step from 0 to 1 (1 step).
# On the 2ⁿᵈ move, we step from 1 to -1 (2 steps).
# On the 3ʳᵈ move, we step from -1 to 2 (3 steps).
# 
# Example 2:
# 
# Input: target = 3
# Output: 2
# 
# Explanation:
# On the 1ˢᵗ move, we step from 0 to 1 (1 step).
# On the 2ⁿᵈ move, we step from 1 to 3 (2 steps).
# 
# 
# Constraints:
#         -10⁹ <= target <= 10⁹
#         target != 0

import math

# Solution: https://algo.monster/liteproblems/754
# Credit: AlgoMonster
def reach_number_to(target):
    # Since we can mirror any sequence of moves, we only need to consider positive targets
    target = abs(target)
    
    # Initialize sum of steps and step counter
    current_sum = 0
    step = 0
    
    # Keep adding steps until we meet the conditions
    while True:
        # We can reach the target when:
        # 1. The sum of steps is at least the target
        # 2. The difference between sum and target is even (we can flip some steps)
        if current_sum >= target and (current_sum - target) % 2 == 0:
            return step
        
        # Move to the next step
        step += 1
        current_sum += step
    # Time: O(√|target|)
    # Space: O(1)

# Alternative Solution: More efficient
# Solution: https://leetcode.com/problems/reach-a-number/solutions/3788925/o-1-walkthrough-with-3-solutions-intuition-python
# Credit: Jason -> https://leetcode.com/u/jasonqiu212/
def reach_number(target):
    target = abs(target)
    m = math.ceil((math.sqrt(1 + 8 * target) - 1) / 2)
    total = m * (m + 1) / 2
    
    if (total - target) % 2 == 0:
        return m
    return m + 2 if m % 2 == 1 else m + 1
    # Time: O(1)
    # Space: O(1)


def main():
    result = reach_number(target = 2)
    print(result) # 3

    result = reach_number(target = 3)
    print(result) # 2

if __name__ == "__main__":
    main()
