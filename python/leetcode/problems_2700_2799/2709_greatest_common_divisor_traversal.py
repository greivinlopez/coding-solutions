# ---------------------------------------
# 2709. Greatest Common Divisor Traversal
# ---------------------------------------

# Problem: https://leetcode.com/problems/greatest-common-divisor-traversal
#
# You are given a 0-indexed integer array nums, and you are allowed to traverse
# between its indices. You can traverse between index i and index j, i != j, if
# and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.
# 
# Your task is to determine if for every pair of indices i and j in nums, where i
# < j, there exists a sequence of traversals that can take us from i to j.
# 
# Return true if it is possible to traverse between all such pairs of indices, or
# false otherwise.
# 
# Example 1:
# 
# Input: nums = [2,3,6]
# Output: true
# Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0,
# 2), and (1, 2).
# To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 ->
# 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2,
# 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1])
# = gcd(6, 3) = 3 > 1.
# To go from index 0 to index 2, we can just go directly because gcd(nums[0],
# nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can
# just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
# 
# Example 2:
# 
# Input: nums = [3,9,5]
# Output: false
# Explanation: No sequence of traversals can take us from index 0 to index 2 in
# this example. So, we return false.
# 
# Example 3:
# 
# Input: nums = [4,3,12,8]
# Output: true
# Explanation: There are 6 possible pairs of indices to traverse between: (0, 1),
# (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals
# exists for each pair, so we return true.
# 
# 
# Constraints:
#         1 <= nums.length <= 10^5
#         1 <= nums[i] <= 10^5


# Solution: https://youtu.be/jZ-RVp5CVYY
# Credit: Navdeep Singh founder of NeetCode
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]
        self.count -=1

def can_traverse_all_pairs(nums):
    uf = UnionFind(len(nums))

    factor_index = {}
    for i, n in enumerate(nums):
        f = 2
        while f * f <= n:
            if n % f == 0:
                if f in factor_index:
                    uf.union(i, factor_index[f])
                else:
                    factor_index[f] = i
                while n % f == 0:
                    n = n // f
            f += 1
        if n > 1:
            if n in factor_index:
                uf.union(i, factor_index[n])
            else:
                factor_index[n] = i
    return uf.count == 1


def main():
    result = can_traverse_all_pairs([2,3,6])
    print(result) # True

    result = can_traverse_all_pairs([3,9,5])
    print(result) # False

    result = can_traverse_all_pairs([4,3,12,8])
    print(result) # True

if __name__ == "__main__":
    main()
