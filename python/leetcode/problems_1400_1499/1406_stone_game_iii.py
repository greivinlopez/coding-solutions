# -----------------------
# 1406. Stone Game III 🪨
# -----------------------

# Problem: https://leetcode.com/problems/stone-game-iii
#
# Alice and Bob continue their games with piles of stones. There are several
# stones arranged in a row, and each stone has an associated value which is an
# integer given in the array stoneValue.
# 
# Alice and Bob take turns, with Alice starting first. On each player's turn, that
# player can take 1, 2, or 3 stones from the first remaining stones in the row.
# 
# The score of each player is the sum of the values of the stones taken. The score
# of each player is 0 initially.
# 
# The objective of the game is to end with the highest score, and the winner is
# the player with the highest score and there could be a tie. The game continues
# until all the stones have been taken.
# 
# Assume Alice and Bob play optimally.
# 
# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will
# end the game with the same score.
# 
# Example 1:
# 
# Input: stoneValue = [1,2,3,7]
# Output: "Bob"
# 
# Explanation: Alice will always lose. Her best move will be to take three piles
# and the score become 6. Now the score of Bob is 7 and Bob wins.
# 
# Example 2:
# 
# Input: stoneValue = [1,2,3,-9]
# Output: "Alice"
# 
# Explanation: Alice must choose all the three piles at the first move to win and
# leave Bob with negative score.
# If Alice chooses one pile her score will be 1 and the next move Bob's score
# becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
# If Alice chooses two piles her score will be 3 and the next move Bob's score
# becomes 3. In the next move, Alice will take the pile with value = -9 and also
# lose.
# Remember that both play optimally so here Alice will choose the scenario that
# makes her win.
# 
# Example 3:
# 
# Input: stoneValue = [1,2,3,6]
# Output: "Tie"
# 
# Explanation: Alice cannot win this game. She can end the game in a draw if she
# decided to choose all the first three piles, otherwise she will lose.
# 
# 
# Constraints:
#         1 <= stoneValue.length <= 5 * 10⁴
#         -1000 <= stoneValue[i] <= 1000


# Solution: https://algo.monster/liteproblems/1406
# Credit: AlgoMonster
def stone_game_iii(stoneValue):
    from functools import cache
    from math import inf
    
    @cache
    def dfs(index):
        # Base case: no stones left
        if index >= n:
            return 0
        
        # Try taking 1, 2, or 3 stones and find the best outcome
        max_score_diff = -inf
        current_sum = 0
        
        for num_stones in range(3):
            # Check if we can take this many stones
            if index + num_stones >= n:
                break
            
            # Add the stone value to current sum
            current_sum += stoneValue[index + num_stones]
            
            # Calculate score difference:
            # current_sum (what we take) - dfs(next) (opponent's best from remaining)
            score_diff = current_sum - dfs(index + num_stones + 1)
            max_score_diff = max(max_score_diff, score_diff)
        
        return max_score_diff
    
    # Initialize game parameters
    n = len(stoneValue)
    
    # Get Alice's maximum score difference
    alice_score_diff = dfs(0)
    
    # Determine winner based on score difference
    if alice_score_diff == 0:
        return 'Tie'
    elif alice_score_diff > 0:
        return 'Alice'
    else:
        return 'Bob'
    # Time: O(n)
    # Space: O(n)


def main():
    result = stone_game_iii(stoneValue = [1,2,3,7])
    print(result) # "Bob"

    result = stone_game_iii(stoneValue = [1,2,3,-9])
    print(result) # "Alice"

    result = stone_game_iii(stoneValue = [1,2,3,6])
    print(result) # "Tie"

if __name__ == "__main__":
    main()
