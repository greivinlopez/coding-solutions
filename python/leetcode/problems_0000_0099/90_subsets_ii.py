# ---------------
# 90. Subsets II
# ---------------

# Problem: https://leetcode.com/problems/subsets-ii/
# 
# Given an integer array nums that may contain duplicates, return all possible 
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in 
# any order.

# Solution: https://youtu.be/Vn2v6ajA7U0
# Credit: Navdeep Singh founder of NeetCode
def subsets_with_dup(nums):
    # Time: O(n * 2^n)
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return

        # All subsets that include nums[i]
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        # All subsets that don't include nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res


def main():
    nums = [1,2,2]
    result = subsets_with_dup(nums)
    print(result) # [[],[1],[1,2],[1,2,2],[2],[2,2]]

    nums = [0]
    result = subsets_with_dup(nums)
    print(result) # [[],[0]]

if __name__ == "__main__":
    main()