# --------------------------
# 1223. Dice Roll Simulation
# --------------------------

# Problem: https://leetcode.com/problems/dice-roll-simulation
#
# A die simulator generates a random number from 1 to 6 for each roll. You
# introduced a constraint to the generator such that it cannot roll the number i
# more than rollMax[i] (1-indexed) consecutive times.
# 
# Given an array of integers rollMax and an integer n, return the number of
# distinct sequences that can be obtained with exact n rolls. Since the answer may
# be too large, return it modulo 10⁹ + 7.
# 
# Two sequences are considered different if at least one element differs from each
# other.
# 
# Example 1:
# 
# Input: n = 2, rollMax = [1,1,2,2,2,3]
# Output: 34
# 
# Explanation: There will be 2 rolls of die, if there are no constraints on the
# die, there are 6 * 6 = 36 possible combinations. In this case, looking at
# rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore
# sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
# 
# Example 2:
# 
# Input: n = 2, rollMax = [1,1,1,1,1,1]
# Output: 30
# 
# Example 3:
# 
# Input: n = 3, rollMax = [1,1,1,2,2,3]
# Output: 181
# 
# 
# Constraints:
#         1 <= n <= 5000
#         rollMax.length == 6
#         1 <= rollMax[i] <= 15

from functools import cache

# Solution: https://algo.monster/liteproblems/1223
# Credit: AlgoMonster
def die_simulator(n, rollMax):
    MOD = 10**9 + 7
    
    @cache
    def dfs(roll_index, last_number, consecutive_count):
        # Base case: completed all n rolls
        if roll_index >= n:
            return 1
        
        total_sequences = 0
        
        # Try rolling each die face (1 through 6)
        for die_face in range(1, 7):
            if die_face != last_number:
                # Rolling a different number - reset consecutive count to 1
                total_sequences += dfs(roll_index + 1, die_face, 1)
            elif consecutive_count < rollMax[last_number - 1]:
                # Rolling the same number - check if within rollMax limit
                # Note: rollMax is 0-indexed, so we use last_number - 1
                total_sequences += dfs(roll_index + 1, last_number, consecutive_count + 1)
        
        return total_sequences % MOD
    
    # Start with roll_index=0, last_number=0 (no previous roll), consecutive_count=0
    return dfs(0, 0, 0)
    # Time: O(n * k * M)
    # Space: O(n * k * M)
    # n = the number of dice rolls
    # k = 6 the number of faces on the die (constant)
    # M = the maximum value in rollMax array


def main():
    result = die_simulator(n = 2, rollMax = [1,1,2,2,2,3])
    print(result) # 34

    result = die_simulator(n = 2, rollMax = [1,1,1,1,1,1])
    print(result) # 30

    result = die_simulator(n = 3, rollMax = [1,1,1,2,2,3])
    print(result) # 181

if __name__ == "__main__":
    main()
