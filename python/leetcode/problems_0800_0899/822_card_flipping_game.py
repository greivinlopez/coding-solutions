# -----------------------
# 822. Card Flipping Game
# -----------------------

# Problem: https://leetcode.com/problems/card-flipping-game
#
# You are given two 0-indexed integer arrays fronts and backs of length n, where
# the ith card has the positive integer fronts[i] printed on the front and
# backs[i] printed on the back. Initially, each card is placed on a table such
# that the front number is facing up and the other is facing down. You may flip
# over any number of cards (possibly zero).
# 
# After flipping the cards, an integer is considered good if it is facing down on
# some card and not facing up on any card.
# 
# Return the minimum possible good integer after flipping the cards. If there are
# no good integers, return 0.
# 
# Example 1:
# 
# Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
# Output: 2
# 
# Explanation:
# If we flip the second card, the face up numbers are [1,3,4,4,7] and the face
# down are [1,2,4,1,3].
# 2 is the minimum good integer as it appears facing down but not facing up.
# It can be shown that 2 is the minimum possible good integer obtainable after
# flipping some cards.
# 
# Example 2:
# 
# Input: fronts = [1], backs = [1]
# Output: 0
# 
# Explanation:
# There are no good integers no matter how we flip the cards, so we return 0.
# 
# 
# Constraints:
#         n == fronts.length == backs.length
#         1 <= n <= 1000
#         1 <= fronts[i], backs[i] <= 2000

from itertools import chain

# Solution: https://algo.monster/liteproblems/822
# Credit: AlgoMonster
def flip_game(fronts, backs):
    # Find all numbers that appear on both sides of the same card
    # These numbers cannot be the answer since flipping won't help
    same_on_both_sides = {front for front, back in zip(fronts, backs) if front == back}
    
    # Find the minimum number from all cards (both fronts and backs)
    # that is not in the set of numbers appearing on both sides
    # If no valid number exists, return 0 as default
    return min((number for number in chain(fronts, backs) 
                if number not in same_on_both_sides), default=0)
    # Time: O(n)
    # Space: O(n)


def main():
    result = flip_game(fronts = [1,2,4,4,7], backs = [1,3,4,1,3])
    print(result) # 2

    result = flip_game(fronts = [1], backs = [1])
    print(result) # 0

if __name__ == "__main__":
    main()
