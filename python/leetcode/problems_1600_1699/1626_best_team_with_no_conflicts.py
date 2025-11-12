# ---------------------------------
# 1626. Best Team With No Conflicts
# ---------------------------------

# Problem: https://leetcode.com/problems/best-team-with-no-conflicts
#
# You are the manager of a basketball team. For the upcoming tournament, you want
# to choose the team with the highest overall score. The score of the team is the
# sum of scores of all the players in the team.
# 
# However, the basketball team is not allowed to have conflicts. A conflict exists
# if a younger player has a strictly higher score than an older player. A conflict
# does not occur between players of the same age.
# 
# Given two lists, scores and ages, where each scores[i] and ages[i] represents
# the score and age of the ith player, respectively, return the highest overall
# score of all possible basketball teams.
# 
# Example 1:
# 
# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# 
# Explanation: You can choose all the players.
# 
# Example 2:
# 
# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# 
# Explanation: It is best to choose the last 3 players. Notice that you are
# allowed to choose multiple people of the same age.
# 
# Example 3:
# 
# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# 
# Explanation: It is best to choose the first 3 players.
# 
# 
# Constraints:
#         1 <= scores.length, ages.length <= 1000
#         scores.length == ages.length
#         1 <= scores[i] <= 10^6
#         1 <= ages[i] <= 1000


# Solution: https://youtu.be/7kURH3btcV4
# Credit: Navdeep Singh founder of NeetCode
def best_team_score_recursive(scores, ages):
    # Recursive solution
    pairs = [[scores[i], ages[i]] for i in range(len(scores))]
    pairs.sort()
    dp = {}

    def dfs(i, j):
        if i == len(pairs):
            return 0
        if (i, j) in dp:
            return dp[(i, j)]

        mScore, mAge = pairs[j] if j >= 0 else [0, 0]
        score, age = pairs[i]
        res = 0

        if not (score > mScore and age < mAge):
            res = dfs(i + 1, i) + score
        
        dp[(i, j)] = max(res, dfs(i + 1, j))
        return dp[(i, j)]

    return dfs(0, -1)
    # Time: O(n²)
    # Space: O(n²)

def best_team_score(scores, ages):
    # Dynamic programming solution
    pairs = [[scores[i], ages[i]] for i in range(len(scores))]
    pairs.sort()
    dp = [pairs[i][0] for i in range(len(pairs))]
    
    for i in range(len(pairs)):
        mScore, mAge = pairs[i]
        for j in range(i):
            score, age = pairs[j]
            if mAge >= age:
                dp[i] = max(dp[i], mScore + dp[j])
    
    return max(dp)
    # Time: O(n²)
    # Space: O(n)


def main():
    result = best_team_score(scores = [1,3,5,10,15], ages = [1,2,3,4,5])
    print(result) # 34

    result = best_team_score(scores = [4,5,6,5], ages = [2,1,2,1])
    print(result) # 16

    result = best_team_score(scores = [1,2,3,5], ages = [8,9,10,1])
    print(result) # 6

if __name__ == "__main__":
    main()
