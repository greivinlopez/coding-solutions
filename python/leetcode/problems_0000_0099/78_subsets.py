# ------------
# 78. Subsets
# ------------

# Problem: https://leetcode.com/problems/combinations/
# 
# Given an integer array nums of unique elements, return all possible 
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

# Solution: https://youtu.be/REOH22Xwdkk
# Credit: Navdeep Singh founder of NeetCode
def subsets(nums):
    res = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

# Solution: https://youtu.be/UP3dOYJa05s
# Credit: Greg Hogg
def subsets_alt(nums):
    # Time: O(2^n)
    # Space: O(n)
    n = len(nums)
    ans, sol = [], []

    def backtrack(i):
        if i == n:
            ans.append(sol[:])
            return

        # Don't pick nums[i]
        backtrack(i + 1)

        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()

    backtrack(0)
    return ans

def main():
    result = subsets([1,2,3]) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(result)
    result = subsets([0]) # [[],[0]]
    print(result)

if __name__ == "__main__":
    main()