# ---------------------------------------
# 1627. Graph Connectivity With Threshold
# ---------------------------------------

# Problem: https://leetcode.com/problems/graph-connectivity-with-threshold
#
# We have n cities labeled from 1 to n. Two different cities with labels x and y
# are directly connected by a bidirectional road if and only if x and y share a
# common divisor strictly greater than some threshold. More formally, cities with
# labels x and y have a road between them if there exists an integer z such that
# all of the following are true:
# 
#         x % z == 0,
#         y % z == 0, and
#         z > threshold.
# 
# Given the two integers, n and threshold, and an array of queries, you must
# determine for each queries[i] = [aᵢ, bᵢ] if cities aᵢ and bᵢ are connected
# directly or indirectly. (i.e. there is some path between them).
# 
# Return an array answer, where answer.length == queries.length and answer[i] is
# true if for the iᵗʰ query, there is a path between aᵢ and bᵢ, or answer[i] is
# false if there is no path.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/09/ex1.jpg
# 
# Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
# Output: [false,false,true]
# 
# Explanation: The divisors for each number:
# 1:   1
# 2:   1, 2
# 3:   1, 3
# 4:   1, 2, 4
# 5:   1, 5
# 6:   1, 2, 3, 6
# Using the underlined divisors above the threshold, only cities 3 and 6 share a
# common divisor, so they are the
# only ones directly connected. The result of each query:
# [1,4]   1 is not connected to 4
# [2,5]   2 is not connected to 5
# [3,6]   3 is connected to 6 through path 3--6
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/10/tmp.jpg
# 
# Input: n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
# Output: [true,true,true,true,true]
# 
# Explanation: The divisors for each number are the same as the previous example.
# However, since the threshold is 0,
# all divisors can be used. Since all numbers share 1 as a divisor, all cities are
# connected.
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/10/17/ex3.jpg
# 
# Input: n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
# Output: [false,false,false,false,false]
# Explanation: Only cities 2 and 4 share a common divisor 2 which is strictly
# greater than the threshold 1, so they are the only ones directly connected.
# Please notice that there can be multiple queries for the same pair of nodes [x,
# y], and that the query [x, y] is equivalent to the query [y, x].
# 
# 
# Constraints:
#         2 <= n <= 10⁴
#         0 <= threshold <= n
#         1 <= queries.length <= 10⁵
#         queries[i].length == 2
#         1 <= aᵢ, bᵢ <= cities
#         aᵢ != bᵢ


# Solution: https://algo.monster/liteproblems/1627
# Credit: AlgoMonster
def are_connected(n, threshold, queries):
    # Initialize Union-Find with n+1 elements (to handle 1-indexed numbers)
    union_find = UnionFind(n + 1)
    
    # Connect all numbers that share a common divisor > threshold
    # For each potential divisor greater than threshold
    for divisor in range(threshold + 1, n + 1):
        # Connect all multiples of this divisor
        # Start from 2*divisor and increment by divisor to get all multiples
        for multiple in range(divisor + divisor, n + 1, divisor):
            # Union the divisor with its multiple
            # This creates connected components of numbers sharing common divisors
            union_find.union(divisor, multiple)
    
    # Check each query pair to see if they're in the same component
    # Two numbers are connected if they have the same root in the Union-Find
    return [union_find.find(a) == union_find.find(b) for a, b in queries]
    # Time: O(n * log n * α(n) + q)
    # Space: O(n)

class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure with path compression 
    and union by size optimization.
    """
  
    def __init__(self, n: int) -> None:
        """
        Initialize the Union-Find structure with n elements (0 to n-1).
      
        Args:
            n: Number of elements in the structure
        """
        # Each element is initially its own parent (represents n disjoint sets)
        self.parent = list(range(n))
        # Track the size of each component for union by size optimization
        self.component_size = [1] * n
  
    def find(self, x: int) -> int:
        """
        Find the root/representative of the component containing element x.
        Uses path compression to optimize future queries.
      
        Args:
            x: The element whose root we want to find
          
        Returns:
            The root element of the component containing x
        """
        # Path compression: make all nodes on the path point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
  
    def union(self, a: int, b: int) -> bool:
        """
        Unite the components containing elements a and b.
        Uses union by size to keep the tree balanced.
      
        Args:
            a: First element
            b: Second element
          
        Returns:
            True if the elements were in different components (union performed),
            False if they were already in the same component
        """
        # Find the roots of both elements
        root_a, root_b = self.find(a), self.find(b)
      
        # Already in the same component
        if root_a == root_b:
            return False
      
        # Union by size: attach smaller tree under the root of larger tree
        if self.component_size[root_a] > self.component_size[root_b]:
            self.parent[root_b] = root_a
            self.component_size[root_a] += self.component_size[root_b]
        else:
            self.parent[root_a] = root_b
            self.component_size[root_b] += self.component_size[root_a]
      
        return True


def main():
    result = are_connected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]])
    print(result) # [False, False, True]

    result = are_connected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]])
    print(result) # [True, True, True, True, True]

    result = are_connected(n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]])
    print(result) # [False, False, False, False, False]

if __name__ == "__main__":
    main()
