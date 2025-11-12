# --------------------
# 39. Combination Sum
# --------------------

# Problem: https://leetcode.com/problems/combination-sum/description/
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen 
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen 
# numbers is different.
# 
# The test cases are generated such that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.

# Solution: https://youtu.be/GBKI9VSKdGg
# Credit: Navdeep Singh founder of NeetCode 
def combinations_sum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res

# Solution: https://youtu.be/utBw5FbYswk
# Credit: Greg Hogg
def combinations_sum_alt(candidates, target):
    # Time: O(n^t)
    # Space: O(n)
    res, sol = [], []
    nums = candidates
    n = len(nums)

    def backtrack(i, cur_sum):
        if cur_sum == target:
            res.append(sol[:])
            return
        
        if cur_sum > target or i == n:
            return
        
        backtrack(i+1, cur_sum)

        sol.append(nums[i])
        backtrack(i, cur_sum+nums[i])
        sol.pop()
    
    backtrack(0, 0)
    return res

def main():
    result = combinations_sum(candidates = [2,3,6,7], target = 7) # [[2,2,3],[7]]
    print(result)
    result = combinations_sum(candidates = [2,3,5], target = 8) # [[2,2,2,2],[2,3,3],[3,5]]
    print(result)
    result = combinations_sum(candidates = [2], target = 1) # []
    print(result)

if __name__ == "__main__":
    main()