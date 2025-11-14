# ----------------------
# 1510. Stone Game IV 🪨
# ----------------------

# Problem: https://leetcode.com/problems/stone-game-iv
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# Initially, there are n stones in a pile. On each player's turn, that player
# makes a move consisting of removing any non-zero square number of stones in the
# pile.
# 
# Also, if a player cannot make a move, he/she loses the game.
# 
# Given a positive integer n, return true if and only if Alice wins the game
# otherwise return false, assuming both players play optimally.
# 
# Example 1:
# 
# Input: n = 1
# Output: true
# 
# Explanation: Alice can remove 1 stone winning the game because Bob doesn't have
# any moves.
# 
# Example 2:
# 
# Input: n = 2
# Output: false
# 
# Explanation: Alice can only remove 1 stone, after that Bob removes the last one
# winning the game (2 -> 1 -> 0).
# 
# Example 3:
# 
# Input: n = 4
# Output: true
# 
# Explanation: n is already a perfect square, Alice can win with one move,
# removing 4 stones (4 -> 0).
# 
# 
# Constraints:
#         1 <= n <= 10⁵


# Solution: https://algo.monster/liteproblems/1510
# Credit: AlgoMonster
def winner_square_game(n):
    from functools import cache
    
    @cache
    def can_win(remaining_stones):
        # Base case: no stones left means previous player took the last stone
        if remaining_stones == 0:
            return False
        
        # Try all possible moves (removing perfect square number of stones)
        square_root = 1
        while square_root * square_root <= remaining_stones:
            stones_to_remove = square_root * square_root
            
            # If opponent cannot win after our move, then we can win
            if not can_win(remaining_stones - stones_to_remove):
                return True
                
            square_root += 1
        
        # No winning move found
        return False
    
    # Alice starts first, check if she can win
    return can_win(n)
    # Time: O(n * √n)
    # Space: O(n)


def main():
    result = winner_square_game(n = 1)
    print(result) # True

    result = winner_square_game(n = 2)
    print(result) # False

    result = winner_square_game(n = 4)
    print(result) # True

if __name__ == "__main__":
    main()
