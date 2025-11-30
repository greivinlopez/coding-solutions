# -----------------------
# 1690. Stone Game VII 🪨
# -----------------------

# Problem: https://leetcode.com/problems/stone-game-vii
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# There are n stones arranged in a row. On each player's turn, they can remove
# either the leftmost stone or the rightmost stone from the row and receive points
# equal to the sum of the remaining stones' values in the row. The winner is the
# one with the higher score when there are no stones left to remove.
# 
# Bob found that he will always lose this game (poor Bob, he always loses), so he
# decided to minimize the score's difference. Alice's goal is to maximize the
# difference in the score.
# 
# Given an array of integers stones where stones[i] represents the value of the
# ith stone from the left, return the difference in Alice and Bob's score if they
# both play optimally.
# 
# Example 1:
# 
# Input: stones = [5,3,1,4,2]
# Output: 6
# 
# Explanation:
# - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0,
# stones = [5,3,1,4].
# - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones =
# [3,1,4].
# - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones =
# [1,4].
# - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
# - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
# The score difference is 18 - 12 = 6.
# 
# Example 2:
# 
# Input: stones = [7,90,5,1,100,10,10,2]
# Output: 122
# 
# 
# Constraints:
#         n == stones.length
#         2 <= n <= 1000
#         1 <= stones[i] <= 1000


# Solution: https://algo.monster/liteproblems/1690
# Credit: AlgoMonster
def stone_game_vii(stones):
    from functools import cache
    from itertools import accumulate
    
    @cache
    def dfs(left, right):
        """
        Calculate the maximum score difference the current player can achieve
        from the subarray stones[left:right+1].
        
        Args:
            left: Left boundary index of the current stone range
            right: Right boundary index of the current stone range
            
        Returns:
            Maximum score difference the current player can achieve
        """
        # Base case: no stones left to pick
        if left > right:
            return 0
        
        # Option 1: Remove leftmost stone
        # Score gained: sum of remaining stones (excluding the removed one)
        # Subtract opponent's best score from the remaining subarray
        remove_left_score = prefix_sum[right + 1] - prefix_sum[left + 1] - dfs(left + 1, right)
        
        # Option 2: Remove rightmost stone
        # Score gained: sum of remaining stones (excluding the removed one)
        # Subtract opponent's best score from the remaining subarray
        remove_right_score = prefix_sum[right] - prefix_sum[left] - dfs(left, right - 1)
        
        # Choose the option that maximizes the current player's advantage
        return max(remove_left_score, remove_right_score)
    
    # Build prefix sum array for O(1) range sum queries
    # prefix_sum[i] = sum of stones[0:i]
    prefix_sum = list(accumulate(stones, initial=0))
    
    # Calculate the maximum score difference Alice can achieve
    result = dfs(0, len(stones) - 1)
    
    # Clear the cache to free memory
    dfs.cache_clear()
    
    return result
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = stone_game_vii(stones = [5,3,1,4,2])
    print(result) # 6

    result = stone_game_vii(stones = [7,90,5,1,100,10,10,2])
    print(result) # 122

if __name__ == "__main__":
    main()
