# -----------------------------------------------
# 2660. Determine the Winner of a Bowling Game 🎳
# -----------------------------------------------

# Problem: https://leetcode.com/problems/determine-the-winner-of-a-bowling-game
#
# You are given two 0-indexed integer arrays player1 and player2, representing the
# number of pins that player 1 and player 2 hit in a bowling game, respectively.
# 
# The bowling game consists of n turns, and the number of pins in each turn is
# exactly 10.
# 
# Assume a player hits xᵢ pins in the iᵗʰ turn. The value of the ith turn for the
# player is:
# 
#         2xᵢ if the player hits 10 pins in either (i - 1)ᵗʰ or (i - 2)ᵗʰ turn.
#         Otherwise, it is xᵢ.
# 
# The score of the player is the sum of the values of their n turns.
# 
# Return
#         1 if the score of player 1 is more than the score of player 2,
#         2 if the score of player 2 is more than the score of player 1, and
#         0 in case of a draw.
# 
# Example 1:
# 
# Input: player1 = [5,10,3,2], player2 = [6,5,7,3]
# Output: 1
# 
# Explanation:
# The score of player 1 is 5 + 10 + 2*3 + 2*2 = 25.
# The score of player 2 is 6 + 5 + 7 + 3 = 21.
# 
# Example 2:
# 
# Input: player1 = [3,5,7,6], player2 = [8,10,10,2]
# Output: 2
# 
# Explanation:
# The score of player 1 is 3 + 5 + 7 + 6 = 21.
# The score of player 2 is 8 + 10 + 2*10 + 2*2 = 42.
# 
# Example 3:
# 
# Input: player1 = [2,3], player2 = [4,1]
# Output: 0
# 
# Explanation:
# The score of player1 is 2 + 3 = 5.
# The score of player2 is 4 + 1 = 5.
# 
# Example 4:
# 
# Input: player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]
# Output: 2
# 
# Explanation:
# The score of player1 is 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73.
# The score of player2 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75.
# 
# Constraints:
#         n == player1.length == player2.length
#         1 <= n <= 1000
#         0 <= player1[i], player2[i] <= 10


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def is_winner(player1, player2):
    def calculate(a):
        s = 0
        for i in range(len(a)):
            if(i-1 >= 0 and a[i-1] == 10) or (i-2 >= 0 and a[i-2] == 10):
                s += (a[i]*2)
            else:
                s += a[i]
        return s   

    score1 = calculate(player1)
    score2 = calculate(player2)
    
    if score1 > score2:
        return 1
    
    elif score1 < score2:
        return 2
    
    return 0
    # Time: O(n)
    # Space: O(1)


def main():
    result = is_winner(player1 = [5,10,3,2], player2 = [6,5,7,3])
    print(result) # 1

    result = is_winner(player1 = [3,5,7,6], player2 = [8,10,10,2])
    print(result) # 2

    result = is_winner(player1 = [2,3], player2 = [4,1])
    print(result) # 0

    result = is_winner(player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1])
    print(result) # 2

if __name__ == "__main__":
    main()
