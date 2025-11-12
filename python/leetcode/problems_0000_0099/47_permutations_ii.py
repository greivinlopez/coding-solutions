# --------------------
# 47. Permutations II
# --------------------

# Problem: https://leetcode.com/problems/permutations-ii/
# Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.

# Solution: https://youtu.be/qhBVWf0YafA
# Credit: Navdeep Singh founder of NeetCode 
import collections
def permute_unique(nums):
    # Time: O(n * 2^nh)
    result = []
    counter = collections.Counter(nums)

    def backtrack(perm, counter):
        if len(perm) == len(nums):
            result.append(perm.copy())

        for n in counter:
            if counter[n] == 0:
                continue
            perm.append(n)
            counter[n] -= 1
            backtrack(perm, counter)
            perm.pop()
            counter[n] += 1

    backtrack([], counter)

    return result

def main():
    result = permute_unique([1,1,2]) # [[1,1,2],[1,2,1],[2,1,1]]
    print(result)
    result = permute_unique([1,2,3]) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(result)

if __name__ == "__main__":
    main()