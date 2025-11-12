# -----------------------
# 40. Combination Sum II
# -----------------------

# Problem: https://leetcode.com/problems/combination-sum-ii/
# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.

# Solution: https://www.youtube.com/watch?v=FOyRpNUSFeA
# Credit: Navdeep Singh founder of NeetCode 
def combination_sum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(cur, pos, target):
        if target == 0:
            res.append(cur.copy())
            return
        if target <= 0:
            return

        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur, i + 1, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack([], 0, target)
    return res

def main():
    result = combination_sum2(candidates = [10,1,2,7,6,1,5], target = 8) # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    print(result)
    result = combination_sum2(candidates = [2,5,2,1,2], target = 5) # [[1, 2, 2], [5]]
    print(result)

if __name__ == "__main__":
    main()