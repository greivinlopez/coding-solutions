# ------------------------------------------------------------
# 1434. Number of Ways to Wear Different Hats to Each Other 🎩
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other
#
# There are n people and 40 types of hats labeled from 1 to 40.
# 
# Given a 2D integer array hats, where hats[i] is a list of all hats preferred by
# the iᵗʰ person.
# 
# Return the number of ways that n people can wear different hats from each other.
# 
# Since the answer may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: hats = [[3,4],[4,5],[5]]
# Output: 1
# 
# Explanation: There is only one way to choose hats given the conditions.
# First person choose hat 3, Second person choose hat 4 and last one hat 5.
# 
# Example 2:
# 
# Input: hats = [[3,5,1],[3,5]]
# Output: 4
# 
# Explanation: There are 4 ways to choose hats:
# (3,5), (5,3), (1,3) and (1,5)
# 
# Example 3:
# 
# Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# Output: 24
# 
# Explanation: Each person can choose hats labeled from 1 to 4.
# Number of Permutations of (1,2,3,4) = 24.
# 
# 
# Constraints:
#         n == hats.length
#         1 <= n <= 10
#         1 <= hats[i].length <= 40
#         1 <= hats[i][j] <= 40
#         hats[i] contains a list of unique integers.

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1434
# Credit: AlgoMonster
def number_ways(hats):
    # Build a mapping from each hat to the list of people who can wear it
    hat_to_people = defaultdict(list)
    for person_id, person_hats in enumerate(hats):
        for hat in person_hats:
            hat_to_people[hat].append(person_id)
    
    MOD = 10**9 + 7
    num_people = len(hats)
    max_hat_id = max(max(person_hats) for person_hats in hats)
    
    # dp[i][mask] = number of ways to assign first i hats to people
    # where mask represents which people have been assigned hats
    # bit j in mask = 1 means person j has been assigned a hat
    dp = [[0] * (1 << num_people) for _ in range(max_hat_id + 1)]
    
    # Base case: 0 hats considered, no one has a hat = 1 way
    dp[0][0] = 1
    
    # Process each hat from 1 to max_hat_id
    for hat_id in range(1, max_hat_id + 1):
        for people_mask in range(1 << num_people):
            # Option 1: Don't use the current hat
            dp[hat_id][people_mask] = dp[hat_id - 1][people_mask]
            
            # Option 2: Assign current hat to one of the eligible people
            for person in hat_to_people[hat_id]:
                # Check if this person already has a hat in current mask
                if people_mask >> person & 1:
                    # Add ways from previous state where this person didn't have a hat
                    previous_mask = people_mask ^ (1 << person)
                    dp[hat_id][people_mask] = (dp[hat_id][people_mask] + 
                                                dp[hat_id - 1][previous_mask]) % MOD
    
    # Return the number of ways where all hats are considered and all people have hats
    # The mask with all people having hats is (1 << num_people) - 1 = all bits set
    return dp[max_hat_id][(1 << num_people) - 1]
    # Time: O(m * 2ⁿ * n)
    # Space: O(m * 2ⁿ)


def main():
    result = number_ways(hats = [[3,4],[4,5],[5]])
    print(result) # 1

    result = number_ways(hats = [[3,5,1],[3,5]])
    print(result) # 4

    result = number_ways(hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
    print(result) # 24

if __name__ == "__main__":
    main()
