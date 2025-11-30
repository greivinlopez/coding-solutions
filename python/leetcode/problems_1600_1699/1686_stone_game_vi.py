# ----------------------
# 1686. Stone Game VI 🪨
# ----------------------

# Problem: https://leetcode.com/problems/stone-game-vi
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# There are n stones in a pile. On each player's turn, they can remove a stone
# from the pile and receive points based on the stone's value. Alice and Bob may
# value the stones differently.
# 
# You are given two integer arrays of length n, aliceValues and bobValues. Each
# aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively,
# value the iᵗʰ stone.
# 
# The winner is the person with the most points after all the stones are chosen.
# If both players have the same amount of points, the game results in a draw. Both
# players will play optimally. Both players know the other's values.
# 
# Determine the result of the game, and:
# 
#         If Alice wins, return 1.
#         If Bob wins, return -1.
#         If the game results in a draw, return 0.
# 
# Example 1:
# 
# Input: aliceValues = [1,3], bobValues = [2,1]
# Output: 1
# 
# Explanation:
# If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
# Bob can only choose stone 0, and will only receive 2 points.
# Alice wins.
# 
# Example 2:
# 
# Input: aliceValues = [1,2], bobValues = [3,1]
# Output: 0
# 
# Explanation:
# If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
# Draw.
# 
# Example 3:
# 
# Input: aliceValues = [2,4,3], bobValues = [1,6,7]
# Output: -1
# 
# Explanation:
# Regardless of how Alice plays, Bob will be able to have more points than Alice.
# For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone
# 0, Alice will have 6 points to Bob's 7.
# Bob wins.
# 
# 
# Constraints:
#         n == aliceValues.length == bobValues.length
#         1 <= n <= 10⁵
#         1 <= aliceValues[i], bobValues[i] <= 100


# Solution: https://algo.monster/liteproblems/1686
# Credit: AlgoMonster
def stone_game_vi(aliceValues, bobValues):
    # Create list of (combined_value, index) pairs
    # Combined value represents the total impact of taking a stone:
    # - Alice gains aliceValues[i] and denies Bob bobValues[i]
    # - Bob gains bobValues[i] and denies Alice aliceValues[i]
    # So the strategic value for either player is the sum of both values
    combined_values = [(alice_val + bob_val, index) 
                        for index, (alice_val, bob_val) 
                        in enumerate(zip(aliceValues, bobValues))]
    
    # Sort by combined value in descending order (greedy approach)
    # Players should pick stones with highest combined value first
    combined_values.sort(reverse=True)
    
    # Alice takes stones at even indices (0, 2, 4, ...)
    alice_score = sum(aliceValues[index] 
                        for _, index in combined_values[::2])
    
    # Bob takes stones at odd indices (1, 3, 5, ...)
    bob_score = sum(bobValues[index] 
                    for _, index in combined_values[1::2])
    
    # Determine the winner
    if alice_score > bob_score:
        return 1  # Alice wins
    elif alice_score < bob_score:
        return -1  # Bob wins
    else:
        return 0  # Tie
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = word_break(params)
    print(result) # True

    result = word_break(params)
    print(result) # True

    result = word_break(params)
    print(result) # False

if __name__ == "__main__":
    main()
