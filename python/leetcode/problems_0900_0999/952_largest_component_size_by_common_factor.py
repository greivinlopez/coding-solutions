# --------------------------------------------
# 952. Largest Component Size by Common Factor
# --------------------------------------------

# Problem: https://leetcode.com/problems/largest-component-size-by-common-factor
#
# You are given an integer array of unique positive integers nums. Consider the
# following graph:
#         
#   * There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
#   * There is an undirected edge between nums[i] and nums[j] if nums[i] and
#     nums[j] share a common factor greater than 1.
# 
# Return the size of the largest connected component in the graph.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2018/12/01/ex1.png
# 
# Input: nums = [4,6,15,35]
# Output: 4
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2018/12/01/ex2.png
# 
# Input: nums = [20,50,9,63]
# Output: 2
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2018/12/01/ex3.png
# 
# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8
# 
# 
# Constraints:
#         1 <= nums.length <= 2 * 10⁴
#         1 <= nums[i] <= 10⁵
#         All the values of nums are unique.

from collections import Counter

# Solution: https://algo.monster/liteproblems/952
# Credit: AlgoMonster
class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression."""

    def __init__(self, n: int) -> None:
        """Initialize n disjoint sets, each element is its own parent initially."""
        self.parent = list(range(n))
  
    def union(self, a: int, b: int) -> None:
        """Unite the sets containing elements a and b."""
        root_a = self.find(a)
        root_b = self.find(b)
      
        # Only unite if they belong to different sets
        if root_a != root_b:
            self.parent[root_a] = root_b
  
    def find(self, x: int) -> int:
        """Find the root of the set containing x with path compression."""
        if self.parent[x] != x:
            # Path compression: make every node point directly to the root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

def largest_component_size(nums):
    # Create UnionFind structure with size equal to max value + 1
    max_value = max(nums)
    union_find = UnionFind(max_value + 1)
    
    # For each number, connect it with all its factors
    for num in nums:
        # Find all factors by iterating up to sqrt(num)
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                # Connect num with its factor
                union_find.union(num, factor)
                # Connect num with its complementary factor (num // factor)
                union_find.union(num, num // factor)
            factor += 1
    
    # Count the size of each connected component
    # by finding the root of each number and counting occurrences
    component_sizes = Counter(union_find.find(num) for num in nums)
    
    # Return the size of the largest component
    return max(component_sizes.values())
    # Time: O(n * √m * α(m))
    # Space: O(m)
    # n = the length of the input array
    # m = the maximum value in the array
    # α is the inverse Ackermann function.


def main():
    result = largest_component_size(nums = [4,6,15,35])
    print(result) # 4

    result = largest_component_size(nums = [20,50,9,63])
    print(result) # 2

    result = largest_component_size(nums = [2,3,6,7,4,12,21,39])
    print(result) # 8

if __name__ == "__main__":
    main()
