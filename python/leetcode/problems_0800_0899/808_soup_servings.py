# ---------------------
# 808. Soup Servings 🍲
# ---------------------

# Problem: https://leetcode.com/problems/soup-servings
#
# You have two soups, A and B, each starting with n mL. On every turn, one of the
# following four serving operations is chosen at random, each with probability
# 0.25 independent of all previous turns:
#
#         pour 100 mL from type A and 0 mL from type B
#         pour 75 mL from type A and 25 mL from type B
#         pour 50 mL from type A and 50 mL from type B
#         pour 25 mL from type A and 75 mL from type B
# 
# Note:
#         
#   * There is no operation that pours 0 mL from A and 100 mL from B.
#   * The amounts from A and B are poured simultaneously during the turn.
#   * If an operation asks you to pour more than you have left of a soup, pour
#     all that remains of that soup.
# 
# The process stops immediately after any turn in which one of the soups is used
# up.
# 
# Return the probability that A is used up before B, plus half the probability
# that both soups are used up in the same turn. Answers within 10-5 of the actual
# answer will be accepted.
# 
# Example 1:
# 
# Input: n = 50
# Output: 0.62500
# 
# Explanation:
# If we perform either of the first two serving operations, soup A will become
# empty first.
# If we perform the third operation, A and B will become empty at the same time.
# If we perform the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability
# that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
# 
# Example 2:
# 
# Input: n = 100
# Output: 0.71875
# 
# Explanation:
# If we perform the first serving operation, soup A will become empty first.
# If we perform the second serving operations, A will become empty on performing
# operation [1, 2, 3], and both A and B become empty on performing operation 4.
# If we perform the third operation, A will become empty on performing operation
# [1, 2], and both A and B become empty on performing operation 3.
# If we perform the fourth operation, A will become empty on performing operation
# 1, and both A and B become empty on performing operation 2.
# So the total probability of A becoming empty first plus half the probability
# that A and B become empty at the same time, is 0.71875.
# 
# 
# Constraints:
#         0 <= n <= 10⁹

from functools import cache

# Solution: https://algo.monster/liteproblems/808
# Credit: AlgoMonster
def soup_servings(n):
    # For large n values, the probability approaches 1 due to asymmetric serving sizes
    # (A is served more on average than B: 2.5 vs 1.5 units per operation)
    if n > 4800:
        return 1.0
    
    # Scale down by 25ml to reduce computation (all serving sizes are multiples of 25)
    # Add 24 before dividing to handle ceiling division
    scaled_n = (n + 24) // 25
    
    @cache
    def calculate_probability(soup_a: int, soup_b: int) -> float:
        # Base cases
        # Both soups empty at the same time
        if soup_a <= 0 and soup_b <= 0:
            return 0.5
        
        # Soup A empties first
        if soup_a <= 0:
            return 1.0
        
        # Soup B empties first
        if soup_b <= 0:
            return 0.0
        
        # Recursive case: equal probability (0.25) for each of 4 operations
        # Operation 1: Serve 100ml A, 0ml B (scaled: 4, 0)
        # Operation 2: Serve 75ml A, 25ml B (scaled: 3, 1)
        # Operation 3: Serve 50ml A, 50ml B (scaled: 2, 2)
        # Operation 4: Serve 25ml A, 75ml B (scaled: 1, 3)
        probability = 0.25 * (
            calculate_probability(soup_a - 4, soup_b) +      # Operation 1
            calculate_probability(soup_a - 3, soup_b - 1) +  # Operation 2
            calculate_probability(soup_a - 2, soup_b - 2) +  # Operation 3
            calculate_probability(soup_a - 1, soup_b - 3)    # Operation 4
        )
        
        return probability
    
    return calculate_probability(scaled_n, scaled_n)
    # Time: O(n²)
    # Space: O(n²)
    # n = the input value (scaled down by 25)


def main():
    result = soup_servings(50)
    print(result) # 0.62500

    result = soup_servings(100)
    print(result) # 0.71875

if __name__ == "__main__":
    main()
