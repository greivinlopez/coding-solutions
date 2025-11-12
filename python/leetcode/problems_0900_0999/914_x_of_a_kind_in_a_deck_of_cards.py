# -----------------------------------
# 914. X of a Kind in a Deck of Cards
# -----------------------------------

# Problem: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards
#
# You are given an integer array deck where deck[i] represents the number written
# on the ith card.
# 
# Partition the cards into one or more groups such that:
#         
#   * Each group has exactly x cards where x > 1, and
#   * All the cards in one group have the same integer written on them.
# 
# Return true if such partition is possible, or false otherwise.
# 
# Example 1:
# 
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# 
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# 
# Example 2:
# 
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# 
# Explanation: No possible partition.
# 
# 
# Constraints:
#         1 <= deck.length <= 10⁴
#         0 <= deck[i] < 10⁴

from collections import Counter
from functools import reduce
from math import gcd

# Solution: https://algo.monster/liteproblems/914
# Credit: AlgoMonster
def has_groups_size_x(deck):
    # Count the frequency of each card value in the deck
    card_counts = Counter(deck)
    
    # Find the GCD of all frequency counts
    # If the GCD is at least 2, we can partition the deck into groups of equal size
    # where each group contains cards of the same value
    common_divisor = reduce(gcd, card_counts.values())
    
    # Return True if we can form groups of size >= 2
    return common_divisor >= 2
    # Time: O(n + k * log(m))
    # Space: O(k)
    # n = length of the array deck
    # m = maximum count value in Counter
    # k = number of unique values in deck


def main():
    result = has_groups_size_x(deck = [1,2,3,4,4,3,2,1])
    print(result) # True

    result = has_groups_size_x(deck = [1,1,1,2,2,2,3,3])
    print(result) # False

if __name__ == "__main__":
    main()
