# --------------------
# 174. Dungeon Game 😈
# --------------------

# Problem: https://leetcode.com/problems/dungeon-game
#
# The demons had captured the princess and imprisoned her in the bottom-right
# corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid.
# Our valiant knight was initially positioned in the top-left room and must fight
# his way through dungeon to rescue the princess.
# 
# The knight has an initial health point represented by a positive integer. If at
# any point his health point drops to 0 or below, he dies immediately.
# 
# Some of the rooms are guarded by demons (represented by negative integers), so
# the knight loses health upon entering these rooms; other rooms are either empty
# (represented as 0) or contain magic orbs that increase the knight's health
# (represented by positive integers).
# 
# To reach the princess as quickly as possible, the knight decides to move only
# rightward or downward in each step.
# 
# Return the knight's minimum initial health so that he can rescue the princess.
# 
# Note that any room can contain threats or power-ups, even the first room the
# knight enters and the bottom-right room where the princess is imprisoned.
# 
# Example 1:
# 
# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# 
# Explanation: The initial health of the knight must be at least 7 if he follows
# the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
# 
# Example 2:
# 
# Input: dungeon = [[0]]
# Output: 1
# 
# 
# Constraints:
#         m == dungeon.length
#         n == dungeon[i].length
#         1 <= m, n <= 200
#         -1000 <= dungeon[i][j] <= 1000

# Solution: https://leetcode.com/problems/dungeon-game/solutions/6288826/detailed-dry-run-with-diagram-beginner-friendly-memoization-step-by-step-solution
# Credit: Ayush Kumar Singh -> https://leetcode.com/u/ayushsingh03/
def solve(i, j, dungeon, dp):
    m, n = len(dungeon), len(dungeon[0])

    # Base case: Bottom-right cell (princess's room)
    if i == m - 1 and j == n - 1:
        return max(1, 1 - dungeon[i][j])

    # If out of bounds
    if i >= m or j >= n:
        return float('inf')

    # If the value is already calculated
    if dp[i][j] != -1:
        return dp[i][j]

    # Recursive calculation for the minimum health needed
    right = solve(i, j + 1, dungeon, dp)
    down = solve(i + 1, j, dungeon, dp)

    # The knight needs at least 1 health point to survive
    min_health = min(right, down) - dungeon[i][j]
    dp[i][j] = max(1, min_health)

    return dp[i][j]

def calculate_minimum_hp(dungeon):
    m, n = len(dungeon), len(dungeon[0])

    # Create a memoization table initialized with -1
    dp = [[-1] * n for _ in range(m)]

    # Start from the top-left cell
    return solve(0, 0, dungeon, dp)
    # Time: O(m * n)
    # Space: O(m * n)
    # m = number of rows
    # n = number of columns


def main():
    result = calculate_minimum_hp([[-2,-3,3],[-5,-10,1],[10,30,-5]])
    print(result) # 7

    result = calculate_minimum_hp([[0]])
    print(result) # 1

if __name__ == "__main__":
    main()
