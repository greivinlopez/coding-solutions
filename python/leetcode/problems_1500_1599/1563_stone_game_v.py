# ------------------
# 1563. Stone Game V
# ------------------

# Problem: https://leetcode.com/problems/stone-game-v
#
# There are several stones arranged in a row, and each stone has an associated
# value which is an integer given in the array stoneValue.
# 
# In each round of the game, Alice divides the row into two non-empty rows (i.e.
# left row and right row), then Bob calculates the value of each row which is the
# sum of the values of all the stones in this row. Bob throws away the row which
# has the maximum value, and Alice's score increases by the value of the remaining
# row. If the value of the two rows are equal, Bob lets Alice decide which row
# will be thrown away. The next round starts with the remaining row.
# 
# The game ends when there is only one stone remaining. Alice's score is initially
# zero.
# 
# Return the maximum score that Alice can obtain.
# 
# Example 1:
# 
# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# 
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The
# left row has the value 11 and the right row has value 14. Bob throws away the
# right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws
# away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3].
# Bob throws away the right row and Alice's score is now 18 (16 + 2). The game
# ends because only one stone is remaining in the row.
# 
# Example 2:
# 
# Input: stoneValue = [7,7,7,7,7,7,7]
# Output: 28
# 
# Example 3:
# 
# Input: stoneValue = [4]
# Output: 0
# 
# 
# Constraints:
#         1 <= stoneValue.length <= 500
#         1 <= stoneValue[i] <= 10⁶

from functools import cache
from itertools import accumulate

# Solution: https://algo.monster/liteproblems/1563
# Credit: AlgoMonster
def stone_game_v(stoneValue):
    @cache
    def dp(left, right):
        # Base case: if range is invalid or contains single stone, no score
        if left >= right:
            return 0
        
        max_score = 0
        left_sum = 0
        # Calculate right sum using prefix sum array
        right_sum = prefix_sum[right + 1] - prefix_sum[left]
        
        # Try all possible split points
        for split_point in range(left, right):
            # Update sums after including current stone in left group
            left_sum += stoneValue[split_point]
            right_sum -= stoneValue[split_point]
            
            if left_sum < right_sum:
                # Left group has smaller sum, Alice gets left_sum points
                # Pruning: skip if current max_score is already >= 2 * left_sum
                if max_score >= left_sum * 2:
                    continue
                max_score = max(max_score, left_sum + dp(left, split_point))
                
            elif left_sum > right_sum:
                # Right group has smaller sum, Alice gets right_sum points
                # Pruning: break early if max_score is already >= 2 * right_sum
                if max_score >= right_sum * 2:
                    break
                max_score = max(max_score, right_sum + dp(split_point + 1, right))
                
            else:
                # Both groups have equal sum, Alice chooses the better option
                max_score = max(
                    max_score,
                    max(left_sum + dp(left, split_point), 
                        right_sum + dp(split_point + 1, right))
                )
        
        return max_score
    
    # Build prefix sum array for efficient range sum queries
    # prefix_sum[i] = sum of stoneValue[0:i]
    prefix_sum = list(accumulate(stoneValue, initial=0))
    
    # Start the recursive solution from the entire array
    return dp(0, len(stoneValue) - 1)
    # Time: O(n³)
    # Space: O(n²)


def main():
    result = stone_game_v(stoneValue = [6,2,3,4,5,5])
    print(result) # 18

    result = stone_game_v(stoneValue = [7,7,7,7,7,7,7])
    print(result) # 28

    result = stone_game_v(stoneValue = [4])
    print(result) # 0

if __name__ == "__main__":
    main()
