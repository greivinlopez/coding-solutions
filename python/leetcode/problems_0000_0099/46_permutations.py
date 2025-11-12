# -----------------
# 46. Permutations
# -----------------

# Problem: https://leetcode.com/problems/permutations/
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

# Solution: https://youtu.be/s7AvT7cGdSo
# Credit: Navdeep Singh founder of NeetCode 
def permute(nums):
    # Time: O(n!)
    # Space: O(n)
    res = []

    if len(nums) == 1:
        return [nums[:]]  # nums[:] is a deep copy

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

# Solution: https://youtu.be/gFm1lEfnzUQ
# Credit: Greg Hogg
def permute_alt(nums):
    # Time: O(n!)
    # Space: O(n)
    n = len(nums)
    ans, sol = [], []

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return

        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()

    backtrack()
    return ans

def main():
    result = permute([1,2,3]) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(result)
    result = permute([0,1]) # [[0,1],[1,0]]
    print(result)
    result = permute([1]) # [[1]]
    print(result)

if __name__ == "__main__":
    main()