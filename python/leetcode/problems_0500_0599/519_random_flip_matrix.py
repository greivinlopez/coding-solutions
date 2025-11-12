# -----------------------
# 519. Random Flip Matrix
# -----------------------

# Problem: https://leetcode.com/problems/random-flip-matrix
#
# There is an m x n binary grid matrix with all the values set 0 initially. Design
# an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips
# it to 1. All the indices (i, j) where matrix[i][j] == 0 should be equally likely
# to be returned.
# 
# Optimize your algorithm to minimize the number of calls made to the built-in
# random function of your language and optimize the time and space complexity.
# 
# Implement the Solution class:
#         
#   * Solution(int m, int n) Initializes the object with the size of the
#     binary matrix m and n.
#   * int[] flip() Returns a random index [i, j] of the matrix where 
#     matrix[i][j] == 0 and flips it to 1.
#   * void reset() Resets all the values of the matrix to be 0.
#
# Example 1:
# 
# Input
# ["Solution", "flip", "flip", "flip", "reset", "flip"]
# [[3, 1], [], [], [], [], []]
# Output
# [null, [1, 0], [2, 0], [0, 0], null, [2, 0]]
# 
# Explanation
# Solution solution = new Solution(3, 1);
# solution.flip();  // return [1, 0], [0,0], [1,0], and [2,0] should be equally
# likely to be returned.
# solution.flip();  // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
# solution.flip();  // return [0, 0], Based on the previously returned indices,
# only [0,0] can be returned.
# solution.reset(); // All the values are reset to 0 and can be returned.
# solution.flip();  // return [2, 0], [0,0], [1,0], and [2,0] should be equally
# likely to be returned.
# 
# 
# Constraints:
#         1 <= m, n <= 10⁴
#         There will be at least one free cell for each call to flip.
#         At most 1000 calls will be made to flip and reset.

from typing import List
import random

# Solution: https://algo.monster/liteproblems/519
# Credit: AlgoMonster
class Solution:
    def __init__(self, m: int, n: int):
        """
        Initialize the matrix flipper with dimensions m x n.
      
        Args:
            m: Number of rows in the matrix
            n: Number of columns in the matrix
        """
        self.rows = m
        self.cols = n
        self.total_cells = m * n
        # Virtual mapping to track swapped positions
        # Maps original index to its current value after swaps
        self.index_mapping = {}

    def flip(self) -> List[int]:
        """
        Randomly select and flip a cell that hasn't been flipped yet.
        Uses Fisher-Yates shuffle concept with virtual mapping.
      
        Returns:
            List containing [row, column] of the flipped cell
        """
        # Decrease available cells count
        self.total_cells -= 1
      
        # Generate random index from remaining unflipped cells
        random_index = random.randint(0, self.total_cells)
      
        # Get the actual index (considering previous swaps)
        # If random_index has been swapped before, use its mapped value
        # Otherwise, use random_index itself
        actual_index = self.index_mapping.get(random_index, random_index)
      
        # Swap the selected index with the last available index
        # This ensures we don't select the same cell twice
        last_index_value = self.index_mapping.get(self.total_cells, self.total_cells)
        self.index_mapping[random_index] = last_index_value
      
        # Convert 1D index to 2D coordinates [row, column]
        row = actual_index // self.cols
        col = actual_index % self.cols
      
        return [row, col]

    def reset(self) -> None:
        """
        Reset all flipped cells back to their original state.
        Clears the mapping and resets the total count.
        """
        self.total_cells = self.rows * self.cols
        self.index_mapping.clear()


def main():
    print("TO DO")

if __name__ == "__main__":
    main()
