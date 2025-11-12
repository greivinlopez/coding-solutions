# ---------------------------------------
# 1128. Number of Equivalent Domino Pairs
# ---------------------------------------

# Problem: https://leetcode.com/problems/number-of-equivalent-domino-pairs
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that
# is, one domino can be rotated to be equal to another domino.
# 
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].
# 
# Example 1:
# 
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# 
# Example 2:
# 
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
# 
# 
# Constraints:
#         1 <= dominoes.length <= 4 * 10⁴
#         dominoes[i].length == 2
#         1 <= dominoes[i][j] <= 9

from collections import Counter

# Solution: https://algo.monster/liteproblems/1128
# Credit: AlgoMonster
def num_equiv_domino_pairs(dominoes):
    # Counter to track frequency of normalized dominoes
    domino_count = Counter()
    
    # Total number of equivalent pairs found
    total_pairs = 0
    
    # Process each domino
    for first_val, second_val in dominoes:
        # Normalize the domino by ensuring smaller value comes first
        # This treats [a,b] and [b,a] as equivalent
        normalized_key = first_val * 10 + second_val if first_val < second_val else second_val * 10 + first_val
        
        # Add count of previously seen equivalent dominoes to total
        # (forms pairs with current domino)
        total_pairs += domino_count[normalized_key]
        
        # Increment count for this normalized domino
        domino_count[normalized_key] += 1
    
    return total_pairs
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_equiv_domino_pairs(dominoes = [[1,2],[2,1],[3,4],[5,6]])
    print(result) # 1

    result = num_equiv_domino_pairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]])
    print(result) # 3

if __name__ == "__main__":
    main()
