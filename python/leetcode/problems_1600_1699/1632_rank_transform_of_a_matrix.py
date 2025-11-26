# --------------------------------
# 1632. Rank Transform of a Matrix
# --------------------------------

# Problem: https://leetcode.com/problems/rank-transform-of-a-matrix
#
# Given an m x n matrix, return a new matrix answer where answer[row][col] is the
# rank of matrix[row][col].
# 
# The rank is an integer that represents how large an element is compared to other
# elements. It is calculated using the following rules:
#         
#   * The rank is an integer starting from 1.
#   * If two elements p and q are in the same row or column, then:
#       * If p < q then rank(p) < rank(q)
#       * If p == q then rank(p) == rank(q)
#       * If p > q then rank(p) > rank(q)
#   * The rank should be as small as possible.
# 
# The test cases are generated so that answer is unique under the given rules.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/10/18/rank1.jpg
# 
# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# 
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row and
# column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and
# matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and
# matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1]
# > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
# 
# Example 2:
# 
# https://assets.leetcode.com/uploads/2020/10/18/rank2.jpg
# 
# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
# 
# Example 3:
# 
# https://assets.leetcode.com/uploads/2020/10/18/rank3.jpg
# 
# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
# 
# 
# Constraints:
#         m == matrix.length
#         n == matrix[i].length
#         1 <= m, n <= 500
#         -10⁹ <= matrix[row][col] <= 10⁹


# Solution: https://algo.monster/liteproblems/1632
# Credit: AlgoMonster
def matrix_rank_transform(matrix):
    from collections import defaultdict
    m, n = len(matrix), len(matrix[0])
    
    # Group all positions by their values
    value_to_positions = defaultdict(list)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            value_to_positions[value].append((i, j))
    
    # Track maximum rank achieved in each row and column
    row_max_rank = [0] * m
    col_max_rank = [0] * n
    
    # Initialize result matrix
    result = [[0] * n for _ in range(m)]
    
    # Union-Find to handle rows and columns (rows: 0 to m-1, columns: m to m+n-1)
    uf = UnionFind(m + n)
    
    # Process values in ascending order
    for value in sorted(value_to_positions.keys()):
        # Dictionary to store the maximum rank for each connected component
        component_max_rank = defaultdict(int)
        
        # Union all positions with the same value that share row or column
        for row, col in value_to_positions[value]:
            # Connect row and column (column index offset by m)
            uf.union(row, col + m)
        
        # Find maximum existing rank for each connected component
        for row, col in value_to_positions[value]:
            root = uf.find(row)
            # Component's rank should be at least 1 more than max of row/col
            component_max_rank[root] = max(
                component_max_rank[root], 
                row_max_rank[row], 
                col_max_rank[col]
            )
        
        # Assign ranks to all positions with current value
        for row, col in value_to_positions[value]:
            root = uf.find(row)
            new_rank = 1 + component_max_rank[root]
            result[row][col] = new_rank
            row_max_rank[row] = new_rank
            col_max_rank[col] = new_rank
        
        # Reset Union-Find for next value group
        for row, col in value_to_positions[value]:
            uf.reset(row)
            uf.reset(col + m)
    
    return result
    # Time: O(mn * log(mn) + mn * α(m+n))
    # Space: O(mn)

class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression and union by size."""
  
    def __init__(self, n: int) -> None:
        """Initialize Union-Find structure with n elements."""
        self.parent = list(range(n))  # Each element is its own parent initially
        self.size = [1] * n  # Size of each component is 1 initially
  
    def find(self, x: int) -> int:
        """Find the root of element x with path compression."""
        if self.parent[x] != x:
            # Path compression: make all nodes point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
  
    def union(self, a: int, b: int) -> None:
        """Union two elements a and b by size (attach smaller tree to larger)."""
        root_a, root_b = self.find(a), self.find(b)
      
        if root_a != root_b:
            # Union by size: attach smaller component to larger one
            if self.size[root_a] > self.size[root_b]:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]
  
    def reset(self, x: int) -> None:
        """Reset element x to be its own parent with size 1."""
        self.parent[x] = x
        self.size[x] = 1


def main():
    result = matrix_rank_transform(matrix = [[1,2],[3,4]])
    print(result) # [[1, 2], [2, 3]]

    result = matrix_rank_transform(matrix = [[7,7],[7,7]])
    print(result) # [[1, 1], [1, 1]]

    result = matrix_rank_transform(matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]])
    print(result) # [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]]

if __name__ == "__main__":
    main()
