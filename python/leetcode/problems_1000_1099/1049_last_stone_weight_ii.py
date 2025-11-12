# -----------------------------
# 1049. Last Stone Weight II 🪨
# -----------------------------

# Problem: https://leetcode.com/problems/last-stone-weight-ii
#
# You are given an array of integers stones where stones[i] is the weight of the
# ith stone.
# 
# We are playing a game with the stones. On each turn, we choose any two stones
# and smash them together. Suppose the stones have weights x and y with x <= y.
# 
# The result of this smash is:
#         - If x == y, both stones are destroyed, and
#         - If x != y, the stone of weight x is destroyed, and the stone of weight y
#           has new weight y - x.
# 
# At the end of the game, there is at most one stone left.
# 
# Return the smallest possible weight of the left stone. If there are no stones
# left, return 0.
# 
# Example 1:
# 
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0, so the array converts to [1], then that's the
# optimal value.
# 
# Example 2:
# 
# Input: stones = [31,26,33,21,40]
# Output: 5
# 
# Constraints:
#         1 <= stones.length <= 30
#         1 <= stones[i] <= 100


# Solution: https://www.youtube.com/watch?v=gdXkkmzvR3c
# Credit: Navdeep Singh founder of NeetCode
def last_stone_weight_ii(stones):
    total_weight = sum(stones)
    target = total_weight // 2

    def dfs(i, total):
        if total >= target or i == len(stones):
            return abs(total - (total_weight - total))
        if (i, total) in dp:
            return dp[ (i,total) ]
        
        dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
        return dp[(i, total)]
        
    dp = {}
    return dfs(0, 0)

# Better solution ?
def last_stone_weight_ii_best(stones):
    dp = {0}
    for weight in stones:
        new_dp = set()
        for s in dp:
            new_dp.add(s+weight)
            new_dp.add(s-weight)
        dp = new_dp
    return min([s if s>=0 else float("inf") for s in dp])


def main():
    result = last_stone_weight_ii([2,7,4,1,8,1])
    print(result) # 1

    result = last_stone_weight_ii([31,26,33,21,40])
    print(result) # 5

if __name__ == "__main__":
    main()
